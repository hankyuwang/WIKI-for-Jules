---
title: SIMT (單指令多執行緒)
level: intermediate
tags:
  - AI
  - SIMT
  - GPU架構
  - 平行運算
---

# SIMT (Single Instruction, Multiple Threads)

摘要：SIMT（單指令多執行緒）是現代 GPU 核心的執行模式，它結合了 SIMD（單指令多資料）的高效能與純量多執行緒的靈活性，是實現大規模平行運算與 AI 加速的基礎。

## Prerequisites
閱讀本篇前，建議先了解以下基礎概念：
- [[基礎計算機結構]]
- [[SIMD]]
- [[GPU運算架構]]

## 技術原理 (Principle)
在傳統的 CPU SIMD (Single Instruction, Multiple Data) 架構中，一條指令會強制操作一個固定長度的向量資料（例如同時計算 4 個浮點數）。但如果這 4 個資料的邏輯分支不同（例如 if-else 條件判斷），SIMD 處理起來就會非常笨拙。
NVIDIA 在其 GPU 架構中引入了 SIMT 模型。在 SIMT 中，程式設計師撰寫的是針對單一執行緒（Thread）的程式碼，而硬體會將數十個執行緒（例如 NVIDIA 的 Warp 為 32 個執行緒，AMD 的 Wavefront 為 64 個）綑綁在一起執行。
- **Single Instruction:** 硬體調度器一次發射一條指令給這一個 Warp。
- **Multiple Threads:** Warp 內的 32 個執行緒各自擁有獨立的暫存器與程式計數器 (Program Counter)，並將該指令套用在各自的資料上。

## 分支發散 (Branch Divergence)
SIMT 最大的特色與挑戰在於處理條件分支。當 Warp 內的執行緒遇到 `if-else` 時：
- 如果所有執行緒都走同一條路徑，執行效率最高。
- 如果部分走 `if`，部分走 `else`（這稱為分支發散），硬體會強制 Warp 走完 `if` 路徑（此時走 `else` 的執行緒被遮蔽暫停），接著再走 `else` 路徑（此時走 `if` 的執行緒被暫停）。這會導致執行時間加倍，降低運算單元的利用率。

## 為什麼 AI 需要了解 SIMT？
深度學習模型（尤其是 CNN 與 Transformer 的矩陣乘法）本質上是大量獨立且無條件分支的數學運算。SIMT 架構能完美契合這種運算特徵，允許 GPU 輕易同時管理數以萬計的執行緒，並透過快速切換 Warp 來隱藏記憶體存取延遲。了解 SIMT 限制，有助於撰寫高效的 CUDA Kernel，避免分支發散造成的效能瓶頸。

## SIMD 與 SIMT 差異總結

- **程式撰寫視角：** SIMD 需明確編寫向量指令（如 AVX）；SIMT 則編寫純量指令（單一 Thread 邏輯），由硬體自動群組化執行。
- **彈性：** SIMT 允許各執行緒有獨立的執行路徑與記憶體位址存取；SIMD 強制鎖定資料對齊與同步。
- **硬體成本：** SIMT 為了維持每個執行緒的狀態，需要龐大的暫存器檔案（Register File），硬體成本較高。
