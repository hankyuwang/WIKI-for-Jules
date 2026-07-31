---
title: GPU 架構與演進
level: intermediate
tags:
  - gpu
  - hardware
  - architecture
---

# GPU 架構與演進

圖形處理器 (Graphics Processing Unit, GPU) 原本是為了處理電腦圖形渲染而設計的硬體。由於圖形渲染需要處理大量的像素點，這本質上是高度平行的數學運算，使得 GPU 天生具備強大的平行計算能力。

## 從圖形渲染到通用計算 (GPGPU)

早期的 GPU 只能透過特定的圖形 API 進行程式設計。直到 NVIDIA 推出 CUDA (Compute Unified Device Architecture) 架構，讓開發者可以使用 C/C++ 等通用程式語言來編寫在 GPU 上執行的程式，GPU 才真正轉變為通用計算加速器 (GPGPU)。這成為了後來深度學習爆發的硬體基礎。

## 現代 AI GPU 的關鍵架構特徵

隨著 AI 工作負載的增加，GPU 在架構上也針對 AI 進行了許多演進與優化：

### 1. 張量核心 (Tensor Cores)
傳統的 CUDA 核心主要處理單精度或雙精度浮點數的純量運算。為了加速深度學習中最常見的矩陣乘法累積 (MAC) 運算，NVIDIA 在 Volta 架構中首次引入了 Tensor Cores。Tensor Cores 可以在一個時脈週期內完成小矩陣的乘加運算（例如 4x4 矩陣），大幅提升了 AI 訓練與推論的吞吐量。後續架構也支援了更低精度的運算（如 FP16, INT8, FP8），這與[[模型量化技術]]的發展息息相關。

### 2. 高頻寬記憶體 (HBM)
AI 運算往往受限於記憶體頻寬，即所謂的「記憶體牆」問題（詳見 [[AI加速晶片的記憶體架構]]）。高階資料中心 GPU 採用了 HBM (High Bandwidth Memory)，透過 2.5D/3D 封裝技術，將記憶體晶片與 GPU 核心靠得很近，提供極高的資料傳輸速率。

### 3. 多晶片互連技術 (NVLink)
在訓練大型語言模型時，單一 GPU 的算力與記憶體已不夠用，需要多顆 GPU 協同運算。NVIDIA 開發了 NVLink 高速互連技術，讓 GPU 之間可以直接進行高速資料交換，繞過 PCIe 頻寬的瓶頸，實現了大規模的叢集運算。

## 總結
GPU 憑藉其強大的軟體生態系統（如 CUDA, cuDNN）和持續演進的硬體架構，目前在 AI 訓練和推論領域佔據統治地位。然而，相對於專用晶片，GPU 的功耗較高。

回顧整體 AI 晶片生態，可參考：[[AI加速晶片總覽]]。
