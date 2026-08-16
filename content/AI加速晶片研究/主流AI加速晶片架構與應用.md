---
title: 主流 AI 加速晶片架構與應用
level: intermediate
tags:
  - ai-chip
  - hardware-architecture
  - nvidia
  - google-tpu
  - amd
---

# 主流 AI 加速晶片架構與應用

本篇深入探討市面上知名大廠 (NVIDIA, Google, AMD, Groq, Intel, Apple 等) 的 AI 加速晶片架構。我們將從應用情境出發，剖析其內部硬體架構，並分析這些設計帶來的優勢與目標市場。

## 前置知識
- [[基礎計算機結構]]
- [[NPU架構探索]]
- 了解基本的記憶體階層 (Memory Hierarchy) 與 DMA (Direct Memory Access) 概念。

## 1. NVIDIA H100 / B200 (Hopper / Blackwell 架構)
NVIDIA 無疑是目前 AI 晶片的霸主，其 GPU 架構針對通用性與高效能進行了極致優化。

*   **應用情境**: 雲端運算 (Cloud)、超大規模 Model Training & Inference (特別是 LLM)。
*   **硬體架構重點**:
    *   **ISA 介面**: PTX (Parallel Thread Execution) 虛擬指令集，再由驅動編譯為硬體特定指令 (SASS)。屬於 SIMT (Single Instruction, Multiple Threads) 架構。
    *   **Memory 架構**: 高頻寬記憶體 (HBM3 / HBM3e)。例如 H100 具備高達 80GB/96GB HBM3，頻寬達 3TB/s 以上。B200 則進一步提升。
    *   **SRAM / Cache**: 龐大的 L2 Cache (H100 達 50MB)，各個 Streaming Multiprocessor (SM) 內有 Shared Memory (可視為 L1/SRAM，可由軟體控制)，容量約為數百 KB。
    *   **運算能力 (TOPS/TFLOPS)**: 具備第四代 Tensor Core。H100 在 FP8 下可達約 4,000 TFLOPS (Sparse)。
    *   **DMA 架構**: 具備非同步複製 (Asynchronous Copy) 和 TMA (Tensor Memory Accelerator)，允許資料直接從 Global Memory (HBM) 搬運到 Shared Memory，大幅減輕暫存器和執行單元的負擔。
*   **優勢/劣勢/目標市場**:
    *   **優勢**: 生態系極為強大 (CUDA)，支援幾乎所有模型與算子。硬體運算與頻寬極高。TMA 解決了 memory-bound 問題。
    *   **劣勢**: 價格昂貴，功耗極高 (700W+)，非專為單一模型設計，存在一定的矽面積浪費 (相對於純 ASIC)。
    *   **市場**: 資料中心、大型 AI 實驗室。

## 2. Google TPU (v4 / v5e / v5p / TPU v6 (Trillium))
Google 的 TPU 是針對神經網路高度最佳化的 ASIC，特別強調整體叢集 (Cluster) 的效能。

*   **應用情境**: 雲端運算 (Cloud)，主要為 Google 內部與 GCP 客戶的 Model Training & Inference。
*   **硬體架構重點**:
    *   **ISA 介面**: VLIW (Very Long Instruction Word) 架構。透過編譯器 (XLA) 將複雜指令打包，減少硬體 Decode 的負擔。
    *   **Memory 架構**: 同樣採用 HBM，叢集間透過專屬光學交換機 (Optical Circuit Switches, OCS) 連結，形成 3D Torus 等拓撲，極大化跨晶片頻寬。
    *   **SRAM / Cache**: 核心運算單元 (Matrix Multiply Unit, MXU) 旁配置大量的 Vector Memory (SRAM)，容量高達數十 MB，直接供應矩陣運算，軟體完全控制 (Scratchpad)。
    *   **運算能力**: MXU 是巨型的 Systolic Array (例如 128x128)。v5p 具備 459 TFLOPS (BF16)。
    *   **DMA 架構**: 高度依賴編譯器排程 (Software Managed)，透過 DMA 引擎在 HBM 與 Vector Memory 之間搬移資料，重疊運算與通訊 (Overlap Compute and Comm)。
*   **優勢/劣勢/目標市場**:
    *   **優勢**: 大規模叢集擴展性極佳 (Scale-out)。相較於 GPU，單位功耗的矩陣運算效能 (TOPS/W) 更高。
    *   **劣勢**: 通用性不如 GPU，高度依賴 XLA 編譯器，若模型包含非標準算子，效能可能驟降。只能在 GCP 上租用，無法買斷。
    *   **市場**: GCP 雲端客戶、Google 自身服務 (Search, Gemini)。

## 3. AMD MI300X (CDNA 3 架構)
AMD 的 MI300X 是 NVIDIA 目前最大的競爭對手，主打超大記憶體容量與頻寬。

