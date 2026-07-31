---
title: AI晶片軟體堆疊與SDK設計
level: advanced
tags:
  - software-stack
  - sdk
  - compiler
  - cuda
---

# AI晶片軟體堆疊與SDK設計

硬體的成功往往取決於其軟體生態系的完備程度。AI 加速晶片的軟體堆疊決定了開發者能否輕易地將上層的框架（如 PyTorch、TensorFlow）映射到下層的硬體上。

## 1. 手寫 Kernel 生態：CUDA
- **代表硬體**：NVIDIA GPUs
- **設計理念**：提供一套類似 C/C++ 的程式語言擴充，讓開發者能夠直接控制硬體的執行緒架構 (Thread Blocks, Warps)、記憶體階層 (Shared Memory) 等細節。
- **優勢**：
  - 極限效能優化：開發者可以針對特定硬體微調 Kernel，榨乾最後一滴效能（如 FlashAttention）。
  - 生態系龐大：經過十幾年的累積，擁有最豐富的函式庫 (cuBLAS, cuDNN)。
- **劣勢**：學習曲線陡峭，開發與維護成本高。硬體一旦發生重大架構改變，手寫 Kernel 可能需要重寫。

## 2. 基於編譯器的堆疊：XLA / MLIR
- **代表硬體**：Google TPU (XLA), 眾多新創 AI 晶片 (基於 MLIR)
- **設計理念**：將硬體抽象化，不依賴手寫 Kernel，而是將高階圖 (Graph) 透過編譯器自動優化並轉換為硬體指令。
- **XLA (Accelerated Linear Algebra)**：
  - Google 為 TPU 開發，擅長做 Graph-level 的優化（如 Operator Fusion），減少記憶體存取。
- **MLIR (Multi-Level Intermediate Representation)**：
  - LLVM 專案的一環。它提供了一種通用的中介碼表示方法，讓編譯器可以分層進行優化（從圖層級、迴圈層級到硬體指令層級）。
  - 對於新硬體來說，只需要實作 MLIR 的後端 (Backend)，就能接入上層的 AI 框架，大幅降低軟體開發門檻。

## 3. 開放生態與中介層：Triton / ROCm
- **Triton (OpenAI)**：
  - 介於 CUDA 和高階編譯器之間。它隱藏了 CUDA 複雜的執行緒與 Shared Memory 管理，讓使用者用 Python 就能寫出效能媲美手寫 CUDA 的 Kernel。
  - 對於打破 CUDA 壟斷具有重要意義，因為 Triton 也能編譯到非 NVIDIA 的硬體上。
- **ROCm (AMD)**：
  - AMD 的開放軟體堆疊，試圖提供一個相容/轉換 CUDA 的環境 (HIP)。
  - 目前正積極整合 Triton 與 MLIR，以縮小與 CUDA 在生態上的差距。
