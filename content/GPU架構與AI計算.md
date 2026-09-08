---
title: GPU架構與AI計算
level: intermediate
tags:
  - GPU
  - AI Accelerator
  - Parallel Computing
---

# GPU架構與AI計算

圖形處理單元（GPU）由於具備大量核心，特別擅長處理高度平行的運算任務，這使其成為現代人工智慧發展的基石。本文探討 GPU 如何適應並加速 AI 計算。

## Prerequisites
- [[AI加速晶片概述]]
- [[基礎計算機結構]]

## GPU 的核心優勢
相較於 CPU 的少量高效能核心，GPU 擁有數以千計的較小核心。這種架構非常適合深度學習中的矩陣乘法與卷積運算，這些運算可以輕易地被拆分並平行處理。

## Tensor Core 與 AI 專屬優化
NVIDIA 等廠商在近代 GPU 中引入了 Tensor Core，這是專門為深度學習設計的運算單元。Tensor Core 可以在單一指令中完成 4x4 的矩陣乘加運算（Mixed Precision，例如 FP16 與 FP32 混合），大幅提升了吞吐量。此外，為了降低顯存壓力與加速運算，通常會結合 [[模型量化技術]]。

## 記憶體頻寬與互連技術
AI 訓練的瓶頸往往在於數據傳輸。因此，高頻寬記憶體（HBM, High Bandwidth Memory）和 NVLink 等高速互連技術成為現代 AI GPU 的標準配置。

## 在不同場景中的應用
GPU 主要主導雲端的模型訓練（Training）與大規模推理（Inference）。然而，在邊緣端，通常會考慮功耗更低的解決方案，詳見 [[邊緣運算AI晶片]] 與 [[NPU架構探索]]。

## 5分鐘了解 GPU 在 AI 運算中的角色 (補充說明)
GPU 最初是為了圖形渲染而設計，但其高度平行的架構完美契合了深度學習中的矩陣乘法運算。與 CPU 擁有少量高效能核心不同，GPU 擁有數以千計的較小核心，可以在同時處理大量的數據流（Data-parallelism）。這使得它在訓練（Training）與推理（Inference）階段都能提供極高的吞吐量。

## 核心技術：Tensor Core 與 SIMT (補充說明)
現代 AI GPU（如 NVIDIA 的 Volta, Ampere, Hopper 架構）引入了專門為深度學習設計的運算單元：**Tensor Core**。
- **Tensor Core** 可以在單一指令週期內完成 4x4 或更大的矩陣乘加運算（MAC），並且支援混合精度（Mixed Precision，例如使用 [[FP16]] 或 [[BF16]] 進行乘法，使用 FP32 進行累加），這在保證模型精度的同時大幅提升了運算速度。
- 此外，GPU 採用單指令多執行緒（[[SIMT]]）架構，多個執行緒同時執行相同的指令但處理不同的數據，極大地提升了資源利用率。為了降低記憶體帶寬壓力，通常會結合 [[模型量化技術]]（如 [[INT8]] 或 [[FP8]]）。

## 記憶體頻寬與互連技術 (Memory and Interconnect) (補充說明)
AI 模型的參數與中間結果（Activation）龐大，經常遇到「記憶體牆（Memory Wall）」的挑戰。高頻寬記憶體（[[HBM]]）的應用是現代 GPU 的標準配置，它透過 2.5D/3D 封裝技術與 GPU 核心靠攏，提供 TB/s 級別的頻寬。
為了支援大規模叢集運算，節點內的 GPU 通常透過 [[NVLink]] 或 [[PCIe]] 進行高速互連，而節點間則依賴 [[InfiniBand]] 或 [[RoCE]] 網路標準進行 RDMA 傳輸。

## 各場景應用與硬體選擇 (補充說明)
- **雲端訓練與超大型模型推理**：主要依賴 NVIDIA H100、A100 或 AMD MI300X，這類硬體成本高且耗能大，但能提供絕對的算力優勢。
- **邊緣運算**：在功耗受限的環境下，GPU 會被精簡，或採用其他解決方案。詳見 [[邊緣運算AI晶片]] 與 [[NPU架構探索]]。
