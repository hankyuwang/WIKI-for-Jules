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

## Prerequisites (先備知識)
- [[GPU架構與發展]]：理解 GPU 硬體的限制。
- [[CUDA]]：了解傳統 GPU 開發的門檻與挑戰。

## 為什麼我們需要 Triton？
傳統上，要充分發揮 GPU 的極致效能，工程師必須使用 [[CUDA]] C++ 來撰寫底層 Kernel。這就像是在沒有現代化工具的環境下手刻極為精密的機械：你需要深刻理解硬體架構，精準控制 Shared Memory 的分配、Warp 的排程、以及 Memory coalescing (記憶體合併存取)。學習曲線極其陡峭，開發成本極高。

Triton 提供了一套基於 Python 的高階語法，隱藏了許多繁瑣的底層細節，讓 AI 研究員能專注於「演算法本身」，而非「硬體細節」。

## 核心原理解析：Block-level Operations
在 CUDA 中，開發者必須定義每個「單一執行緒 (Thread)」要做什麼事，這非常容易出錯。

Triton 的創新在於：**開發者只需定義「Block (區塊)」層級的操作**。
這意味著你寫的程式碼是針對一小塊記憶體矩陣（例如 $64 \times 64$ 的區塊）進行操作。Triton 的編譯器會在背後自動幫你處理：
1. 將這個 Block 拆解並分配給底層的 Warp 和 Thread。
2. 自動管理 Shared Memory 的分配與同步。
3. 最佳化記憶體的存取模式以最大化頻寬。

## 開發成本與效能對比
- **手寫 CUDA**：可能需要數百行 C++ 程式碼，耗時數週進行除錯與效能調校。效能極限最高，但僅限少數硬體專家。
- **使用 Triton**：只需數十行 Python 程式碼，幾天內即可完成開發。在多數常見場景下（如 FlashAttention），能達到手寫 CUDA 80%~95% 以上的效能，大幅縮短了從理論到部署的距離。
