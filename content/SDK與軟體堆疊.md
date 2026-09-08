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

## Prerequisites
- [[GPU在AI加速的應用]]
- [[深度學習運算原理]]

強大的 AI 晶片需要同樣強大的軟體生態系來釋放其效能。本文件探討當前主流的 AI 軟體堆疊與編譯器技術。


## 虛擬團隊補充說明：軟體堆疊的必要性

> **教育員白話文解釋**：想像一下，AI 硬體晶片（如 GPU/TPU）就像是一台擁有上千匹馬力的超級跑車引擎。但是，如果你（AI 開發者）只會開一般的自排車（Python 語法），你要怎麼控制這台怪物？
>
> 這時候就需要「軟體堆疊（Software Stack）」來當作翻譯和橋樑。它像是一個極其聰明的變速箱和自動駕駛系統，把你寫的 Python 程式碼，自動翻譯、拆解並最佳化成千上萬個指令，精準地分發給引擎裡的每一個汽缸（運算核心）去執行。沒有這些強大的軟體（如 CUDA、編譯器），再強的硬體也只是一塊發熱的石頭。

## CUDA (Compute Unified Device Architecture)
CUDA 是 NVIDIA 建立的平行運算平台與編程模型，也是目前 AI 領域最成熟、生態系最龐大的軟體堆疊。幾乎所有主流深度學習框架（PyTorch, TensorFlow）都原生支援 CUDA，其豐富的函式庫 (cuBLAS, cuDNN) 提供了極致的最佳化效能。

## XLA (Accelerated Linear Algebra) 與 MLIR
XLA 是 Google 開發的機器學習編譯器，最初用於最佳化 TensorFlow 在 TPU 上的執行效能，目前也廣泛支援 PyTorch (透過 PyTorch/XLA) 與 JAX。
MLIR (Multi-Level Intermediate Representation) 則是一個編譯器基礎架構，旨在統一不同層級的抽象表示，讓編譯器開發者能更輕易地為各種新興 AI 加速器建構高效的後端。

## Triton
OpenAI 開發的 Triton 是一個為神經網路撰寫高效能客製化 GPU 程式碼的開源語言與編譯器。它抽象化了複雜的 GPU 記憶體階層與同步機制，讓研究人員與工程師能以接近 Python 的語法，寫出效能媲美手刻 CUDA C++ 的 kernel 程式碼，大幅降低了硬體最佳化的門檻。
