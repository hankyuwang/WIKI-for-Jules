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

## 核心原理
Transformer 捨棄了傳統 [[RNN]] 依賴序列處理的限制，透過**自注意力機制 (Self-Attention)** 讓模型能夠同時關注輸入序列中的所有位置。這賦予了 Transformer 極高的平行化計算能力，非常適合在硬體上執行。

## 模型架構組成
典型的 Transformer 包含以下模組：
- **Self-Attention 層**：捕捉序列內 token 之間的相互關係。
- **Feed Forward Network (FFN)**：在每個位置獨立進行非線性變換。
- **Layer Normalization** 與 **Residual Connections**：穩定訓練過程。

## 計算與記憶體挑戰
隨著模型規模與上下文長度的增加，Transformer 面臨著嚴峻的硬體挑戰：
- **平方複雜度**：自注意力機制的計算複雜度隨著序列長度呈平方增長，導致 [[Long Context]] 處理變得極其耗時。
- **[[KV Cache]] 記憶體瓶頸**：在推論 (Inference) 的生成階段，必須儲存先前 token 的 Key 和 Value 矩陣，這會消耗極大的記憶體容量與頻寬，導致 Memory-bound 問題。

## 硬體映射挑戰
在硬體層面，Transformer 的平行性高度依賴晶片上大量的 SRAM 來快取權重。當面對極大規模的模型（如 GPT-4 或更大型的網路），必須採用 [[MoE]] (Mixture of Experts) 或模型並行等分散式策略，這使得網絡連線能力與晶片間的通訊頻寬成為瓶頸。

## 前沿解決方案
為了解決 Transformer 的瓶頸，學界與業界提出了多種優化方案，包括演算法層級優化，以及 [[Mamba]]/[[SSM]] 等具備線性複雜度的新興架構替代方案。
