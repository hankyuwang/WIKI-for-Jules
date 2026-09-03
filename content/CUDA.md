---
title: CUDA
level: intermediate
tags:
  - AI
  - CUDA
---

# CUDA

摘要：CUDA (Compute Unified Device Architecture) 是 NVIDIA 推出的平行運算平台與編程模型，允許開發者利用 GPU 進行通用計算 (GPGPU)。這是目前 AI 領域最底層且最重要的運算基礎之一。

## Prerequisites (先備知識)
- [[GPU架構與AI計算]] : 了解 GPU 在 AI 中為何如此重要。
- [[SIMT]] : 了解單指令多執行緒的基本運作原理。

## 核心概念與原理
CUDA 的核心在於將龐大的運算任務平行化。採用 **[[SIMT]] (單指令多執行緒)** 架構。
- **Thread (執行緒)**：最基本的執行單元。
- **Block (區塊)**：由多個 Thread 組成，同一個 Block 內的 Thread 可以透過共享記憶體互相通訊與同步。
- **Grid (網格)**：由多個 Block 組成，代表整個運算任務。

當開發者撰寫 CUDA Kernel (核心程式) 時，硬體排程器會將 Block 分派給 GPU 內部的 **Streaming Multiprocessors (SM)** 執行。

## 開發挑戰與限制
CUDA 提供了基於 C/C++ 的擴充語法，讓開發者能直接管理 GPU 的記憶體階層。然而：
1. **硬體綁定**：高度綁定 NVIDIA 硬體生態，跨平台 (如移植到 AMD 或 Intel GPU) 極其困難。
2. **開發門檻高**：開發者需具備深厚的計算機結構知識，才能處理記憶體對齊、Bank Conflict 等底層問題。

## 最佳實務與生態發展
深度學習的底層原語（如 cuDNN、cuBLAS）皆由 CUDA 高度優化實作。應用層開發者（如使用 PyTorch 的開發者）通常無需從頭撰寫 Kernel。

隨著模型規模擴大，如何透過高階編譯器抽象技術（如 [[Triton]] 或 [[TVM]]）自動產生媲美手寫 CUDA 的核心程式碼，以降低開發門檻並突破單一供應商鎖定，是當前熱門的研究方向。
