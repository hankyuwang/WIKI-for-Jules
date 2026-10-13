---
title: CUDA
level: intermediate
tags:
  - software
  - framework
  - nvidia
---
# CUDA (Compute Unified Device Architecture)

> CUDA 是由 NVIDIA 所推出的平行運算平台與應用程式設計介面 (API)。它允許軟體開發者利用 NVIDIA GPU 的強大運算能力來解決複雜的運算問題。

## 初學者導覽：指揮千軍萬馬的專屬語言
如果把 GPU 想像成一個擁有成千上萬名工人的超級工廠（用來做大量的平行運算），那麼 **CUDA 就是能夠同時指揮這些工人的專屬語言和擴音器**。

在 CUDA 出現之前，如果你想讓 GPU 幫你算數學，你必須把數學問題「偽裝」成畫圖的指令（因為 GPU 原本是處理圖形的）。這不僅痛苦而且效率低。
NVIDIA 推出 CUDA 後，開發者可以直接用類似 C/C++ 的語言寫程式，明確告訴 GPU：「第一排的工人處理 A 資料，第二排處理 B 資料」。這徹底釋放了 GPU 在科學運算與人工智慧領域的潛力。

## 為什麼 CUDA 如此重要？（護城河效應）
今天 NVIDIA 能夠在 AI 晶片市場佔據統治地位，硬體強大只是其中一個原因，更重要的是 **CUDA 建立的軟體生態系**。
十多年來，全球的研究人員都在使用 CUDA 開發演算法。所有主流的深度學習框架（如 [[PyTorch]]、[[TensorFlow]]）底層都深度依賴 CUDA 及相關函式庫（如 [[cuDNN]]）。
這形成了一道巨大的護城河：即使其他公司的硬體規格超越了 NVIDIA，但因為開發者已經習慣了 CUDA 生態系，要遷移到其他平台（如 AMD 的 [[ROCm]]）的成本非常巨大。

## 核心概念
- **Kernel**：在 GPU 上平行執行的函數。當你呼叫一個 Kernel 時，它會被成千上萬個執行緒同時執行。
- **Thread Hierarchy (執行緒階層)**：CUDA 將工作劃分為 Grid、Block 和 Thread。這讓程式能夠靈活適應不同規模的 GPU 硬體。
- **Shared Memory**：這是一種非常快速的晶片內暫存區，同一 Block 的執行緒可以透過它來共享資料，大幅減少存取慢速主記憶體的時間。

## 延伸閱讀
- 了解硬體的實際執行方式：[[SIMT]]
- 了解 AMD 推出的對手平台：[[ROCm]]
- 若想了解更底層的實作分析：[[CUDA逆向工程與算子實作分析]]
