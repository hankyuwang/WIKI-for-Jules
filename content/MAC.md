---
title: MAC (Multiply-Accumulate)
level: beginner
tags:
  - hardware
  - arithmetic
---

# MAC (Multiply-Accumulate 乘積累加運算)

摘要：MAC (Multiply-Accumulate) 是深度學習硬體中最基礎、也最核心的運算單元。理解 MAC，是理解 GPU、TPU 以及神經網路為何能運作的第一步。

## Prerequisites
- [[基礎計算機結構]]
- [[深度學習運算原理]]

## 什麼是 MAC？

MAC 的全名是 Multiply-Accumulate（乘積累加）。它執行的是一個非常簡單的數學方程式：

$$a \leftarrow a + (b \times c)$$

也就是把 $b$ 和 $c$ 相乘，然後把結果加到目前的累加器 $a$ 上面。這一個動作，在硬體設計上被實作為一個單一的運算週期（Clock Cycle），這個專門負責執行此數學運算的硬體單元就稱為 MAC 單元。

## 為什麼 MAC 在 AI 中如此重要？

如果你回想神經網路的基本原理，一個神經元（Neuron）的輸出是：

$$y = \sum (權重 \times 輸入) + 偏差值$$

這正是無數個「相乘然後相加」的過程。
- **在 CNN 中**：影像處理的卷積運算 (Convolution) 本質上就是濾波器權重與影像像素點的 MAC 運算。
- **在 LLM 中**：大型語言模型（如 [[Transformer]] 架構）的核心是龐大的矩陣相乘 (Matrix Multiplication)。一個矩陣相乘可以拆解成無數個點積，而點積的底層全部都是由數以十億、百億計的 MAC 運算所構成。

> **虛擬團隊教育員補充：資料搬移比運算更昂貴！**
> 雖然 MAC 是核心，但在現代 AI 晶片中，**把資料 (b 和 c) 從記憶體搬運到 MAC 單元所消耗的能量，往往比執行 MAC 運算本身高出幾個數量級**。這就是為什麼現代架構如 [[TPU 架構深度解析]] 會發展出 [[Systolic Array]]，或者研究 [[PIM記憶體內運算技術]]，目的都是為了減少資料搬運，讓 MAC 單元能持續滿載運作而不被餓死（Data Starvation）。

## 精度與 MAC 效率的權衡

在神經網路中，資料的表示方式（精度）會嚴重影響 MAC 的效率：
- **FP32 (單精度浮點數)**：傳統精細的計算，佔用空間大，MAC 電路複雜，速度慢。
- **[[FP16]] / BF16**：現代 AI 訓練的主流，減少了表示範圍或精度，但硬體能以倍數速度執行 MAC 運算。
- **[[INT8]] / INT4**：透過 [[Quantization]] (量化) 技術將浮點數轉換為整數，常用於推論階段。整數 MAC 的電路極小且省電，可以讓晶片在相同面積下塞入更多 MAC 單元，吞吐量大幅躍升。

## MAC 與算力的關係 (TOPS)

我們常聽到評估 AI 晶片算力的單位叫做 **TOPS (Tera Operations Per Second)**，代表每秒可以進行一兆次運算。

一次 MAC 運作包含了兩個操作（一個乘法和一個加法，也就是 2 Operations）。
所以，如果一個晶片有 $1000$ 個 MAC 單元，運作時脈是 $1$ GHz（每秒十億次週期），它的理論算力大約是：
$$1000 \text{ (MACs)} \times 1\text{G (Hz)} \times 2 \text{ (Ops/MAC)} = 2000 \text{ GOPS} = 2 \text{ TOPS}$$

這也是為什麼像 [[GPU架構與AI計算]] 這樣的硬體，會盡可能捨棄複雜的控制邏輯與大型快取，將晶片面積大量讓給 MAC 單元（或稱為 Tensor Cores），以換取極高的平行運算吞吐量。
