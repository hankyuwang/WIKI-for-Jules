---
title: AI晶片架構深度問答解析
level: advanced
tags:
  - TPU
  - GPU
  - Systolic Array
---

摘要：本文件針對使用者提出的六個核心問題進行深度分析，涵蓋 NPU 算力與 SRAM 容量關係、TPU 與 CISC/RISC 架構差異、脈動陣列 (Systolic Array) 解析、TPU 與 NVIDIA GPU 架構對比、現代 AI 模型訓練硬體選擇，以及 TPUv8 的集合通訊加速引擎 (CAE) 分析。

## 1. NPU 矩陣算力與 SRAM 的關係
在 NPU 架構中，特別是以矩陣運算為核心的脈動陣列，算力（MAC 單元數量）與所需 SRAM 頻寬往往呈「開根號關係」。
這是因為一個 N x N 的脈動陣列，其運算單元數量為 $N^2$（算力），但邊緣輸入的資料頻寬需求僅為 $O(N)$。因此，在增加算力時，對 SRAM 頻寬的壓力成長較為平緩，這正是脈動陣列高效能的關鍵。

## 2. TPU 與 CISC/RISC 的關聯
傳統 CPU 分為精簡指令集（RISC）與複雜指令集（CISC）。TPU 屬於領域專用架構，其指令集設計更接近 CISC 或 VLIW（超長指令字）。
TPU 使用單一複雜指令（如 `MatrixMultiply`）即可觸發成千上萬個 MAC 單元的運算。這減少了指令抓取與解碼的開銷，將硬體面積最大程度保留給運算單元。

## 3. 脈動陣列（Systolic Array）解析
脈動陣列是一種二維運算陣列。資料如同脈搏般在 PE（Processing Element）之間流動，將前一個 PE 的結果直接傳遞給下一個。
- 相比於 SIMD（如 GPU 的向量單元），脈動陣列大幅減少了從暫存器或 SRAM 讀寫中間變數的次數。
- 相比於存算一體 (CIM)，脈動陣列仍將運算與記憶體分離，但在運算陣列內部實現了極高密度。

## 4. TPU 與 NVIDIA GPU 的架構差異
- **運算核心**：GPU 採用 SIMT 架構，具備強大的通用性與複雜的排程器；TPU 核心是單一龐大的脈動陣列，專注於密集矩陣乘法。
- **記憶體管理**：GPU 擁有硬體管理的 L1/L2 Cache；TPU 則多採用軟體管理的 Scratchpad Memory（由編譯器靜態排程，避免 Cache Miss 的不確定性）。

## 5. 現代 AI 模型訓練：GPU 還是 TPU？
- 科學家大多傾向使用 **NVIDIA GPU**，主要因為 CUDA 建立的無敵軟體生態（如 PyTorch, Triton 等對 GPU 的完美支援）。
- 然而，Google 等巨頭在內部訓練超大模型（如 Gemini）時會大規模使用 TPU 叢集，因其 ICI 互連網路與成本效益在大規模部署下極具優勢。

## 6. TPUv8 與 CAE 潛在分析
雖然 Google 官方尚未完全公開 TPUv8，但可預期其在網路互連上將有重大突破。集合通訊加速引擎 (Collective Acceleration Engine, CAE) 是解決 MoE 模型中 All-to-All 網路瓶頸的關鍵。CAE 將網路通訊從 CPU 卸載到硬體，透過光交換網路大幅降低叢集通訊延遲。

## 架構演進方案探討

### 方案一：強化傳統脈動陣列 (Dense TPU)
- **優點 (Pros)**：硬體實現簡單，稠密矩陣效能極佳。
- **缺點 (Cons)**：處理 MoE 等稀疏模型效率差。
- **成本 (Cost)**：設計成熟，NRE 較低。
- **維護性 (Maintainability)**：編譯器優化相對簡單。
- **風險 (Risk)**：面對新興的稀疏演算法可能算力利用率低下。

### 方案二：支援稀疏運算的彈性陣列
- **優點 (Pros)**：針對 2:4 或非結構化稀疏模型提供顯著的效能提升。
- **缺點 (Cons)**：PE 內部控制邏輯複雜化，面積增大。
- **成本 (Cost)**：硬體設計與驗證成本高。
- **維護性 (Maintainability)**：需要編譯器（如 XLA）深度配合硬體。
- **風險 (Risk)**：若稀疏模式改變，硬體可能無法適應。

### 方案三：整合超大 SRAM 與強大 CAE 的分散式架構
- **優點 (Pros)**：極大化叢集擴展性，解決 Memory Wall 與 Network Wall。
- **缺點 (Cons)**：單晶片良率挑戰大，光互連成本高。
- **成本 (Cost)**：極其高昂的封裝與網路佈建成本。
- **維護性 (Maintainability)**：分散式系統除錯與維護極具挑戰。
- **風險 (Risk)**：技術過於前沿，可能面臨量產延遲。
