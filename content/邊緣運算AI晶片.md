---
title: 邊緣運算AI晶片
level: intermediate
tags:
  - edge-ai
  - hardware
  - npu
---

# 邊緣運算 AI 晶片

與資料中心裡龐大的 GPU 或 TPU 叢集不同，邊緣運算 (Edge Computing) 環境下的 AI 晶片面臨著嚴苛的功耗 (Power)、效能 (Performance) 和面積 (Area) 限制（合稱 PPA）。

## 設計考量
如 [[AI加速晶片概覽]] 所述，邊緣 AI 晶片（例如智慧型手機中的 NPU 或自駕車晶片）首要目標是提供實時的推理能力，同時將功耗降至最低。

## 關鍵技術
1. **深度量化**: 為了縮減模型大小和運算量，邊緣裝置常依賴 [[模型量化技術]]，將模型參數從 32-bit 浮點數轉換為 8-bit 甚至更低精度的整數。
2. **硬體加速器優化**: 針對特定常見的卷積層或神經網路架構進行硬體層級的深度優化，詳見 [[GPU與NPU架構比較]] 中的 NPU 部分。
3. **異質運算 (Heterogeneous Computing)**: 結合 CPU, GPU, NPU 和 DSP，根據不同任務的特性分配最合適的運算單元，以達到最佳能效。
