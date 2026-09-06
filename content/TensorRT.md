---
title: TensorRT
level: intermediate
tags:
  - AI
  - TensorRT
  - Inference
  - NVIDIA
---

# TensorRT

摘要：TensorRT 是 NVIDIA 推出的高效能深度學習推論 (Inference) 引擎與 SDK，專門針對 NVIDIA GPU 進行極致優化，能大幅降低延遲並提升吞吐量。

## 先備知識 (Prerequisites)
- [[GPU]] : 了解圖形處理器與 AI 加速的關聯。
- [[模型量化技術]] : 了解降低模型精度以換取效能的技術。
- [[算子融合]] : 了解 Operator Fusion 原理。

## 已知事實與原理

TensorRT 的核心目標是「在特定的 NVIDIA GPU 上，將訓練好的模型跑得越快越好」。它主要透過以下幾種關鍵技術來達成：

1. **算子融合 (Layer & Tensor Fusion)**：將神經網路中的多個層（例如卷積層、Bias、ReLU 激勵函數）合併為單一的運算核心 (Kernel)。這極大地減少了 GPU 與記憶體之間頻繁的資料讀寫，突破了 [[AI記憶體瓶頸與解決方案]] 中的記憶體牆問題。
2. **精度校準與轉換 (Precision Calibration)**：支援將原本使用 FP32 訓練的模型，安全地轉換為 [[FP16]] 甚至 [[INT8]] 進行推論。透過校準演算法 (Calibration)，能確保在降低精度的同時，將精準度損失降到最低。
3. **核心自動調優 (Kernel Auto-Tuning)**：針對當前執行的具體 GPU 架構（例如 Ampere 或 Hopper），自動選擇最佳的演算法實作來執行特定的操作。
4. **動態張量記憶體管理**：優化記憶體配置，減少執行期間的記憶體佔用。

## 限制
- **硬體綁定**：高度綁定 NVIDIA 的 CUDA 生態系，無法跨平台至 AMD 或其他 ASIC 上運行。
- **模型相容性**：雖然支援多種框架（如 PyTorch, ONNX），但並非所有新奇的算子都能被 TensorRT 直接支援，可能需要撰寫自定義的 Plugin，增加了實作複雜度。

## 最佳實務
通常的開發流程是：使用 [[PyTorch]] 或 TensorFlow 訓練模型 $\rightarrow$ 匯出為 ONNX 格式 $\rightarrow$ 使用 TensorRT 讀取 ONNX 並針對目標部署的 GPU 進行編譯與優化 $\rightarrow$ 產生高度優化的 TensorRT Engine 檔案進行推論部署。

## 個人見解
隨著生成式 AI (如 LLM) 規模日益龐大，推論成本成為企業的主要痛點。TensorRT (以及後續發展的 TensorRT-LLM) 所代表的極致底層優化與量化策略，是決定次世代 AI 系統效能與商業可行性的關鍵勝負手。

## 方案與觀點分析

### 方案一：直接使用訓練框架推論
- **優點**：無須任何轉換，開發最快。
- **缺點**：效能最差，未經底層硬體最佳化，浪費算力與電力。
- **適用場景**：研發初期的快速驗證。

### 方案二：導入 TensorRT (FP16/FP32)
- **優點**：透過算子融合與 Kernel 優化，即可獲得顯著的效能提升與延遲下降。
- **缺點**：需處理模型格式轉換 (如轉為 ONNX) 與潛在的算子不支援問題。
- **適用場景**：多數需要上線服務的模型，對延遲有一定要求。

### 方案三：極致優化 - TensorRT INT8 量化
- **優點**：極致效能與能效，大幅降低記憶體頻寬需求，吞吐量最大化。
- **缺點**：需準備校準數據集 (Calibration Dataset) 進行校準，且有一定機率造成模型精度下降，除錯困難。
- **適用場景**：極高併發量的商業服務、資源受限的邊緣運算裝置。
