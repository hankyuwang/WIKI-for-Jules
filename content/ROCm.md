---
title: ROCm
level: intermediate
tags:
  - AI
  - ROCm
  - AMD
---

# ROCm (Radeon Open Compute)

摘要：ROCm 是 AMD 推出的開源運算軟體平台，旨在對標 NVIDIA 的 CUDA，為 AMD 的 GPU 提供高效能計算（HPC）與人工智慧（AI）的軟硬體橋樑，持續完善其生態以打破單一廠商壟斷。

## Prerequisites
- [[GPU架構與AI加速]]
- [[商業AI加速晶片架構]]
- [[CUDA]]

## 什麼是 ROCm？
長期以來，NVIDIA 透過 [[CUDA]] 建立起深厚的護城河，讓開發者難以轉移到其他硬體。為了打破這個僵局，AMD 推出了 ROCm (Radeon Open Compute)。它不僅僅是一個驅動程式，而是一整套包含編譯器、數學函式庫、分析工具的完整開源生態系統。

ROCm 的目標是讓深度學習框架（如 [[PyTorch]]、[[TensorFlow]]）能夠無縫地在 AMD 硬體（如 AMD Instinct 系列）上運行。

## ROCm 的核心元件
1. **HIP (Heterogeneous-Compute Interface for Portability)**: 這是 ROCm 最關鍵的武器。HIP 是一種 C++ 方言，語法與 CUDA C++ 極度相似。更重要的是，AMD 提供了 `hipify` 工具，可以自動將現有的 CUDA 程式碼轉換為 HIP 程式碼。這大幅降低了開發者將軟體移植到 AMD 平台的門檻。
2. **MIOpen**: 相當於 NVIDIA 的 cuDNN，是一個高度優化的深度學習原始操作（Primitives）函式庫，提供卷積、池化、啟動等底層加速。
3. **rocBLAS**: 相當於 cuBLAS，提供高效能的基礎線性代數運算（BLAS）。
4. **RCCL**: 相當於 NCCL，用於多 GPU 之間的高效通訊與同步，是分散式訓練的基礎。

## ROCm 與開源生態系的整合
隨著 AI 模型規模日益龐大，單一廠商的優化已不足夠，開源編譯器與框架變得更加重要。
- **PyTorch 支援**: ROCm 目前已成為 PyTorch 官方正式支援的後端之一，開發者幾乎不需要修改程式碼即可在 AMD GPU 上訓練模型。
- **Triton 與 OpenAI**: OpenAI 開發的 [[Triton]] 語言也積極支援 ROCm，這意味著許多基於 Triton 撰寫的高效能算子（如 FlashAttention）可以直接在 AMD 硬體上跑出優異效能。

## 挑戰與未來發展
儘管進步神速，ROCm 仍面臨一些挑戰：
- **長尾效應與生態深度**: 雖然主流框架與大模型支援良好，但許多小型的、實驗性的 AI 專案或特定的 CUDA 函式庫依然難以完美移植。
- **硬體相容性**: ROCm 主要針對 AMD 的企業級產品（Instinct CDNA 架構）優化最好，而在消費級顯示卡（RDNA 架構）上的支援度與穩定性仍有待提升。
