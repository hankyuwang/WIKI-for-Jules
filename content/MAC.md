---
title: MAC (Multiply-Accumulate)
level: beginner
tags:
  - hardware
  - arithmetic
---

# MAC (Multiply-Accumulate 乘加運算)

摘要：MAC (Multiply-Accumulate) 是深度學習硬體中最基礎、也最核心的運算單元。理解 MAC，是理解 GPU、TPU 以及神經網路為何能運作的第一步。

## Prerequisites
- [[基礎計算機結構]]

## 什麼是 MAC？

MAC 的全名是 Multiply-Accumulate（乘積累加）。它執行的是一個非常簡單的數學方程式：

$$a \leftarrow a + (b \times c)$$

也就是把 $b$ 和 $c$ 相乘，然後把結果加到目前的累加器 $a$ 上面。這一個動作，在硬體設計上被實作為一個單一的運算週期，這個硬體單元就稱為 MAC 單元。

## 為什麼 MAC 在 AI 中如此重要？

如果你回想神經網路的基本原理，一個神經元的輸出是：

$$y = \sum (權重 \times 輸入) + 偏差值$$

這正是無數個「相乘然後相加」的過程。無論是卷積神經網路 (CNN) 中的卷積運算，還是大型語言模型 (LLM) 中的龐大矩陣相乘，其底層全部都是由數以十億、百億計的 MAC 運算所構成。

> **虛擬團隊教育員補充**：你可以把 AI 模型想像成一座由樂高積木組成的巨大城堡，而 MAC 就是最基本的那一塊樂高積木。AI 加速晶片的強大與否，很大程度上取決於它能在晶片上塞入多少個 MAC 單元，以及它能多快地提供資料給這些單元運作。

## MAC 與算力的關係 (TOPS)

我們常聽到評估 AI 晶片算力的單位叫做 **TOPS (Tera Operations Per Second)**，代表每秒可以進行一兆次運算。

一次 MAC 運作包含了兩個操作（一個乘法和一個加法）。所以，如果一個晶片有 $1000$ 個 MAC 單元，運作時脈是 $1$ GHz（每秒十億次週期），它的理論算力大約是：
$1000 \text{ (MACs)} \times 1\text{G (Hz)} \times 2 \text{ (Ops/MAC)} = 2000 \text{ GOPS} = 2 \text{ TOPS}$。

這也是為什麼像 [[GPU架構與AI計算]] 和 TPU 這樣的硬體，會盡可能捨棄複雜的控制邏輯，將晶片面積大量讓給 MAC 單元，以換取極高的運算吞吐量。
