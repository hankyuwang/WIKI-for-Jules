---
title: Long Context
level: intermediate
tags:
  - AI
  - Long-Context
---

# Long Context

摘要：Long Context 是 長文本處理，在LLM中需要消耗大量記憶體與運算資源，KV Cache管理為其瓶頸。

## 已知事實
在業界，Long Context 的硬體與軟體支援度不斷提升，成為解決特定技術瓶頸的關鍵。

## 原理
Long Context 運作的核心在於透過底層架構的最佳化，解決傳統架構在 長文本處理 上遇到的效能瓶頸。

## 限制
導入 Long Context 面臨的主要挑戰包含實作複雜度高、硬體資源限制，以及與現有生態系統的相容性問題。

## 未知問題
未來針對 Long Context 的研究將聚焦於如何在保持高效能的同時，進一步降低功耗與開發門檻。

## 最佳實務
目前主流作法是將 Long Context 整合至現有的軟硬體堆疊中，並利用自動化工具輔助調優。

## 個人見解
隨著 AI 模型規模日益龐大，Long Context 所代表的優化策略將是決定次世代系統效能的勝負手。

## 方案與觀點分析

### 方案一：基於現有框架的軟體層優化
- 優點：無須硬體更動，導入快
- 缺點：效能提升有限
- 成本：低
- 維護性：高
- 風險：無法突破硬體天花板

### 方案二：客製化硬體 (ASIC) 方案
- 優點：極致效能與能效
- 缺點：開發週期長，缺乏彈性
- 成本：極高
- 維護性：低
- 風險：沉沒成本高

### 方案三：軟硬協同設計 (Co-design)
- 優點：兼具彈性與效能
- 缺點：跨領域整合難度極高
- 成本：中高
- 維護性：中等
- 風險：專案複雜度帶來的延遲風險


## 背景與核心挑戰 (補充說明)
在標準的 [[Transformer]] 架構中，注意力機制（Self-Attention）的運算複雜度與序列長度（Sequence Length）呈現**二次方（O(N²)）增長**。當文本長度增加時，會遇到以下瓶頸：
1. **運算瓶頸**：Prefill 階段的矩陣運算量暴增。
2. **記憶體牆（Memory Wall）**：Decode 階段的 [[KV Cache]] 會呈線性增長，佔用大量高頻寬記憶體（[[HBM]]）。例如，當上下文長度達到 100K Token 時，單個請求的 KV Cache 可能高達數 GB，這嚴重限制了硬體的吞吐量（Batch Size）。

## 硬體與軟體層面的解決方案 (補充說明)
為了解決 Long Context 帶來的挑戰，業界在演算法與系統架構上提出了多種優化：

### 軟體與演算法優化
1. **FlashAttention**：透過硬體感知（Hardware-aware）的算法重構，最大化利用 GPU 的 SRAM (Shared Memory)，減少對外部 HBM 的讀寫次數，大幅加速了長序列的 Attention 運算。
2. **PagedAttention**：靈感來自作業系統的虛擬記憶體分頁機制。將 KV Cache 分割為不連續的記憶體區塊，減少記憶體碎片，提升了平行處理能力（如 vLLM 框架所採用）。
3. **Sparse Attention 與 Sliding Window**：只讓模型關注鄰近或關鍵的 Token，將 O(N²) 複雜度降至 O(N) 或 O(N log N)。

### 架構層面的革新
1. **Ring Attention**：透過跨多個 GPU 節點的分散式計算，將長序列分佈在不同的裝置上，利用 [[NVLink]] 傳遞數據。
2. **線性複雜度模型**：尋求能替代 Transformer 的新型架構。例如 [[Mamba]] 與基於 [[SSM]] (狀態空間模型) 的網路，它們在處理長序列時不需龐大的 KV Cache，具有線性複雜度的優勢。

## 研究方向與未來展望 (補充說明)
如何在不犧牲模型精確度與召回率（Recall，如 Needle In A Haystack 測試）的前提下，透過軟硬體協同設計（Software-Hardware Co-design），進一步降低長文本處理的延遲與功耗，是次世代 AI 推理系統的核心課題。
