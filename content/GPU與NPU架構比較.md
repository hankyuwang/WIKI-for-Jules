---
title: GPU與NPU架構比較
level: intermediate
tags:
  - gpu
  - npu
  - architecture
---

# GPU 與 NPU 架構比較

在 [[AI加速晶片概覽]] 中提到，GPU (Graphics Processing Unit) 和 NPU (Neural Processing Unit) 是目前最主流的兩種 AI 運算硬體。兩者在架構設計和應用場景上有著顯著的差異。

## GPU：極致的並行運算
GPU 最初設計用於圖形渲染，擁有大量的運算核心 (ALU)，非常適合處理高度並行的任務。在深度學習訓練階段，由於其強大的浮點運算能力和高記憶體頻寬，GPU 仍然是不可或缺的角色。

## NPU：專注於神經網絡
相比之下，[[NPU架構探索]] 顯示，NPU 針對深度學習中常見的運算（如矩陣乘法）進行了高度優化。通常採用脈動陣列 (Systolic Array) 架構，減少了資料搬運的開銷，從而在特定任務上達到更高的能效比 (Performance per Watt)。

## 綜合比較
- **通用性**: GPU 高於 NPU。
- **能效比**: NPU 通常優於 GPU（在深度學習任務上）。
- **主要應用**: GPU 多用於模型訓練，NPU 多用於終端裝置的推理。
