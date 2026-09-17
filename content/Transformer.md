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

## 先備知識 (Prerequisites)
要深入理解 Transformer，建議先掌握以下基礎概念：
- [[深度學習運算原理]]：了解神經網路的基礎運作方式。
- [[RNN]] 與 [[CNN]]：早期的主流架構，了解它們的限制有助於明白為何需要 Transformer。
- [[MAC]]：底層硬體的乘累積加運算，理解為何矩陣乘法是 AI 的效能關鍵。

## 初學者延伸學習：Transformer 為什麼重要？
對於初學者而言，可以把 Transformer 想像成一個非常聰明的「閱讀理解」機器。傳統的模型（如 [[RNN]]）在閱讀文章時，是「從左到右」一個字一個字看，如果文章很長，它可能看到後面就忘了前面。

而 Transformer 透過 **自注意力機制 (Self-Attention)**，可以「一眼看完整段話」，並且自動找出這段話中哪些詞語之間有強烈的關聯。例如在句子 "The bank of the river" 中，它會自動將 "bank" 和 "river" 連結，判斷這裡是河岸而不是銀行。

### 主要變體：Encoder 與 Decoder
- **Encoder-only (如 BERT)**：擅長「理解」上下文，常用於文本分類、情感分析。
- **Decoder-only (如 GPT 系列)**：擅長「生成」文本，也是目前 ChatGPT 等大型語言模型 (LLM) 的主流架構。在生成時，會遇到 [[KV Cache]] 與 [[Long Context]] 的記憶體瓶頸。
- **Encoder-Decoder (如 T5)**：適合翻譯任務，將一段文本編碼後再解碼成另一種語言。

## 核心原理
Transformer 捨棄了傳統 [[RNN]] 依賴序列處理的限制，透過**自注意力機制 (Self-Attention)** 讓模型能夠同時關注輸入序列中的所有位置。這賦予了 Transformer 極高的平行化計算能力，非常適合在現代硬體 (如 [[GPU架構與AI計算]]) 上執行。

自注意力機制的核心在於計算 Query (Q), Key (K), Value (V) 矩陣，透過這些矩陣的乘法，模型能計算出每個字詞與其他字詞的關聯度。

## 模型架構組成
典型的 Transformer 包含以下模組：
- **Self-Attention 層**：捕捉序列內 token 之間的相互關係。這部分主要由大量的密集矩陣乘法組成。
- **Feed Forward Network (FFN)**：在每個位置獨立進行非線性變換，通常會將維度擴張再縮小，是參數與計算量最大的部分。
- **Layer Normalization** 與 **Residual Connections**：穩定訓練過程，解決深度網路的梯度消失問題 ([[反向傳播]])。

## 計算與記憶體挑戰
隨著模型規模與上下文長度的增加，Transformer 面臨著嚴峻的硬體挑戰，需要配合 [[硬體架構與SWHW協同]] 設計來解決：
- **平方複雜度**：自注意力機制的計算複雜度隨著序列長度呈平方增長，導致 [[Long Context]] 處理變得極其耗時，也增加了硬體的運算壓力。
- **[[KV Cache]] 記憶體瓶頸**：在推論 (Inference) 的生成階段 ([[Decode]])，必須儲存先前 token 的 Key 和 Value 矩陣，這會消耗極大的記憶體容量與頻寬，導致 Memory-bound 問題。

## 硬體映射挑戰
在硬體層面，Transformer 的平行性高度依賴晶片上大量的 SRAM (參考 [[SRAM微縮挑戰]]) 來快取權重。當面對極大規模的模型（如 GPT-4 或更大型的網路），必須採用 [[MoE]] (Mixture of Experts) 或模型並行等分散式策略。這使得網絡連線能力與晶片間的通訊頻寬 (如 [[NVLink]] 或 [[InfiniBand]]) 成為瓶頸。

## 前沿解決方案
為了解決 Transformer 的瓶頸，學界與業界提出了多種優化方案，包括演算法層級優化，以及 [[Mamba]]/[[SSM]] 等具備線性複雜度的新興架構替代方案。此外，硬體端也發展出如 [[TPU 架構深度解析]] 或特殊 AI 晶片來加速這些特定的矩陣運算。
