---
title: Tensor Core
level: beginner
tags:
  - hardware
  - gpu
  - tensor-core
---

# Tensor Core

Tensor Core 是 NVIDIA GPU 中專為深度學習設計的專用硬體運算單元，旨在加速矩陣乘法與累加運算 (MAC)，從而大幅提升 AI 訓練與推理的效能。

## 背景知識
要了解 Tensor Core，建議先具備以下背景知識：
- [[MAC]]：乘累積加運算，深度學習底層矩陣運算最基本的操作單位。
- [[GPU架構與AI計算]]：了解 GPU 的平行運算特性與硬體架構演進。
- [[FP16]]、[[INT8]]、[[FP8]]：了解各種資料精度及其在深度學習中的應用。

## 為什麼需要 Tensor Core？
在 Tensor Core 誕生之前，GPU 主要依賴 CUDA Core 進行運算。CUDA Core 擅長處理通用的標量 (Scalar) 運算，但對於深度學習中大量的矩陣相乘，效率有限。
Tensor Core 是針對矩陣運算量身打造的。它能在一個時脈週期內，完成小矩陣的乘法與累加，將原本需要多個 CUDA Core 與多個時鐘週期才能完成的工作，濃縮成單一指令執行。

## 運作原理
Tensor Core 的核心在於 **混合精度運算 (Mixed Precision)**：
1. **輸入**：接收低精度 (例如 FP16、INT8、甚至 FP8) 的資料。
2. **計算**：進行高吞吐量的矩陣乘法。
3. **累加**：將結果以高精度 (例如 FP32) 進行累加，以減少精度損失。
4. **輸出**：輸出高精度結果，或根據需求轉回低精度。

這種混合精度策略，能在不犧牲模型準確度的前提下，大幅節省記憶體頻寬，並顯著提升運算速度。

## 世代演進
Tensor Core 隨著 NVIDIA GPU 架構的演進不斷進化：
- **Volta 架構**：首次引入 Tensor Core，支援 FP16 運算。
- **Turing 架構**：加入 INT8 和 INT4 支援，加強推理能力。
- **Ampere 架構**：引入 TF32 (TensorFloat-32) 與 BF16 (Bfloat16)，以及稀疏性 (Sparsity) 支援。
- **Hopper 架構**：進一步引入 FP8 支援，並搭載 Transformer Engine，針對大型語言模型 (LLM) 進行優化。

## 總結
Tensor Core 是現代 GPU 能在 AI 領域取得統治地位的關鍵因素之一。它針對深度學習的核心需求——矩陣運算——進行了極致的優化，開啟了 AI 算力的新紀元。
