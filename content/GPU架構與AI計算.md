---
title: GPU架構與AI計算
level: intermediate
tags:
  - GPU
  - AI Accelerator
  - Parallel Computing
---

# GPU架構與AI計算

圖形處理單元（GPU）由於具備大量核心，特別擅長處理高度平行的運算任務，這使其成為現代人工智慧發展的基石。本文探討 GPU 如何適應並加速 AI 計算。

## Prerequisites
- [[AI加速晶片概述]]
- [[基礎計算機結構]]

## GPU 的核心優勢
相較於 CPU 的少量高效能核心，GPU 擁有數以千計的較小核心。這種架構非常適合深度學習中的矩陣乘法與卷積運算，這些運算可以輕易地被拆分並平行處理。

## Tensor Core 與 AI 專屬優化
NVIDIA 等廠商在近代 GPU 中引入了 Tensor Core，這是專門為深度學習設計的運算單元。Tensor Core 可以在單一指令中完成 4x4 的矩陣乘加運算（Mixed Precision，例如 FP16 與 FP32 混合），大幅提升了吞吐量。此外，為了降低顯存壓力與加速運算，通常會結合 [[模型量化技術]]。

## 記憶體頻寬與互連技術
AI 訓練的瓶頸往往在於數據傳輸。因此，高頻寬記憶體（HBM, High Bandwidth Memory）和 NVLink 等高速互連技術成為現代 AI GPU 的標準配置。

## 在不同場景中的應用
GPU 主要主導雲端的模型訓練（Training）與大規模推理（Inference）。然而，在邊緣端，通常會考慮功耗更低的解決方案，詳見 [[邊緣運算AI晶片]] 與 [[NPU架構探索]]。