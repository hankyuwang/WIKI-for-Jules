---
title: AI加速晶片研究總覽
level: beginner
tags:
  - ai-accelerator
  - overview
---

# AI加速晶片研究總覽

本系列文章旨在全面探索與分析當前AI加速晶片的架構、軟體生態、以及未來的挑戰，並針對小團隊提供自研晶片的策略建議。

## 研究主題清單

- [[主流AI加速晶片架構與應用]]：分析 NVIDIA (Hopper/Blackwell)、Google TPU、AMD (MI300)、Groq 及 Apple ANE 等架構特性，詳細比較 ISA、Memory/SRAM/Cache、DMA、TOPS 與目標市場。
- [[AI模型分類與硬體架構關聯]]：解析不同模型（LLM Dense、MoE、CNN/YOLO、Mamba/SSM）的硬體瓶頸與需求，包括 Memory Bound、Compute Bound 及 Network Bound 等問題。
- [[AI晶片軟體堆疊與SDK設計]]：比較 CUDA（手寫 Kernel）、XLA/MLIR（編譯器基礎）與開放生態系（Triton/ROCm）等軟體開發堆疊。
- [[前沿技術挑戰與瓶頸]]：探討 Memory Wall（記憶體牆）、Power Wall（功耗牆）、Interconnect Wall（互連牆）以及軟硬體協同設計的極限。
- [[小團隊自研AI晶片策略]]：給予小團隊的自研策略建議，包含避開雲端/LLM紅海市場，專注 Edge/DSA，利用開源編譯器（MLIR/TVM），並採用 SRAM-centric 與 Systolic Array 架構配合積極量化（Quantization）。
