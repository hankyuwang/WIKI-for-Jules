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

## 核心概念與原理

傳統的編譯器架構 (例如單純依賴 LLVM IR) 在處理高階機器學習運算圖 (如 TensorFlow 或 PyTorch) 到底層特化硬體 (如 TPU 或 NPU) 時，由於缺乏足夠的語義層次，往往會喪失許多高階優化機會。MLIR 透過引入 **Dialects** (方言) 的概念，允許在同一個框架內定義多個層次的 IR。

1. **Dialects**：MLIR 的核心。你可以把 Dialect 想像成針對特定領域 (如線性代數、張量運算、硬體指令) 所自定義的 IR 集合。
2. **Progressive Lowering**：編譯過程是將高階 Dialect (如 `tensor`) 逐步轉換 (lower) 到更低階的 Dialect (如 `linalg` 再到 `llvm`)，在每一個抽象層級都能進行最適合的優化。

## 在 AI 編譯器中的應用

MLIR 被廣泛應用於現代 AI 編譯器中，例如 Google 的 [[XLA]] (Accelerated Linear Algebra) 演進與 [[OneAPI]] 的部分工具鏈，甚至 [[Triton]] 底層也利用了 MLIR 來實現從 Python 語法到 GPU 硬體指令的轉換。

## 優勢

- **高擴充性**：硬體廠商可以輕易地透過定義專屬的 Dialect 來接入 MLIR 生態，而不需要從頭寫一個完整的編譯器。
- **統一基礎設施**：減少了在不同編譯器 (如 TensorFlow Graph, XLA HLO, LLVM IR) 之間轉換造成的技術債與維護成本。
