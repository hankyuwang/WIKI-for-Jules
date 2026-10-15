---
title: Tensor Core
level: beginner
tags:
  - hardware
  - gpu
  - tensor-core
---
# Tensor Core (張量核心)

> Tensor Core 是 NVIDIA 從 Volta 架構開始引入的一種專門用於深度學習矩陣運算的硬體加速單元。它能夠以極高的效率執行混合精度（Mixed Precision）的矩陣乘累積加 (MAC) 運算。

## 什麼是張量 (Tensor)？
在深度學習中，我們處理的資料往往是多維度的陣列。
- 一維陣列稱為**向量 (Vector)**
- 二維陣列稱為**矩陣 (Matrix)**
- 三維以上的陣列則統稱為**張量 (Tensor)**

## 為什麼需要 Tensor Core？
傳統的 GPU 核心（CUDA Core）主要是為了處理圖形渲染中的浮點運算（例如單個像素的顏色計算）而設計。雖然它們能夠平行運算，但每次只能執行一個純量（Scalar）運算（如 A + B = C）。

但在訓練和推理深度學習模型（如 [[Transformer]]、[[CNN]]）時，最核心的操作是巨大的「矩陣相乘」。
Tensor Core 的設計理念是：**不要一次算一個數字，而是硬體層面上一次算一整個小矩陣！**

舉例來說，一個第一代的 Tensor Core 可以在單個時脈週期（Clock Cycle）內，完成一個 4x4 矩陣的相乘與累加（$D = A 	imes B + C$）。這相當於一口氣執行了 64 個浮點乘積和 64 個浮點加法，速度比傳統 CUDA Core 快上數十倍。

## 混合精度運算 (Mixed Precision)
Tensor Core 另一個強大的地方在於支援**混合精度**。在神經網路中，我們不一定需要非常精確的數字。Tensor Core 能夠：
1. 接收低精度（如 [[FP16]]、[[INT8]]，甚至後來的 [[FP8]] 或 [[INT4]]）的輸入資料以加速運算並節省記憶體頻寬。
2. 在內部計算與輸出時，使用較高精度（如 FP32 或 FP16）進行累加，以確保模型的準確度不會流失。

## 架構演進
- **早期 Volta 架構**：首次引入 Tensor Core，主要支援 FP16 計算。
- **Turing / Ampere 架構**：增加了對 INT8, INT4 甚至 TF32 的支援，使其更適合推理 (Inference) 任務。
- **Hopper / Blackwell 架構**：引入了更靈活的 Transformer Engine，能夠根據網路每一層的需求動態切換 FP8 和 FP16，進一步突破了大型語言模型 (LLM) 的記憶體瓶頸。

## 延伸閱讀
- [[GPU運算架構]]：了解 GPU 如何利用大量的核心進行平行運算。
- 混合精度訓練 (Mixed Precision Training)：深入探討如何利用 Tensor Core 進行高效能模型訓練。
- [[MAC]]：了解最基本的乘累積加運算。
