---
title: 主要商用AI加速晶片架構分析
level: advanced
tags:
  - npu
  - hardware
  - architecture
  - accelerator
---

# 主要商用AI加速晶片架構分析

本頁面探討目前市場上主流的商用 AI 加速晶片（Accelerator Chips）之硬體架構，包含 NVIDIA B200/H100、AMD MI300X、Google TPU v5p / v6 Trillium 以及 AWS Trainium2。

## Prerequisites
- [[NPU架構探索]]
- [[深度學習運算原理]]

## 1. NVIDIA B200 (Blackwell) & H100 (Hopper)
NVIDIA 的 GPU 是目前 AI 訓練與推理的主流平台。
- **架構特點**：
  - **H100** 引入了 Hopper 架構，最主要的革新是 Transformer Engine，能在 FP8 和 FP16 之間動態切換，大幅提升大型語言模型（LLM）的訓練與推理速度。
  - **B200** 採用最新的 Blackwell 架構，設計上使用了第二代 Transformer Engine，進一步支援 FP4 與 FP6 等低精度運算，並利用 NVLink Switch 技術實現超大規模的 GPU 互連。
- **記憶體與互連**：搭載高頻寬的 HBM3/HBM3e，具備極高的記憶體頻寬，以及 NVLink 帶來的高速點對點互連。

## 2. AMD MI300X
AMD MI300X 是針對生成式 AI 和高效能運算 (HPC) 設計的加速器。
- **架構特點**：
  - 採用 CDNA 3 架構，強調將 CPU 與 GPU 的運算核心（在 MI300A 中）或是純 GPU 模組結合。MI300X 則是一款純 GPU 的加速器。
  - 大幅提升了記憶體容量與頻寬，搭載了高達 192GB 的 HBM3，使其在運行極大型 LLM 時可以減少跨節點通訊的瓶頸。
- **優勢**：在單一節點內可容納更大的模型，降低了整體系統建置的複雜度。

## 3. Google TPU v5p / v6 Trillium
Google 的 Tensor Processing Unit (TPU) 是專為 TensorFlow 和 JAX 等機器學習框架深度最佳化的 ASIC 晶片。
- **架構特點**：
  - 採用了高度最佳化的脈動陣列 (Systolic Array) 來執行矩陣乘法。
  - v5p 版本強調了單晶片效能的提升以及更強的互連能力，利用光學互連 (Optical Circuit Switches, OCS) 技術構建超大規模的超級電腦叢集 (Pod)。
- **生態系限制**：通常僅在 Google Cloud 上提供，適合深度綁定 Google 雲端生態與 JAX/XLA 的大型模型訓練。

## 4. AWS Trainium2
AWS Trainium2 是 Amazon 專為深度學習訓練設計的客製化晶片。
- **架構特點**：
  - 針對大規模模型（如包含千億至兆級參數的模型）進行最佳化，支援多種資料型態（包含 FP32、TF32、BF16、FP16、FP8 等）。
  - 整合了 Neuron SDK，能支援 PyTorch 與 TensorFlow，並透過 NeuronCore Pipeline 進行模型平行化運算。
  - 配置了高頻寬的互連網路 EFA (Elastic Fabric Adapter) 來進行節點間的擴展。
- **應用場景**：專注於為 AWS 用戶提供高性價比的 AI 訓練基礎設施。

## 架構比較與方案分析

對於希望建置 AI 基礎設施的企業，我們提出以下三種解決方案：

### 方案 A：採用 NVIDIA 解決方案 (B200/H100)
- **優點**：軟體生態系 (CUDA) 最為成熟，幾乎所有開源模型與框架都提供 First-class 支援。開發成本極低。
- **缺點**：硬體取得成本極高，且可能面臨供貨短缺。
- **風險與維護性**：生態系穩定，維護性高，但容易被單一廠商硬體綁定 (Vendor Lock-in)。

### 方案 B：採用 AMD MI300X
- **優點**：提供極大的 HBM 容量，單一節點可部署更大模型。具備高性價比潛力。
- **缺點**：ROCm 軟體生態系雖然正在快速追趕，但相較於 CUDA 仍有部分落差，部分冷門套件支援可能不完善。
- **風險與維護性**：需要較強的底層軟體工程能力來處理潛在的相容性問題。

### 方案 C：採用雲端原生自研晶片 (TPU / Trainium)
- **優點**：在對應的雲端平台上擁有最佳的性價比 (Cost-performance ratio)。基礎設施管理交由雲端供應商負責。
- **缺點**：必須綁定特定的雲端供應商（GCP 或 AWS），且若原先程式碼高度依賴 CUDA，則需要進行程式碼改寫。
- **風險與維護性**：依賴供應商的軟體堆疊（如 XLA 或 Neuron SDK），遷移至其他硬體的成本極高。

## 未來研究方向
- **模型量化技術與硬體架構的結合**：探討 FP4 / INT4 如何在實際硬體上達到 Zero-overhead 的運算轉換。
- **跨平台編譯器技術**：例如 OpenAI Triton 或 MLIR 等開源編譯器如何降低對單一硬體廠商 (CUDA) 的依賴。
