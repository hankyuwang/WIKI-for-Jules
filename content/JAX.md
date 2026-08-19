---
title: JAX
level: intermediate
tags:
  - AI
  - JAX
  - Framework
---

# JAX

摘要：JAX 是 Google 開發的高效能機器學習與數值運算框架，結合了自動微分 (Autograd) 與 [[XLA]] 編譯器。

## 核心特性
JAX 旨在提供比 [[TensorFlow]] 或 [[PyTorch]] 更接近底層的靈活性與極致效能，主要依賴以下幾個核心函數轉換 (Function Transformations)：
- **`jit` (Just-In-Time Compilation)**：透過 [[XLA]] 編譯器將 Python 程式碼編譯成高效的機器碼，極大化執行速度。
- **`grad`**：提供強大且精確的自動微分能力。
- **`vmap` 與 `pmap`**：輕鬆實現向量化與多設備上的平行化處理。

## 設計哲學
JAX 採用函數式編程 (Functional Programming) 的設計哲學，強調純函數 (Pure Functions) 與不可變的資料結構。這使得 JAX 產生的計算圖極其清晰，有助於編譯器進行更激進的優化。

## 硬體與生態系統
JAX 由於原生深度整合了 [[XLA]]，使其展現出無與倫比的效能優勢。許多前沿的大型語言模型與分散式訓練框架，都開始採用 JAX 作為底層運算引擎，以突破現有框架的效能天花板。此外，JAX 生態系中也包含了如 Flax (基於 JAX 的神經網路函式庫) 與 Optax (最佳化函式庫) 等工具，使其不僅限於底層運算，也能支援高階模型開發。
