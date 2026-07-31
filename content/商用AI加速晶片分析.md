---
title: 商用 AI 加速晶片分析
level: advanced
tags:
  - npu
  - hardware
  - ai-accelerators
  - architecture
---

# 商用 AI 加速晶片分析

本頁面提供對當前主流商用 AI 加速晶片（包含 NVIDIA, Google TPU, AMD Instinct, Intel Gaudi, Apple ANE, Qualcomm Snapdragon Hexagon）的深入研究與分析。

## Prerequisites
- [[NPU架構探索]]
- [[基礎計算機結構]]

## 快速比較矩陣 (Structured Matrix)

| 廠商 | 晶片系列/型號 | 核心架構特色 | 互連技術 | 軟體生態系 (SDK) | 主要應用場景 |
| --- | --- | --- | --- | --- | --- |
| NVIDIA | H100 / B200 | Tensor Core, 異質運算 | NVLink, NVSwitch | CUDA, TensorRT | 雲端訓練、大型推論 |
| Google | TPU v5 / v5e | Systolic Array (脈動陣列) | ICI (Inter-Core Interconnect) | XLA, JAX, TensorFlow | 雲端訓練 (內部生態) |
| AMD | Instinct MI300X | CDNA 架構, Chiplet 設計 | Infinity Fabric | ROCm | 雲端訓練、HPC |
| Intel | Gaudi 3 | 矩陣數學引擎 (MME), 乙太網互連 | 整合 Ethernet (RoCE v2) | SynapseAI | 雲端訓練、高 CP 值推論 |
| Apple | ANE (A/M 系列) | 專用神經網路引擎, 統一記憶體 (UMA) | 晶片內匯流排 | Core ML | 終端裝置推論 (Edge AI) |
| Qualcomm | Snapdragon Hexagon | 向量擴充, 標量與張量加速器融合 | 內部高頻寬匯流排 | Qualcomm AI Engine Direct | 手機/IoT 終端推論 |

## 架構分析與模型映射 (SW/HW Co-design)

硬體架構與軟體的協同設計 (SW/HW Co-design) 是發揮 AI 加速器效能的關鍵。
- **NVIDIA Tensor Core**：透過將小塊矩陣乘法硬體化（例如 4x4 或 8x8 矩陣），軟體層面將 Transformer 模型中的大矩陣切割（Tiling）以對齊 Tensor Core。
- **Google TPU**：採用大規模的脈動陣列（Systolic Array），極度優化靜態計算圖。軟體端利用 XLA (Accelerated Linear Algebra) 編譯器進行算子融合 (Operator Fusion)，減少記憶體讀寫。
- **AMD CDNA**：透過 Chiplet 將多個運算晶粒與 HBM 封裝在一起，軟體上透過 ROCm 映射平行運算任務。

## SDK 設計哲學 (SDK Design Philosophies)

- **CUDA (NVIDIA)**：極致的控制力與龐大的社群。提供從底層 PTX 到高層 cuBLAS 的全面 API，是目前 AI 運算的業界標準。
- **XLA / JAX (Google)**：以編譯器為中心的設計。強調全域最佳化 (Global Optimization)，適合靜態圖和純函數式編程。
- **ROCm (AMD)**：開源與 CUDA 兼容性。努力打造類似 CUDA 的體驗 (HIP)，以降低開發者遷移成本。
- **Core ML (Apple)**：封裝複雜度。對開發者隱藏底層硬體 (CPU/GPU/ANE)，由系統自動分配工作負載以達最佳能效。

## 前沿瓶頸 (Frontier Bottlenecks)

### 記憶體牆 (Memory Wall)
隨著 LLM (如 GPT-4, Llama 3) 參數量爆炸，計算能力（FLOPs）的增長遠大於記憶體頻寬的增長。晶片往往處於等待資料的狀態 (Memory-bound)，而非計算狀態 (Compute-bound)。

### 互連技術 (Interconnect)
單一晶片無法容納巨大模型，必須依賴分散式系統。跨晶片、跨節點的通訊延遲成為瓶頸。NVLink 與 PCIe 的頻寬差異，以及乙太網路在叢集規模下的長尾延遲，是目前急需解決的互連難題。

## 新創晶片提案 (Startup Chip Proposals)

面對上述瓶頸，業界與新創提出了幾種顛覆性架構：
1. **SRAM-centric (以 SRAM 為中心)**：如 Groq 提出的 LPU 架構，完全捨棄 HBM，將模型與資料全部存放在超大容量的晶片內 SRAM 中，以獲取極低的延遲與超高頻寬。
2. **Wafer-scale (晶圓級封裝)**：如 Cerebras，直接將整片晶圓作為一個超大型晶片，內部具有極高頻寬的互連網路，藉此徹底打破傳統晶片間的通訊瓶頸。
3. **RISC-V Dataflow (基於 RISC-V 的資料流架構)**：利用開源且可高度客製化的 RISC-V 指令集，結合資料流 (Dataflow) 驅動的執行模式，取代傳統馮·紐曼架構的指令驅動，以提高運算資源的利用率並降低功耗。
