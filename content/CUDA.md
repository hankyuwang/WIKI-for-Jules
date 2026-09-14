---
title: CUDA
level: intermediate
tags:
  - AI
  - CUDA
---

# CUDA

摘要：CUDA 是 NVIDIA 推出的平行運算平台與編程模型，允許開發者利用 GPU 進行通用計算 (GPGPU)。透過 CUDA，我們能徹底解放顯示卡的平行運算能力，用於加速深度學習模型。

## Prerequisites (先備知識)
- [[GPU架構與發展]]：理解 GPU 為什麼適合平行運算。
- [[SIMT]]：單指令多執行緒，這是 GPU 平行處理的核心概念。

## 核心架構解析
要理解 CUDA 如何運作，可以想像我們有一個超級工廠，裡面有成千上萬的工人。

1. **執行緒架構 (Thread Hierarchy)**：
   - **Thread (執行緒)**：最基本的工人，負責執行單一的指令。
   - **Block (區塊)**：一組工人的小隊。小隊內的工人可以互相溝通、共享資源（就像在同一個辦公室）。
   - **Grid (網格)**：整個工廠的所有小隊總和。
   這種分層結構讓硬體排程器能有效率地將任務分派給 GPU 的各個核心 (Streaming Multiprocessors, SM) 執行。

2. **記憶體階層 (Memory Architecture)**：
   - **Global Memory (全局記憶體)**：工廠的大型倉庫。容量最大（例如 80GB HBM），但存取速度最慢。
   - **Shared Memory (共享記憶體)**：小隊 (Block) 辦公室裡的白板。容量很小（通常幾十 KB），但速度極快，同一個 Block 內的 Thread 可以共同讀寫這塊記憶體。
   - **Local Memory / Registers (暫存器)**：工人自己手上的筆記本。速度最快，但只屬於該工人自己。

## 效能影響分析與最佳實務
在開發 CUDA 程式碼 (稱為 Kernel) 時，最大的挑戰在於「記憶體存取最佳化」。例如：
- **Memory Coalescing (記憶體合併存取)**：確保相鄰的 Thread 存取相鄰的 Global Memory，這樣就能一次把資料搬完，大幅提升頻寬利用率。
- **減少分支 (Warp Divergence)**：GPU 是以 32 個 Thread (稱為一個 Warp) 為單位一起執行相同的指令。如果同一個 Warp 內的工人遇到 `if-else` 分支而要走不同路線，GPU 必須分別執行兩條路線，導致效能折半。

**實務建議**：對於絕大多數 AI 開發者，應盡量呼叫高度優化的底層原語（如 cuDNN、cuBLAS），除非遇到了特殊的算子融合 (Operator Fusion) 需求，才考慮手寫 CUDA Kernel，或使用高階編譯器（如 OpenAI [[Triton]]）來降低開發門檻。
