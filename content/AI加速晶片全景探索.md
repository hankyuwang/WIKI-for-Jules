---
title: AI 加速晶片全景探索
level: advanced
tags:
  - ai-chips
  - hardware
  - npu
  - acceleration
---

# AI 加速晶片全景探索

本報告對當前 AI 加速晶片的發展格局進行深入分析，涵蓋從雲端到邊緣端的主要硬體架構，並探討其應用場景、硬體特性、SDK 生態與新創公司的應對策略。

## Prerequisites
- [[NPU架構探索]]
- [[基礎計算機結構]]

## 1. 雲端巨頭與極致算力 (Cloud & High-Performance Computing)

### 1.1 NVIDIA H100 (Hopper 架構)
- **使用場景**：大規模語言模型 (LLM) 訓練與推理、高效能運算 (HPC)、資料中心。
- **硬體特性**：
  - 第四代 Tensor Core，支援 FP8 和 FP64。
  - 引入 Transformer Engine，針對 Transformer 架構的網路進行加速。
  - HBM3 記憶體帶來極高的記憶體頻寬 (超過 3 TB/s)。
  - NVLink 第四代，支援多 GPU 之間的高速通訊。
- **關聯模型**：GPT-4, Llama 3, Claude 3 (千億到萬億參數等級)。
- **SDK 生態**：CUDA, cuDNN, TensorRT。CUDA 生態系極為成熟，幾乎是業界標準。

### 1.2 Google TPU v5p
- **使用場景**：Google Cloud 平台上的大規模模型訓練與推理。
- **硬體特性**：
  - 針對矩陣運算高度優化的 Systolic Array (脈動陣列) 架構。
  - 高度可擴展的 Pod 架構，透過光纖互連 (Optical Circuit Switches) 組成超級電腦。
  - 專注於高性價比和能源效率 (Performance per Watt)。
- **關聯模型**：Gemini, PaLM 2。
- **SDK 生態**：XLA (Accelerated Linear Algebra), JAX, TensorFlow, PyTorch (透過 XLA 編譯)。

## 2. 邊緣與終端裝置 (Edge & On-Device)

### 2.1 Apple ANE (Apple Neural Engine)
- **使用場景**：iPhone, iPad, Mac 上的端側 AI 應用 (如 FaceID, 圖像處理, Core ML 應用)。
- **硬體特性**：
  - 整合於 Apple Silicon (M 系列, A 系列) SoC 中，與 CPU/GPU 共享統一記憶體 (Unified Memory)。
  - 專注於低功耗推論 (Inference)，支援 FP16 和 INT8。
- **關聯模型**：終端側的小型模型 (如 MobileNet, Whisper-tiny, 以及 Apple 自家的端側語言模型)。
- **SDK 生態**：Core ML。開發者可透過 Core ML 將 PyTorch/TensorFlow 模型轉換並在 ANE 上執行。
- **邊緣挑戰**：記憶體容量受限於系統記憶體，且 ANE 不開放底層編程介面，開發者只能依賴 Core ML 的高階 API。

## 3. 新興架構與顛覆者

### 3.1 Groq LPU (Language Processing Unit)
- **使用場景**：超低延遲的大語言模型 (LLM) 推理。
- **硬體特性**：
  - 確定性架構 (Deterministic Architecture)，沒有快取 (Cache) 或複雜的分支預測，編譯器在編譯階段就排程好所有的指令與資料流。
  - 採用大量超高速 SRAM，極大化記憶體頻寬，解決 LLM 推理時的 Memory Wall 問題。
- **關聯模型**：Llama 3, Mixtral (專注於百億到千億參數模型的超快速生成)。
- **SDK 生態**：GroqCompiler。將模型轉換為確定性指令流。

## 4. 當前邊緣運算挑戰與新創策略

### 4.1 邊緣端 AI 的挑戰
- **記憶體牆 (Memory Wall)**：邊緣裝置的 DRAM 頻寬和容量通常很小，難以載入大型模型。
- **功耗限制**：終端裝置對散熱和電池續航有嚴格要求，必須在 TOPS/W (每瓦算力) 上取得平衡。
- **軟體碎片化**：不同硬體廠商 (如 Qualcomm, MediaTek, Apple) 有各自的 SDK 和編譯工具，缺乏像 CUDA 這樣的大一統標準。

### 4.2 小型新創公司的策略 (Startup Strategy)
- **避免與 NVIDIA 在雲端訓練市場正面交鋒**：CUDA 的護城河太深。
- **專注於特定垂直領域 (Domain-Specific)**：如專注於極低功耗的 IoT 晶片、或是針對特定網路架構 (如 Transformer 或 Mamba) 的專用 ASIC。
- **軟硬協同與量化技術**：深度結合 [[模型量化技術]] (如 4-bit / 2-bit quantization) 與編譯器優化，在有限資源下達到可接受的精準度。
- **擁抱開放生態**：支援開源編譯器堆疊 (如 MLIR, TVM, IREE)，降低開發者遷移模型的門檻。