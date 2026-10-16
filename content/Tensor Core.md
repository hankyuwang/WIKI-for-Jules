---
title: Tensor Core
level: beginner
tags:
  - hardware
  - gpu
  - architecture
  - nvidia
---
# Tensor Core

> Tensor Core 是 NVIDIA GPU 中專門為深度學習設計的運算單元，旨在極大地加速矩陣乘法與累加 (MAC, Multiply-Accumulate) 運算。

## 什麼是 Tensor Core？
在 AI 與深度學習的計算中，最核心且佔用最多運算資源的操作便是**矩陣相乘**。
傳統的 [[CUDA]] 核心在執行計算時，一次只能處理單一的數據乘加；而 **Tensor Core** 則可以在單一的時脈週期內，一口氣處理整個小矩陣（例如 4x4）的乘法與累加運算。

這種設計使得配備 Tensor Core 的 GPU 在處理 AI 任務時的吞吐量（Throughput）比起傳統 GPU 呈現指數級的成長。

## 架構演進
自從在早期 Volta (現已演進至 Hopper/Blackwell) 架構中首次引入以來，Tensor Core 經歷了多次世代的進化：
- **第一代 (Volta, 早期架構)**：首次引入混合精度運算 (Mixed Precision)，支援 FP16 的輸入與 FP32 的累加，大幅降低記憶體頻寬需求同時保持精度。
- **第二代 (Turing) 與第三代 (Ampere)**：加入了對更多數據格式的支援，例如 INT8, INT4（應用於 [[模型量化技術]] 與推論加速），以及對稀疏矩陣 (Sparsity) 的硬體加速，進一步提升算力。
- **第四代 (Hopper)**：引入了革命性的 **Transformer Engine**，原生支援 [[FP8]] 運算。系統會根據每層神經網路的數值分佈，自動在 FP8 與 FP16 之間切換，專門為了加速 LLM (大型語言模型) 而生。
- **第五代 (Blackwell)**：進一步推動了精度的極限，支援微縮 FP4 精度運算，並具備專屬的動態 Scaling 引擎，為萬億參數模型提供極致效能。

## 為什麼它如此重要？
現代的 AI 語言模型（例如 GPT 系列，基於 [[Transformer]] 架構）是由海量的矩陣組成。如果沒有 Tensor Core 的矩陣乘法硬體加速，訓練這些模型將需要耗費數年甚至更長的時間。

透過將計算精度降低（如 FP8），並將底層運算交由專屬硬體負責，Tensor Core 完美地兼顧了「運算速度」與「模型準確度」。

## 延伸閱讀
- 了解 GPU 的演進過程：[[GPU架構與演進]]
- Tensor Core 的競爭對手（如 Google TPU 的核心陣列）：[[Systolic Array]]
- 軟體如何發揮 Tensor Core 的極限：[[Triton]] 或手寫 [[CUDA]] Kernel。
