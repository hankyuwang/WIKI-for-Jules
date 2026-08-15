---
title: 主流 AI 加速晶片架構分析
level: advanced
tags:
  - npu
  - hardware
  - architecture
  - accelerator
---

# 主流 AI 加速晶片架構分析

本文件分析目前市面上知名大廠的 AI 加速晶片，涵蓋它們的應用情境、硬體架構及與市場定位的關聯。

## Prerequisites
- [[NPU架構探索]]
- [[基礎計算機結構]]

## 面向的應用情境

大廠的 AI 晶片通常根據應用情境分為三大類：
1. **Cloud Model Training (雲端模型訓練)**: 需要龐大的運算力與記憶體頻寬，以及強大的晶片互連能力 (Scale-out)。代表晶片：Nvidia H100 / B200 (Blackwell 架構), Google TPU v5p / Trillium, AMD MI300X。
2. **Cloud Model Inference (雲端模型推論)**: 追求高吞吐量、低延遲與高性價比。代表晶片：Groq LPU, AWS Inferentia, Nvidia L40S, Google TPU v5e / Trillium。
3. **Edge Inference (邊緣推論)**: 追求極致的功耗效能比 (TOPS/W)，通常用於手機、PC 或 IoT 裝置。代表晶片：Apple Neural Engine (ANE), Qualcomm Hexagon NPU, Intel NPU。

## 內部硬體架構分析

### 1. ISA 介面定義與分類
- **CISC/RISC-like (如 Nvidia GPU, AMD GPU)**: 提供通用且高度彈性的指令集，如 SIMT (Single Instruction, Multiple Threads) 架構，可應對各種複雜的算子 (Operators) 與控制流。優點是通用性極高，缺點是指令解碼與排程的硬體開銷較大。
- **VLIW / Domain-Specific ISA (如 Google TPU, 某些 NPU)**: 指令長度較長，編譯器在軟體層面負責指令級平行 (ILP) 的排程。硬體不需複雜的亂序執行 (Out-of-Order) 與動態排程，可將更多電晶體用於運算單元 (ALU/MAC)。
- **Dataflow / Spatial (如 Groq LPU)**: 沒有傳統的指令提取，資料流動路徑由編譯器靜態排程，資料直接從 SRAM 流向 ALU，幾乎無額外指令控制負擔，達到極致的低延遲。

### 2. Memory 架構 & Size
- **Training 晶片**: 普遍採用 HBM (High Bandwidth Memory)，如 H100 具備 80GB HBM3 (新一代如 H200/B200 採用更高速的 HBM3e)，頻寬達 3TB/s。AMD MI300X 甚至達到 192GB HBM3 (部分採用 HBM3e)。大容量與高頻寬對於儲存巨大模型的權重 (Weights) 與活化值 (Activations) 至關重要。
- **Edge 晶片**: 通常與 CPU 共用 LPDDR (如 Apple Unified Memory 架構)，記憶體頻寬受限，因此需要依賴高效率的 SRAM 與壓縮技術。

### 3. Cache & SRAM 架構 & Size
- **SRAM 扮演關鍵角色**: SRAM 頻寬遠大於 DRAM。例如 Nvidia H100 的 L2 Cache 約為 50MB。Groq LPU 則採用了激進的設計，捨棄 HBM，全晶片配備約 230MB 的超大 SRAM，確保所有權重都在 SRAM 內，達成極低的推論延遲。
- **Scratchpad Memory (SPM)**: 許多 NPU (如 TPU) 採用由軟體顯式控制的 Scratchpad Memory 取代傳統硬體管理的 Cache，這讓編譯器可以完全掌握資料在晶片內的流動時間，實現 Zero-overhead 搬運。

### 4. 運算能力 & 架構
- **Matrix Multiply Unit / Tensor Core**: 核心架構通常是巨大的脈動陣列 (Systolic Array)。Nvidia H100 的 Tensor Core 支援 FP8, BF16, FP16，透過混合精度計算極大化 FLOPS。
- **Vector Unit**: 用於處理非線性函數 (如 Softmax, GeLU, LayerNorm)。
- **Sparcity 加速**: 近期晶片如 H100 支援 2:4 結構化稀疏 (Structured Sparsity)，可以在不犧牲太多精度的情況下讓運算力翻倍。

### 5. DMA (Direct Memory Access) 能力 & 架構
- **非同步資料搬運**: DMA 負責將資料從 DRAM 搬運到 SRAM (或不同節點之間)。高效的 NPU 會利用 DMA 配合 Double Buffering 或 Ping-Pong Buffering 技術，使得運算與資料搬運能同時進行，隱藏記憶體延遲。

## 硬體架構與應用情境的關聯、優劣與目標市場

- **Nvidia GPU (如 H100)**:
  - *優勢*: 算力強、HBM 頻寬高、CUDA 生態系無可匹敵、極度通用。
  - *劣勢*: 功耗極高 (700W+)，價格昂貴。
  - *目標市場*: 雲端大規模 AI 訓練與推論的霸主。
- **Google TPU**:
  - *優勢*: 為矩陣運算深度優化的架構 (Systolic Array + SPM)，透過光互連 (Optical Interconnect) 組建的 Pod 規模巨大，極度適合訓練巨型模型。
  - *劣勢*: 通用性不如 GPU，綁定 Google Cloud 與 XLA 生態。
  - *目標市場*: 自家雲端 AI 服務與大型企業客製化訓練需求。
- **Groq LPU (Language Processing Unit)**:
  - *優勢*: 超大 SRAM + Deterministic Dataflow 架構，推論延遲極低。
  - *劣勢*: 晶片容量小 (230MB SRAM)，無法單顆跑完大模型，需大量晶片互連，成本不見得低於 GPU。
  - *目標市場*: 對延遲極度敏感的實時 LLM 推論應用。
- **Apple Silicon (ANE)**:
  - *優勢*: 與 CPU/GPU 共用 Unified Memory，TOPS/W 極高，無縫整合 Core ML 生態。
  - *劣勢*: 運算力不足以進行大規模訓練。
  - *目標市場*: 消費級終端裝置 (Edge AI)。

---
*相關閱讀*：
- [[AI模型分類與硬體協同設計]]
- [[AI加速晶片軟體堆疊與SDK設計]]
- [[自研AI晶片策略與前沿挑戰]]
