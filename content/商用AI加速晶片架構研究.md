---
title: 商業 AI 加速晶片架構研究
level: intermediate
tags:
  - hardware
  - architecture
  - npu
  - ai-accelerator
---

# 商業 AI 加速晶片架構研究

## 先備知識 (Prerequisites)
- [[主要廠商架構分析]]
- [[GPU]]
- [[TPU]]

本篇筆記主要整理與探討目前市場上主流商業 AI 加速晶片的架構設計，包含其核心設計理念、記憶體階層架構，以及針對不同 AI 負載的特化設計。

## 1. NVIDIA 架構發展
NVIDIA 在 AI 加速領域佔據主導地位，其架構不斷演進以適應日益增長的大型語言模型（LLM）需求。
- **Hopper (H100)**：引入了第 4 代 Tensor Core，並新增了 Transformer Engine，支援 FP8 資料格式，大幅提升 LLM 的訓練與推論效率。
- **Blackwell (B200/GB200)**：採用第二代 Transformer Engine，進一步支援 FP4 及 FP6 格式，並透過高速 NVLink 串接多個 GPU，針對兆級參數模型設計。

## 2. Google TPU (Tensor Processing Unit) 架構
Google TPU 是專為 TensorFlow 與 JAX 打造的客製化 ASIC。
- TPU 的核心優勢在於其**脈動陣列 (Systolic Array)** 設計，這是一種高度優化的矩陣相乘單元，能有效減少資料搬移，提升吞吐量。
- **TPU v4/v5/Trillium**：透過強大的互連技術 (如 OCS - 光學電路交換)，允許在資料中心級別彈性配置拓撲結構，提供極高的擴展性。

## 3. AMD Instinct 系列架構
AMD 透過其 CDNA 架構，在資料中心市場提供強大的運算能力。
- **MI300 系列 (MI300X/MI300A)**：採用了先進的 Chiplet (小晶片) 封裝技術與 3D 堆疊，整合了龐大的 HBM (High Bandwidth Memory) 記憶體與 CPU/GPU 核心。這種高整合度的設計在處理需要極大記憶體頻寬的 AI 任務時展現出明顯優勢。

## 4. 記憶體架構與互連技術的關鍵性
除了運算核心 (Compute Cores) 的進化外，現代商業 AI 晶片也高度依賴以下技術：
- **HBM (高頻寬記憶體)**：提供 AI 模型所需的極大記憶體頻寬。
- **互連架構**：如 NVLink、Infinity Fabric 等，用於打破單一晶片的算力瓶頸，實現跨晶片的大規模平行運算。

## 延伸閱讀
- [[NPU架構探索]]：深入了解 NPU 軟硬體協同設計與基礎架構。



## 虛擬團隊補充說明：商業 AI 晶片架構的維護與生態系挑戰

研究商業 AI 晶片架構，除了關注硬體規格 (如 TOPS, TFLOPS, HBM 容量) 外，軟體生態系 (Software Ecosystem) 往往是決定勝負的關鍵。

1. **CUDA 的護城河**：Nvidia 最大的優勢不在於硬體本身，而在於其經過十多年打磨的 CUDA 生態系。大多數前沿的 AI 模型、框架 (PyTorch) 與優化庫 (如 FlashAttention) 都是首先 (甚至只) 針對 CUDA 進行最佳化。這使得其他硬體廠商 (如 AMD, Intel) 面臨極大的遷移成本。
2. **AMD 的 ROCm 追趕**：AMD 透過 ROCm 平台試圖打破 CUDA 的壟斷。透過將 PyTorch 編譯為相容於 AMD GPU 的程式碼，並大力發展 HIPIFY (將 CUDA 轉譯為 HIP) 等工具，AMD MI300X 在硬體規格上已能與 H100 匹敵，但在長尾的開源模型與特殊算子支援上，仍有追趕的空間。
3. **雲端廠商的自研晶片 (ASIC)**：如 Google TPU, AWS Trainium, Microsoft Maia。這類晶片針對特定運算 (如張量矩陣乘法) 進行極致優化，並透過專屬的編譯器 (如 Google 的 XLA) 將高階框架語法轉換為機器碼。這類架構犧牲了部分通用性，換取了在特定場景下極高的性價比與能效比。但缺點是，開發者可能需要針對其架構調整模型程式碼，存在一定的平台鎖定風險。
