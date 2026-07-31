---
title: SDK與軟體堆疊
level: advanced
tags:
  - software-stack
  - sdk
  - cuda
  - xla
  - triton
  - compiler
---

# SDK與軟體堆疊

強大的 AI 晶片需要同樣強大的軟體生態系來釋放其效能。本文件探討當前主流的 AI 軟體堆疊與編譯器技術。

## CUDA (Compute Unified Device Architecture)
CUDA 是 NVIDIA 建立的平行運算平台與編程模型，也是目前 AI 領域最成熟、生態系最龐大的軟體堆疊。幾乎所有主流深度學習框架（PyTorch, TensorFlow）都原生支援 CUDA，其豐富的函式庫 (cuBLAS, cuDNN) 提供了極致的最佳化效能。

## XLA (Accelerated Linear Algebra) 與 MLIR
XLA 是 Google 開發的機器學習編譯器，最初用於最佳化 TensorFlow 在 TPU 上的執行效能，目前也廣泛支援 PyTorch (透過 PyTorch/XLA) 與 JAX。
MLIR (Multi-Level Intermediate Representation) 則是一個編譯器基礎架構，旨在統一不同層級的抽象表示，讓編譯器開發者能更輕易地為各種新興 AI 加速器建構高效的後端。

## Triton
OpenAI 開發的 Triton 是一個為神經網路撰寫高效能客製化 GPU 程式碼的開源語言與編譯器。它抽象化了複雜的 GPU 記憶體階層與同步機制，讓研究人員與工程師能以接近 Python 的語法，寫出效能媲美手刻 CUDA C++ 的 kernel 程式碼，大幅降低了硬體最佳化的門檻。