*   **應用情境**: 雲端運算 (Cloud)、Model Training & Inference (大模型首選)。
*   **硬體架構重點**:
    *   **ISA 介面**: 類似 NVIDIA 的 SIMT 架構，指令集針對矩陣運算優化。
    *   **Memory 架構**: 這是 MI300X 的最大亮點。搭載高達 192GB 的 HBM3，頻寬達 5.3 TB/s。
    *   **SRAM / Cache**: 採用 Chiplet 設計，配備巨大的 Infinity Cache (類似 L3 Cache) 高達 256MB，降低對 HBM 的存取需求。
    *   **運算能力**: Matrix Core 提供強大的 FP8 / BF16 算力，帳面規格(TFLOPS)可與 H100 匹敵甚至超越。
    *   **DMA 架構**: 透過 Infinity Fabric 進行晶片內與晶片間的高速資料傳輸。
*   **優勢/劣勢/目標市場**:
    *   **優勢**: 超大 HBM 容量。對於 LLM Inference (經常受限於記憶體頻寬與容量，即 Memory-bound) 來說，單卡可以塞下更大的模型 (或更大的 Batch Size)，性價比極高。
    *   **劣勢**: 軟體生態系 (ROCm) 起步較晚，雖然進步神速，但在算子支援度和穩定性上與 CUDA 仍有一點差距。
    *   **市場**: 資料中心、尋求 NVIDIA 替代方案的雲端服務商 (如 Microsoft, Meta)。

## 4. Groq (LPU - Language Processing Unit)
Groq 採用了非常激進的架構設計，放棄了傳統的 Cache/HBM 架構，完全追求極致的低延遲。

*   **應用情境**: 雲端 (Cloud) LLM Inference (極致要求低延遲 Generation)。
*   **硬體架構重點**:
    *   **ISA 介面**: TSP (Tensor Streaming Processor) 架構，硬體非常簡單，沒有分支預測器，沒有硬體排程。指令執行完全確定性 (Deterministic)，由編譯器決定每個時脈週期 (Cycle) 的資料流向。
    *   **Memory 架構**: **沒有 HBM**。晶片上全是 SRAM！
    *   **SRAM / Cache**: 單晶片配置約 230MB 的超高速 SRAM。SRAM 頻寬高達 80 TB/s (遠超任何 HBM)。
    *   **運算能力**: 大量分散的 ALU / MAC 單元與 SRAM 交錯佈局。
    *   **DMA 架構**: 網路即 DMA。晶片間透過自有的 Real-time 網路互連，因為一切都是 deterministic 的，資料在預定的 cycle 就會送達隔壁晶片。
*   **優勢/劣勢/目標市場**:
    *   **優勢**: **極低的延遲 (Ultra-low Latency)**。由於模型權重全部塞在 SRAM 裡，生成 Token 的速度極快 (可達數百 tokens/sec/user)。
    *   **劣勢**: 為了放下大模型 (如 Llama-3.1-70B)，需要將模型切分到數十甚至數百張 Groq 卡的 SRAM 中。雖然單卡便宜，但系統層級的成本與機架空間 (Rack Space) 耗費驚人。不適合 Training。
    *   **市場**: 對即時對話、延遲極度敏感的 AI 應用。

## 5. Apple A-Series / M-Series (Apple Neural Engine, ANE)
Apple 的 ANE 是 Edge 端 AI 加速器的典範。

*   **應用情境**: 邊緣端 (Edge) / 裝置端 (On-device) Inference (如 FaceID, 語音辨識, 照片分類)。
*   **硬體架構重點**:
    *   **ISA 介面**: 專用指令集 (封閉系統)，高度依賴 Core ML 框架編譯。
    *   **Memory 架構**: UMA (Unified Memory Architecture)。CPU, GPU, NPU 共享同一塊 LPDDR，避免了資料在不同處理器間複製的 overhead。
    *   **SRAM / Cache**: 晶片內有大容量的 System Cache (SLC)，ANE 可以直接存取 SLC，減少對 DRAM 的依賴。內部也有數 MB 的 SRAM 作為 Activation buffer。
    *   **運算能力**: 數十 TOPS (例如 M3 具備 18 TOPS，M4 達到 38 TOPS)，足以應付終端模型。
    *   **DMA 架構**: 與 SoC 深度整合，透過內部 Fabric 直接 DMA。
*   **優勢/劣勢/目標市場**:
    *   **優勢**: **能效比 (Performance/Watt) 極高**。與作業系統深度整合，Zero-copy memory access 大幅降低功耗。
    *   **劣勢**: 算力與記憶體頻寬無法與雲端晶片相比。開發者無法直接撰寫低階程式碼優化，只能透過 Core ML。
    *   **市場**: 消費性電子產品、PC/手機。

## 總結：架構與應用情境的關聯
1.  **Cloud Training**: 需要龐大算力、大記憶體容量與高頻寬 (HBM)，且需要極高的通用性以應付不斷演進的模型。**GPU 依然是首選**，TPU 也是強大替代品。
2.  **Cloud Inference (Throughput-oriented)**: 需要大記憶體容量放模型，高頻寬提升 Batch Size。**MI300X 等大 HBM 晶片優勢明顯**。
3.  **Cloud Inference (Latency-oriented)**: 要求單筆 Request 的反應時間極快，**Groq (SRAM-based) 架構**提供了解決方案，但系統成本高。
4.  **Edge / On-Device**: 功耗 (Power) 是絕對限制。需要高能效的 ASIC / NPU，結合統一記憶體架構 (UMA) 減少資料搬運。**Apple ANE, Qualcomm NPU** 是主流。
