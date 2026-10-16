---
title: Tensor Core
level: beginner
tags:
  - hardware
  - gpu
  - tensor-core
---

# Tensor Core (張量核心)

> Tensor Core 是由 NVIDIA 引入的一種專門用來加速深度學習中矩陣乘法運算 (Matrix Multiplication) 的特殊硬體單元。它是現代 AI 晶片能處理龐大運算的關鍵秘密。

## 初學者導覽：把 Tensor Core 想像成超級算盤
如果你需要計算成千上萬個數字的相乘與相加，傳統的處理器（像是 CPU 或是早期的 GPU 核心）就像是一般計算機，每次只能算兩個數字的乘積，然後再加起來。

而 **Tensor Core** 就像是一個特別設計的「超級算盤」，它可以一次把一個小網格（例如 4x4 的矩陣）裡所有的數字同時相乘並相加，並且在極短的時間（單一時脈週期）內完成。因為 AI 模型（特別是深度學習）底層幾乎全都是矩陣乘法，這種專門的硬體單元讓 AI 訓練與推論的速度發生了飛躍性的提升。

## Tensor Core 的演進與現代架構
Tensor Core 首次出現在 早期 Volta (現已演進至 Hopper/Blackwell) 架構中，隨後的每一代 NVIDIA 架構都對它進行了升級：
- **混合精度運算 (Mixed Precision)**：Tensor Core 允許使用較低精度（如 [[FP16]]、[[BF16]]）進行乘法，然後用較高精度（如 FP32）來累加結果，兼顧了速度與準確性。
- **最新演進**：在最新的 Hopper 和 Blackwell 架構中，Tensor Core 支援了更低精度的運算格式（如 [[FP8]] 甚至是 FP4），並加入了 **Transformer Engine**，專門針對當下主流的 [[Transformer]] 與大型語言模型 (LLM) 進行了優化。

## 與傳統核心的比較
相較於傳統 GPU 用來處理圖形和通用計算的 CUDA Core，Tensor Core 犧牲了通用性，將晶片的空間全數押注在執行單一的、但也是 AI 最需要的運算上。這與 Google [[TPU]] 裡的 [[Systolic Array]] (脈動陣列) 有異曲同工之妙。

## 延伸閱讀
- 若想了解 GPU 的整體架構：[[GPU運算架構]]
- 關於量化對運算的影響：[[Quantization]]
