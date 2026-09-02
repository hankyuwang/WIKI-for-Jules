---
title: PyTorch
level: beginner
tags:
  - AI
  - PyTorch
  - framework
---

# PyTorch

摘要：PyTorch 是目前學術界與工業界最主流的深度學習框架。以其動態計算圖 (Dynamic Computation Graph)、直覺的 Pythonic 設計與強大的硬體加速生態圈著稱。

## 核心特色與先備知識
要理解 PyTorch 的運作，需要具備基本的 [[深度學習運算原理]] 與 [[反向傳播]] 知識。
- **動態計算圖 (Eager Execution)**：傳統框架 (如早期的 [[TensorFlow]]) 採用靜態圖，必須先定義完整的計算流程才能執行。PyTorch 則採用動態圖，運算圖在每一次前向傳播 (Forward pass) 時動態生成，這使得除錯 (Debugging) 如同寫一般 Python 程式一樣簡單，極大促進了 AI 研究的發展。
- **張量運算 (Tensor)**：PyTorch 的核心資料結構，類似 NumPy 的多維陣列，但原生支援 GPU 上的硬體加速運算。

## 與硬體加速器的整合
PyTorch 的成功離不開其背後對各類 [[AI加速晶片概覽]] 的深度支援：
- **CUDA 整合**：原生深度整合 NVIDIA 的 [[CUDA]] 與 [[cuDNN]]，使其能在 GPU 上獲得極致的效能。
- **XLA 擴展**：透過 PyTorch/XLA，模型可以被編譯並在 Google [[TPU]] 上高效執行。
- **自研加速晶片**：近年來，各家 AI 晶片廠 (如 AMD 的 [[ROCm]]、Apple 的 MPS) 均投入大量資源開發軟體堆疊，以確保能完美對接 PyTorch 生態，這被視為硬體成功的「入場券」。

## 效能優化與進展
儘管動態圖易於開發，但在生產環境佈署時可能面臨效能瓶頸。PyTorch 提出了幾種解決方案：
- **TorchScript**：將動態圖轉換為靜態圖，以便在沒有 Python 執行環境 (如 C++ 後端) 的邊緣裝置上運行。
- **PyTorch 2.0 (torch.compile)**：引入了全新的編譯器後端。利用 [[Triton]] 將高階操作直接編譯為極致優化的 GPU Kernel，在不改變開發者習慣的前提下，大幅提升了訓練與推論的效能。

## 總結
PyTorch 不僅僅是一個軟體工具，它定義了現代 AI 模型與底層硬體 ([[GPU]]、[[NPU架構探索]]) 互動的標準介面。理解 PyTorch 的底層優化，對於理解 AI 軟硬體協同設計至關重要。
