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

## Kernel Function 的具體運作方式
在 CUDA 中，**Kernel** 是非常核心的概念。當你在 CPU (Host) 上呼叫一個 Kernel 時，你必須同時指定「執行組態」(Execution Configuration)——也就是告訴 GPU：「我要派多少個 Block，每個 Block 裡面要有幾個 Thread 來做這件事」。
GPU (Device) 接收到指令後，會將這成千上萬個 Thread 映射到實際的硬體運算單元 (Streaming Multiprocessors, SM) 上，以極度平行的方式同時處理海量數據。

## 效能瓶頸：Host to Device 的記憶體傳輸
儘管 GPU 運算極快，但它有自己專屬的記憶體（VRAM）。在計算開始前，必須先透過 [[PCIe]] 匯流排，將資料從電腦的主記憶體 (Host) 複製到 GPU 的記憶體 (Device)。運算結束後，又得搬回去。
這段搬運過程的速度遠遠慢於 GPU 內部的運算速度。因此，CUDA 程式優化的黃金法則之一，就是「盡可能讓資料留在 GPU 內，減少來回傳輸的次數」。

## CUDA, ROCm 與 Triton 的優缺點對比
- **NVIDIA CUDA**：
  - **優點**：絕對的業界標準，生態系統無比龐大且成熟，除錯工具完善。
  - **缺點**：將開發者深深綁死在 NVIDIA 的硬體上（Vendor Lock-in）。
- **AMD [[ROCm]]**：
  - **優點**：為 AMD GPU 打造的開源生態平台，架構上積極兼容 CUDA 的語法以降低轉移成本。
  - **缺點**：軟體成熟度與社群支援度仍遠不及 CUDA，遇到冷門 bug 時較難解決。
- **OpenAI [[Triton]]**：
  - **優點**：一種更高階的開源編程語言，開發者可以用接近 Python 的語法寫出效能媲美手寫 CUDA 的程式碼，且同時支援 NVIDIA 與 AMD 晶片。
  - **缺點**：相對較新，對於極度底層、非標準的特殊運算優化，仍不如直接寫 CUDA 來得精細。
