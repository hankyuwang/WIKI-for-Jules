---
title: MLIR
level: intermediate
tags:
  - AI
  - MLIR
  - Compiler
---

# MLIR (Multi-Level Intermediate Representation)

摘要：MLIR 是一個多層次中間表示編譯框架，旨在統一不同層級的 IR，改善編譯器重用性，解決傳統編譯器 (如 LLVM) 在針對異質硬體 (如 AI 加速器) 時所面臨的架構瓶頸。

## Prerequisites (先備知識)
- [[基礎計算機結構]]：理解高階語言如何轉換為機器碼。

## 為什麼需要多層次編譯？
傳統的編譯器架構 (例如單純依賴 LLVM IR) 就像是直接把文言文翻譯成最底層的機器語言。在處理高階機器學習運算圖 (如 TensorFlow 或 PyTorch) 到底層特化硬體 (如 TPU 或 NPU) 時，由於缺乏中間的「語義層次」，往往會喪失許多高階優化機會（例如矩陣相乘的優化在底層 IR 中很難被辨識出來）。

MLIR 解決這個問題的方法是引入 **「Dialects (方言)」** 的概念，允許在同一個框架內定義多個層次的 IR。

## 核心概念與運作範例
1. **Dialects**：你可以把 Dialect 想像成針對特定領域所自定義的專門術語集合。例如：
   - `tensor` dialect：專門描述張量操作的高階語義。
   - `linalg` dialect：專門描述線性代數運算（如矩陣乘法）。
   - `vector` dialect：描述單指令多資料流 (SIMD) 的硬體指令。
   - `llvm` dialect：最底層的通用機器指令。

2. **Progressive Lowering (漸進式降級)**：編譯過程不再是一步到位，而是將高階 Dialect (如 `tensor`) 逐步轉換 (lower) 到 `linalg`，再到 `vector`，最後到 `llvm`。**在每一個抽象層級，編譯器都能進行最適合該層級的最佳化。**

## 在 AI 加速器中的應用優勢
對於硬體廠商開發新一代 AI 加速器 (如 NPU)，MLIR 提供了巨大的價值：
- **重用性**：廠商不需要從頭寫一個完整的編譯器。他們可以重用上層的 `tensor` 與 `linalg` 優化，只需專注於開發自己硬體專屬的底層 Dialect。
- **異質運算**：可以輕鬆地在同一個模型中，將不同部分的運算圖派發給不同的硬體（如 CPU, GPU, 專屬加速單元）執行。
