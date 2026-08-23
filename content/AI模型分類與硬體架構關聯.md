---
title: AI模型分類與硬體架構關聯
level: beginner
tags:
  - model-architecture
  - hardware
---

# AI模型分類與硬體架構關聯

摘要：不同的 AI 模型架構（如 CNN, RNN, Transformer）擁有截然不同的運算特徵。了解這些差異有助於選擇或設計最合適的硬體架構。

## Prerequisites
- [[AI模型分類與硬體需求]]

## 核心模型特徵與硬體需求

1. **卷積神經網路 (CNN)**
   - **特徵**：大量的局部資料重複使用（Weight Reuse）和密集的乘加運算（MAC）。
   - **硬體需求**：非常適合使用脈動陣列（[[Systolic Array]]）或具有大量平行運算單元的架構，對記憶體頻寬的需求相對較小。

2. **遞迴神經網路 (RNN)**
   - **特徵**：循序運算（Sequential Computation），下一個時間步的運算依賴前一個時間步的結果。
   - **硬體需求**：平行化困難，容易遇到管線停滯 (Pipeline Stall)。需要快速的 SRAM 來暫存隱藏狀態。

3. **Transformer 與大型語言模型 (LLM)**
   - **特徵**：注意力機制（Attention Mechanism）帶來巨大的矩陣乘法，以及自回歸生成時的記憶體頻寬瓶頸（特別是載入 [[KV Cache]]）。
   - **硬體需求**：極度渴望記憶體頻寬。因此，[[HBM]] (高頻寬記憶體) 成為這類模型硬體的標準配置。
