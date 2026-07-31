---
title: AI 加速晶片概覽
level: beginner
tags:
  - ai-accelerator
  - hardware
  - overview
---

# AI 加速晶片概覽

AI 加速晶片是專門為人工智慧（AI）運算設計的硬體，能夠提供比傳統中央處理器（CPU）更高的效能和能源效率。這些晶片主要用於機器學習、深度學習和類神經網路等需要大量平行運算的工作負載。

## 為什麼我們需要 AI 加速晶片？

傳統的處理器（如 CPU）設計目標在於處理通用任務，它們具備複雜的控制邏輯和少量的核心，適合執行序列式（sequential）的工作。然而，AI 運算（尤其是深度學習）通常涉及大量的矩陣乘法和張量運算，這些運算高度平行且可以同時處理龐大的數據。

AI 加速晶片透過大量的核心、特殊的記憶體架構以及專用的指令集，能夠在相同的時間內完成比 CPU 多上百倍甚至千倍的運算，同時大幅降低能源消耗。

## 常見的 AI 加速晶片類型

目前市場上的 AI 加速晶片主要分為以下幾種：

- **GPU (Graphics Processing Unit)**: 最初為圖形渲染設計，因其高度平行的架構，成為目前最廣泛使用的 AI 訓練晶片。詳見 [[GPU在AI加速的應用]]。
- **ASIC (Application-Specific Integrated Circuit) & TPU**: 專為特定任務（如特定神經網路模型）設計的晶片。Google 的 TPU (Tensor Processing Unit) 是最著名的例子。詳見 [[ASIC與TPU架構分析]]。
- **FPGA (Field-Programmable Gate Array)**: 可以透過軟體重新配置硬體邏輯的晶片，提供高度的靈活性，適用於演算法快速迭代的階段。詳見 [[FPGA在AI硬體的角色]]。
- **NPU (Neural Processing Unit)**: 專為類神經網路運算設計的處理器，常見於手機和邊緣設備。詳見 [[NPU架構探索]]。

## 邊緣運算與新型記憶體解決方案

隨著 AI 應用的普及，越來越多的運算需要在靠近資料來源的邊緣設備（如手機、物聯網設備）上進行，這推動了 [[邊緣AI晶片設計]] 的發展。

此外，AI 晶片的效能往往受限於記憶體頻寬和延遲（即「記憶體牆」問題），這促使了 [[AI晶片的新型記憶體解決方案]] 的研究與突破，如 HBM (High Bandwidth Memory) 和 PIM (Processing In Memory) 技術。
