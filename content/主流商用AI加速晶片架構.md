---
title: 主流商用 AI 加速晶片架構
level: intermediate
tags:
  - hardware
  - ai-accelerator
  - gpu
  - tpu
---

# 主流商用 AI 加速晶片架構

## 摘要

本文章探討目前市場上最主流的三大商用 AI 加速晶片架構：NVIDIA GPUs、AMD Instinct 以及 Google TPUs。隨著大語言模型 (LLM) 與生成式 AI 的蓬勃發展，AI 硬體加速器的需求急遽增加。本文將分析這些架構的特點，並針對不同應用場景（例如：大規模模型訓練、邊緣推論、成本敏感的雲端部署），提出硬體選擇的解決方案與評估。

## Prerequisites

- [[基礎計算機結構]]
- [[NPU架構探索]]

## 1. NVIDIA GPUs 架構 (以 Hopper/Blackwell 為例)

NVIDIA GPU 是目前 AI 運算的主力，其架構特點在於強大的平行運算能力，並針對 AI 應用加入專用硬體。

*   **特點**:
    *   **Tensor Cores**: 專為深度學習矩陣運算優化的硬體單元，支援 FP16, BF16, FP8 等混合精度運算。
    *   **CUDA 生態系**: 最成熟的軟體堆疊，幾乎支援所有的深度學習框架 (PyTorch, TensorFlow)。
    *   **NVLink & NVSwitch**: 提供極高的 GPU 之間 (GPU-to-GPU) 的頻寬，這對於需要跨 GPU 的大規模模型 (如 LLM) 訓練至關重要。
    *   **Transformer Engine**: 針對 Transformer 架構的動態精度調整技術。

## 2. AMD Instinct 架構 (以 MI300X 為例)

AMD 藉由 CDNA 架構強勢挑戰 NVIDIA 的主導地位，主打高記憶體容量與頻寬。

*   **特點**:
    *   **CDNA 架構**: 專注於高效能運算 (HPC) 和 AI，移除圖形處理單元以最大化運算密度。
    *   **高 HBM 容量**: MI300X 具有極高的 HBM3 記憶體容量，能夠將更大的模型或更大的 Batch Size 放入單一 GPU 中，減少節點間通訊。
    *   **ROCm 軟體堆疊**: AMD 的開源軟體平台，近年來與 PyTorch 的相容性大幅提升，但生態系成熟度仍不及 CUDA。
    *   **Infinity Fabric**: 用於連結 CPU 與 GPU，以及 GPU 與 GPU，提供高速傳輸。

## 3. Google TPUs 架構 (Tensor Processing Units)

Google TPU 是專為機器學習工作負載（尤其是 TensorFlow 與 JAX）量身打造的特殊應用積體電路 (ASIC)。

*   **特點**:
    *   **脈動陣列 (Systolic Array)**: TPU 的核心運算單元，能以極高的效率執行密集的矩陣乘法，功耗表現極佳。
    *   **Pod 級別擴展 (TPU Pods)**: 透過專屬的 3D Torus 網路將上千顆 TPU 連結，提供極大的線性擴展能力。
    *   **軟體綁定**: 深度整合 Google Cloud 以及 TensorFlow/JAX/PyTorch/XLA 編譯器。
    *   **HBM (High Bandwidth Memory)**: 近期的 TPU 架構也導入 HBM 以解決 Memory Wall 問題。

---

## 硬體選擇方案 (Solution Approaches)

針對不同的 AI 工作負載，以下提供三種硬體架構選擇方案，並分析其優缺點。

### 方案 A: NVIDIA GPU 叢集 (預設選項)

以 NVIDIA H100/A100 等 GPU 建立運算叢集，適用於多數企業與研究機構的標準作法。

*   **優點 (Pros)**: 生態系最成熟、開箱即用、除錯資源豐富、人才招募容易。幾乎所有的開源模型都能直接在 CUDA 上運行。
*   **缺點 (Cons)**: 硬體採購成本極高、交期可能很長、容易被單一廠商綁定 (Vendor Lock-in)。
*   **成本 (Costs)**: 初期硬體採購成本最高（硬體溢價），營運階段功耗成本高。
*   **維護性 (Maintainability)**: 維護容易，社群支援強大，有豐富的驅動程式與工具鏈。
*   **風險 (Risks)**: 供應鏈短缺風險、地緣政治限制風險。

### 方案 B: Google TPU Cloud (雲端原生方案)

直接使用 Google Cloud 上的 TPU 資源，適合已經採用 JAX 或 TensorFlow 的團隊，或是從頭訓練大型基礎模型的任務。

*   **優點 (Pros)**: 無需管理硬體、大規模網路 (TPU Pods) 效率極高、性價比通常優於雲端 GPU (針對特定框架)。
*   **缺點 (Cons)**: 強烈綁定 Google Cloud Platform，軟體靈活性較低，若使用不熟悉的框架 (如早期 PyTorch) 效能可能大打折扣。
*   **成本 (Costs)**: 只有營運成本 (OpEx)，無初期硬體採購成本 (CapEx)。依使用時間計費。
*   **維護性 (Maintainability)**: 硬體免維護。軟體維護取決於開發團隊對 XLA 與相關框架的熟悉度。
*   **風險 (Risks)**: 雲端供應商鎖定 (Cloud Vendor Lock-in)，若架構需要遷移至地端 (On-premise) 將面臨巨大困難。

### 方案 C: AMD Instinct (高性價比挑戰者)

採用 AMD MI300X 等加速器，適用於推論 (Inference) 階段，或是對記憶體容量需求極高的大型模型。

*   **優點 (Pros)**: 記憶體容量與頻寬優勢明顯，硬體性價比 (Performance/Dollar) 通常高於 NVIDIA，供應鏈來源較豐富。
*   **缺點 (Cons)**: ROCm 軟體生態系相對不穩定，遇到罕見錯誤時難以找到解答，舊有 CUDA 程式碼遷移有成本。
*   **成本 (Costs)**: 硬體採購成本中等（低於 NVIDIA 同級產品），擁有成本 (TCO) 較具競爭力。
*   **維護性 (Maintainability)**: 維護難度較高，需要投入工程資源優化軟體堆疊與解決相容性問題。
*   **風險 (Risks)**: 軟體生態系成熟度不足的風險，可能導致專案開發時程延宕。
