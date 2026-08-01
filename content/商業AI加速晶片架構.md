---
title: 商業 AI 加速晶片架構
level: intermediate
tags:
  - hardware
  - architecture
  - npu
  - nvidia
  - amd
  - tpu
---

# 商業 AI 加速晶片架構

## 摘要
隨著大型語言模型 (LLM) 與生成式 AI 的快速發展，專為 AI 計算設計的硬體加速器成為技術核心。本文探討當前市場上三大商業 AI 加速晶片：NVIDIA GPU、AMD Instinct 以及 Google TPU，深入分析其架構特性、記憶體系統及互連技術，並透過三種部署方案的比較，提供在不同情境下的硬體選擇建議。相關的硬體基礎概念可參考 [[NPU架構探索]]。

---

## 1. NVIDIA GPU 架構 (以 Hopper / Blackwell 為例)

NVIDIA 是目前 AI 加速晶片的市場領導者，其架構演進不斷推動 AI 計算的極限。

### 核心架構特點
- **Tensor Cores**: 專為矩陣乘法設計的運算單元。最新架構支援 FP8 等低精度運算，並具備 Transformer Engine 動態調整精度以提升吞吐量。
- **Memory Subsystem**: 採用高頻寬記憶體 (HBM3/HBM3e)，提供極高的記憶體頻寬，對於解決受限於記憶體頻寬的 LLM 推理至關重要。
- **Interconnect**: **NVLink** 與 **NVSwitch** 提供超高速的 GPU 間通訊頻寬 (例如 H100 的 NVLink 可達 900 GB/s)，這對於張量平行 (Tensor Parallelism) 等分散式訓練至關重要。

### 優勢與挑戰
- **優勢**: CUDA 軟體生態系統成熟，幾乎所有主流 AI 框架開箱即用；高頻寬互連技術在叢集擴展性上表現卓越。
- **挑戰**: 功耗極高，需要先進的水冷散熱方案；價格昂貴且面臨供應鏈短缺。

---

## 2. AMD Instinct 架構 (以 MI300X 為例)

AMD MI300X 是針對生成式 AI 訓練與推理推出的高效能加速器，採用小晶片 (Chiplet) 設計。

### 核心架構特點
- **Chiplet Design (CDNA 3)**: 透過 3D 封裝技術，將多個運算核心 (XCD) 與 I/O 晶片 (IOD) 結合，在提高良率的同時提升運算密度。
- **極大化記憶體容量與頻寬**: MI300X 提供高達 192GB 的 HBM3 記憶體與 5.3 TB/s 的頻寬。超大記憶體容量使其在單一節點內即可運行更大規模的模型，減少對多 GPU 切分的依賴。
- **Interconnect**: 採用 Infinity Fabric 技術進行晶片間通訊，提供高效的點對點傳輸。

### 優勢與挑戰
- **優勢**: 硬體規格 (特別是記憶體容量與頻寬) 在同世代產品中極具競爭力；性價比通常優於 NVIDIA。
- **挑戰**: ROCm 軟體生態系統雖然持續進步，但在部分特定模型或最新算子的支援度與穩定性上，仍與 CUDA 有一段差距。

---

## 3. Google TPU 架構 (以 TPU v5e / v5p 為例)

TPU (Tensor Processing Unit) 是 Google 專為機器學習工作負載定制的 ASIC，主要透過 Google Cloud 提供服務。

### 核心架構特點
- **Systolic Array**: TPU 的核心是脈動陣列設計，專門優化大規模密集矩陣乘法，減少暫存器讀寫頻率，極大化運算效率。(可參考 [[基礎計算機結構]])
- **Scale-out Architecture**: 透過專屬的光學互連技術 (OCI) 與環形拓撲 (Torus topology) 連接形成 TPU Pods，實現極佳的線性擴展性。
- **Software Stack**: 深度整合 XLA (Accelerated Linear Algebra) 編譯器與 JAX/PyTorch/TensorFlow 框架，可自動將計算圖優化並映射到硬體。

### 優勢與挑戰
- **優勢**: 對於特定模型 (如 Transformer) 訓練效率極高；在雲端環境中提供絕佳的價格效能比。
- **挑戰**: 需綁定 Google Cloud 環境，不適合地端 (On-premise) 部署；部分非標準或高度動態的計算圖在 TPU 上效率可能不佳。

---

## 方案與選型視角 (Solution Approaches)

在面臨 AI 基礎設施建置時，選擇合適的加速晶片是一項關鍵決策。以下提供三種不同視角的方案分析：

### 方案 A：全面擁抱 NVIDIA 解決方案 (CUDA First)
選擇最新世代的 NVIDIA GPU 叢集 (如 H100/B200) 建置地端資料中心。
- **優點 (Pros)**: 生態系最成熟，開發者上手快；所有最新的開源模型與框架皆會首發支援。
- **缺點 (Cons)**: 供應鏈限制可能導致交期長；硬體建置與維運成本極高。
- **成本 (Costs)**: 初期硬體採購成本最高，且電力與散熱基礎設施成本高昂。
- **維護性 (Maintainability)**: 軟體維護容易，社群資源豐富；硬體散熱維護困難。
- **風險 (Risks)**: 廠商鎖定 (Vendor Lock-in) 嚴重；面臨地緣政治帶來的出口管制風險。

### 方案 B：混合架構與 AMD MI300X 導入 (Cost-Performance Focused)
在地端或混合雲環境中，導入 AMD MI300X 以應對 LLM 推理負載。
- **優點 (Pros)**: 大容量記憶體可有效降低 LLM 推理的硬體切分需求，提升吞吐量；硬體成本較低。
- **缺點 (Cons)**: 需投入人力適應與調優 ROCm 環境；部分非主流算子可能不支援。
- **成本 (Costs)**: 硬體採購成本相對較低，性價比高。
- **維護性 (Maintainability)**: 軟體維護與除錯難度較高，需培養專門的底層優化工程師。
- **風險 (Risks)**: 軟體生態遷移風險，若新模型依賴特定的 CUDA 算子，將面臨開發延遲。

### 方案 C：全雲端託管 TPU 架構 (Cloud-Native & Scale)
放棄地端建置，全面採用 Google Cloud TPU 進行模型訓練與推理。
- **優點 (Pros)**: 零初期硬體建置時間；極佳的橫向擴展能力 (TPU Pods)；網路互連效能高。
- **缺點 (Cons)**: 資料必須上雲，可能有資料隱私與合規性疑慮；無法擁抱其他雲服務或地端資源。
- **成本 (Costs)**: 轉為營運成本 (OpEx)，長期大量使用下，總成本可能超過自建地端硬體。
- **維護性 (Maintainability)**: 硬體維護由雲端服務商負責，維護性極佳；軟體需確保 XLA 編譯順利。
- **風險 (Risks)**: 雲服務商鎖定；若 API 或計費方式大幅改變，將難以迅速應對。
