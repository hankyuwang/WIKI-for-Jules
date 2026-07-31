---
title: 主流AI加速晶片架構與應用
level: intermediate
tags:
  - ai-accelerator
  - architecture
  - nvidia
  - tpu
  - amd
  - groq
---

# 主流AI加速晶片架構與應用

在當前AI算力需求爆炸的時代，不同硬體廠商推出了各種架構的加速晶片來應對龐大的計算與記憶體需求。本篇整理了市場上主流廠商的架構特色。

## NVIDIA (Hopper / Blackwell 架構)
- **架構特點**：以 GPU 核心為基礎，高度並行化。Blackwell 帶來了更強的 FP4 支援與第二代 Transformer Engine。
- **ISA / 運算單元**：擁有大量 CUDA Cores 及專門針對矩陣運算的 Tensor Cores。
- **Memory / SRAM / Cache**：配備極高頻寬的 HBM (如 HBM3/HBM3e)，並有巨大的 L2 Cache 來減少對 HBM 的存取頻率。
- **DMA / 互連**：NVLink 與 NVSwitch 提供晶片間、節點間的極高頻寬，是其在資料中心霸權的關鍵。
- **目標市場**：雲端訓練、大型推論 (LLM, Foundation Models)，擁有最完整的軟體生態 (CUDA)。

## Google (TPU - Tensor Processing Unit)
- **架構特點**：專為深度學習設計的 [[Systolic Array]]（脈動陣列）架構。
- **ISA / 運算單元**：以矩陣乘法單元 (MXU) 為核心，VLIW (Very Long Instruction Word) 指令集架構，簡化了控制邏輯。
- **Memory / SRAM / Cache**：高頻寬 HBM，以及大量的晶片上 SRAM 作為軟體可控的 Scratchpad Memory。
- **DMA / 互連**：TPU 透過專用的 Inter-Core Interconnect (ICI) 構建 3D Torus 網路，非常適合大規模同步訓練。
- **目標市場**：Google 內部的大規模模型訓練與推論（如 Gemini），提供雲端服務。

## AMD (MI300 系列)
- **架構特點**：Chiplet（小晶片）設計，將 CPU (Zen) 與 GPU (CDNA) 封裝在一起 (MI300A) 或純 GPU (MI300X)。
- **ISA / 運算單元**：CDNA 架構，專注於矩陣/向量運算。
- **Memory / SRAM / Cache**：統一記憶體架構（在 APU 設計中 CPU 和 GPU 共享 HBM3），極大降低資料搬移成本。
- **目標市場**：高效能運算 (HPC)、資料中心AI加速，力圖在軟體端（ROCm）挑戰 NVIDIA 的主導地位。

## Groq (LPU - Language Processing Unit)
- **架構特點**：SRAM-centric 架構。移除了複雜的快取、分支預測等硬體邏輯，將控制權完全交給編譯器。
- **ISA / 運算單元**：TSP (Tensor Streaming Processor)，時間確定性（Deterministic）執行。
- **Memory / SRAM / Cache**：無 HBM，全依賴晶片上巨大的 SRAM，提供超低延遲與極高頻寬。
- **目標市場**：LLM 的極速推論（Batch Size = 1 時的延遲極限），不適合需要巨大記憶體容量的訓練任務。

## Apple (ANE - Apple Neural Engine)
- **架構特點**：高度優化的邊緣裝置加速器。
- **ISA / 運算單元**：專精於低功耗的矩陣與卷積運算，支援 [[模型量化技術|INT8 / FP16 等混合精度]]。
- **Memory / SRAM / Cache**：與 CPU、GPU 共享統一部件記憶體 (Unified Memory Architecture)。
- **目標市場**：終端/邊緣裝置（iPhone, Mac）的 AI 推論，注重功耗與能效比 (Performance per Watt)。
