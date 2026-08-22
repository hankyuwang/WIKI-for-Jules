---
title: AI晶片軟體堆疊與SDK設計
level: intermediate
tags:
  - software-stack
  - sdk
---

# AI晶片軟體堆疊與SDK設計

摘要：AI 加速晶片的成功不僅取決於硬體算力，軟體堆疊（Software Stack）與軟體開發套件（SDK）的設計更是關鍵。本篇探討從底層硬體驅動到高階 AI 框架的整體架構。

## Prerequisites
- [[基礎計算機結構]]
- [[硬體架構與SWHW協同]]

## 軟體堆疊的分層架構

一個完整的 AI 加速器軟體堆疊通常包含以下層級：

1. **高階框架層 (High-Level Frameworks)**：如 PyTorch, TensorFlow, JAX。這是開發者直接操作的介面，提供建立神經網路模型的 API。
2. **編譯器與圖優化層 (Compiler & Graph Optimization)**：如 XLA, MLIR, TVM。這層負責將高階框架產生的計算圖進行優化，例如 [[算子融合]] (Operator Fusion) 與記憶體配置。
3. **運算元函式庫 (Kernel Libraries)**：如 NVIDIA 的 cuBLAS, cuDNN，或是 AMD 的 MIOpen。這些是針對特定硬體架構高度最佳化（常以組合語言撰寫）的基礎數學運算集合（如矩陣乘法、卷積）。
4. **執行時期與驅動程式 (Runtime & Driver)**：負責與硬體溝通，管理記憶體配置、工作排程以及主機 (CPU) 與設備 (AI 晶片) 之間的資料傳輸。

## 虛擬團隊的見解 (Virtual Team Insights)
> **研究員**：我們觀察到新創晶片公司常面臨「軟體牆」。即便晶片算力高，若沒有類似 CUDA 般成熟的 SDK，開發者將難以將模型部署到硬體上。
> **驗證員**：因此，支援開源編譯器基礎設施（如 MLIR 和 OpenAI 的 Triton）已成為自研晶片的最佳實務，這能大幅降低構建自定義軟體堆疊的成本。
