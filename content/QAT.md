---
title: QAT (Quantization-Aware Training)
level: intermediate
tags:
  - AI
  - QAT
  - Quantization
---

# QAT (Quantization-Aware Training)

摘要：QAT 是量化感知訓練(Quantization-Aware Training)，在模型訓練階段就引入量化誤差，讓模型在訓練過程中學習適應低精度運算，從而在大幅壓縮模型體積的同時，保持極高的預測精度。

## 核心概念與原理
在神經網路模型部署到硬體加速晶片（如 NPU 或邊緣裝置）時，為了降低運算與記憶體存取成本，通常會將浮點數（如 FP32）轉換為較低精度的整數（如 INT8）。這種過程稱為量化 ([[Quantization]])。
傳統的訓練後量化（[[PTQ]]）是在模型訓練完成後直接轉換，這往往會帶來無法挽回的精度損失，尤其是對於對數值敏感的網路結構。
QAT 的核心思想在於「假裝量化」（Fake Quantization）。在前向傳播 (Forward Pass) 階段，模型會模擬 INT8 的運算，引入捨入誤差 (Rounding Error) 與截斷誤差 (Clipping Error)。而在反向傳播 (Backward Pass) 階段，為了使梯度能夠順利傳遞，會使用「直通估計器」(Straight-Through Estimator, STE) 來繞過量化操作的不可導問題，直接傳遞浮點數梯度。

## 與 PTQ 的比較
- **精度**：QAT 通常能達到與全精度模型幾乎一致的表現，顯著優於 [[PTQ]]。
- **訓練成本**：QAT 需要額外的訓練時間與運算資源（通常是在預訓練模型上進行微調），而 PTQ 幾乎不需要訓練成本，只需少量的校準資料。
- **適用場景**：對於精度要求極高的應用（如自動駕駛、醫療影像）或極低精度量化（如 INT4），QAT 是必不可少的步驟。

## 最佳實務
目前主流作法是結合框架原生的 QAT API。開發者通常先訓練一個 FP32 基礎模型，然後在其圖結構中插入 Fake Quantize 節點，最後使用較小的學習率進行幾輪微調 (Fine-tuning)。
