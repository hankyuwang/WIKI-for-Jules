---
title: Triton
level: intermediate
tags:
  - AI
  - Triton
  - GPU
---

# OpenAI Triton

摘要：OpenAI Triton 是一個專為 GPU 設計的開源程式語言與編譯器，它大幅簡化了硬體感知 (Hardware-aware) Kernel 的開發難度，讓研究人員能用 Python 寫出媲美手寫 CUDA 的高效能程式碼。

## 設計初衷

傳統上，要充分發揮 GPU (特別是 NVIDIA [[GPU架構與發展]]) 的極致效能，工程師必須使用 [[CUDA]] C++ 來撰寫底層 Kernel。這需要深刻理解硬體架構，如 Shared Memory、Warp scheduling、Memory coalescing 等，學習曲線極其陡峭。

Triton 提供了一套基於 Python 的高階語法，隱藏了部分底層細節。工程師只需定義 **Block** 層級的操作，Triton 編譯器會自動處理 Warp 級別的排程、Shared Memory 的分配與同步。

## 核心優勢

- **降低開發門檻**：以 Python 語法編寫，讓熟悉 PyTorch 的 AI 研究人員能自行開發高度客製化且高效的算子 (如 FlashAttention)。
- **效能優異**：透過內建的編譯器優化 (基於 [[MLIR]])，Triton 產出的機器碼在多數情況下能達到手寫 CUDA Kernel 80% 到 90% 以上的效能，有時甚至更好。
- **跨硬體潛力**：雖然目前主要針對 NVIDIA GPU 優化，但 Triton 的架構設計使其有潛力支援 AMD [[ROCm]] 等其他硬體後端，減少 Vendor Lock-in。

## 應用案例

Triton 在社群中最著名的應用之一是 PyTorch 2.0 中的 `torch.compile` 底層後端，以及被廣泛應用於大型語言模型訓練與推理的 **FlashAttention** 演算法實作。
