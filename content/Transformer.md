---
title: Transformer
level: intermediate
tags:
  - AI
  - Transformer
  - Architecture
---

# Transformer

摘要：Transformer 是一種基於自注意力機制 (Self-Attention) 的深度學習架構，已成為現代大型語言模型 (LLM) 的核心基礎，徹底改變了自然語言處理 (NLP) 領域。

## Prerequisites (先備知識)
- [[深度學習運算原理]] : 了解神經網路基礎運算。
- [[RNN]] : 了解早期處理序列資料的模型及其限制。

## 核心原理：自注意力機制 (Self-Attention)
Transformer 捨棄了傳統 [[RNN]] 依賴序列逐步處理的限制。透過**自注意力機制 (Self-Attention)**，模型能夠在處理當前單詞時，同時「關注」輸入序列中的所有其他單詞，並賦予不同的權重。
這不僅提升了模型理解上下文的能力，還賦予了 Transformer 極高的平行化計算能力，非常適合在 GPU 等硬體上執行。

## 模型架構組成
典型的 Transformer 包含以下模組：
- **Self-Attention 層**：捕捉序列內 token 之間的相互關係。
- **Feed Forward Network (FFN)**：在每個位置獨立進行非線性變換。
- **Layer Normalization** 與 **Residual Connections**：用於穩定深層網路的訓練過程。

## 計算與記憶體挑戰
隨著模型規模與上下文長度的增加，Transformer 面臨著嚴峻的硬體挑戰：
- **平方複雜度**：自注意力機制的計算與記憶體需求隨著序列長度呈平方增長，導致 [[Long Context]] 處理變得極其耗時且佔用大量記憶體。
- **[[KV Cache]] 記憶體瓶頸**：在推論 (Inference) 的生成階段 (如 [[Decode]])，必須儲存先前 token 的 Key 和 Value 矩陣。這會消耗極大的高頻寬記憶體容量，導致嚴重的 Memory-bound 問題。

## 硬體映射挑戰與前沿解決方案
在硬體層面，面對極大規模的模型，單一晶片無法容納，必須採用 [[MoE]] (Mixture of Experts) 或模型並行策略，這使得網絡通訊頻寬成為瓶頸。
為了解決 Transformer 的根本瓶頸，學界提出了如 [[Mamba]] 與其底層理論 [[SSM]] 等具備線性複雜度的新興架構，作為未來的潛在替代方案。
