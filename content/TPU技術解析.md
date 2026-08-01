---
title: TPU技術解析
level: advanced
tags:
  - tpu
  - asic
  - architecture
---

# TPU 技術解析

TPU (Tensor Processing Unit) 是 Google 專為機器學習定制的 ASIC (特殊應用積體電路)。它是 [[AI加速晶片概覽]] 中極具代表性的一種架構。

## 核心設計理念
TPU 的核心是龐大的矩陣乘法單元 (Matrix Multiply Unit, MXU)，這也是它與傳統 CPU 或 GPU 的最大區別。MXU 採用了脈動陣列 (Systolic Array) 設計，使得資料在陣列中流動，每個運算單元在一個時鐘週期內完成乘加運算，並將結果傳遞給下一個單元。

## 效能優勢
這種設計極大地減少了對外部記憶體的存取次數，這點在 [[AI晶片記憶體架構]] 的探討中尤為重要。因為在深度學習運算中，資料搬運往往是最大的效能瓶頸和功耗來源。

## TPU 世代演進
- 第一代 TPU 主要針對推理 (Inference) 任務，專注於 8-bit 整數運算。
- 隨後的 TPU 世代 (v2, v3, v4 等) 加入了浮點運算能力，並支援大規模模型的分散式訓練。
