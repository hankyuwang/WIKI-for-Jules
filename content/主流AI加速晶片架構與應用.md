---
title: 主流AI加速晶片架構與應用
level: intermediate
tags:
  - architecture
  - application
---

# 主流AI加速晶片架構與應用

摘要：探討目前市場上最主流的 AI 加速晶片架構，以及它們在資料中心與邊緣運算中的實際應用場景。

## Prerequisites
- [[商用AI加速晶片架構研究]]

## 架構概覽與場景

市場上的 AI 晶片可分為兩大應用場景：

1. **雲端與資料中心 (Cloud & Data Center)**
   - **代表架構**：NVIDIA Hopper/Blackwell, Google TPU, AMD Instinct。
   - **特點**：追求極致算力與記憶體頻寬，使用先進封裝 (如 [[CoWoS]]) 與昂貴的 [[HBM]]。支援大規模分散式訓練與推論。
   - **應用**：訓練千億參數級別的大型基礎模型、提供大規模雲端 API 服務。

2. **邊緣運算 (Edge Computing)**
   - **代表架構**：NPU (如 Apple Neural Engine), 專用 ASIC, 邊緣 GPU (如 Jetson 系列)。
   - **特點**：受到嚴格的功耗（通常在幾瓦到幾十瓦之間）與成本限制。更重視 TOPS/W (每瓦效能)。依賴模型量化 (如 [[INT8]]) 技術。
   - **應用**：自駕車、智慧安防攝影機、行動裝置上的本機 AI 功能。
