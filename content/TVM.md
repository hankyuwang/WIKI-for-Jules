---
title: TVM
level: intermediate
tags:
  - AI
  - TVM
  - compiler
---

# TVM (Tensor Virtual Machine)

摘要：Apache TVM 是一個開源的跨硬體機器學習編譯器框架。它扮演著軟體框架 (如 [[PyTorch]]) 與底層各種異質硬體 (CPU, GPU, [[TPU]], NPU) 之間的橋樑，能自動將深度學習模型編譯、優化，並部署到任何硬體平台上。

## 核心原理與先備知識
在學習 TVM 之前，了解 [[AI加速晶片軟體堆疊與SDK設計]] 以及基本的運算單元 (如 [[MAC]]) 會有很大幫助。
隨著 AI 模型的演進，硬體架構也百花齊放。如果每一種新硬體都需要手動為模型撰寫優化的底層程式碼 (如 CUDA C++)，開發成本將極其高昂。
TVM 的核心理念是：
1. **中介表示 (Intermediate Representation, IR)**：將各種前端框架的模型轉換為統一的抽象語法樹 (Relay IR)。
2. **高階優化 (Graph-Level Optimization)**：在計算圖層級進行操作，例如 [[算子融合]] (Operator Fusion)，以減少記憶體存取次數。
3. **底層優化 (Tensor-Level Optimization)**：將高階圖轉換為底層張量運算 (TIR)，並針對特定硬體的暫存器大小、快取階層進行優化。

## AutoTVM 與自動排程
傳統上，為特定硬體 (如邊緣裝置的 [[NPU架構探索]]) 優化程式碼需要依賴極具經驗的工程師 (即 "Ninja Programmer")。
TVM 引入了基於機器學習的自動調優 (Auto-tuning) 技術：
- **AutoTVM**：透過定義搜尋空間，讓系統自動在目標硬體上反覆測試不同的優化策略 (如迴圈展開、Tile 大小)，找出最快的執行方案。
- **AutoScheduler (Ansor)**：進一步減少人工干預，無需手動撰寫優化模板，系統能從零開始自動生成高效能的程式碼。

## 應用場景與最佳實務
- **邊緣運算部署**：在資源受限的 [[邊緣運算AI晶片]] 或是 Raspberry Pi 上，TVM 能將模型體積壓縮並提升數倍執行速度，且無需依賴龐大的 Python 執行環境。
- **客製化硬體支援**：新創晶片公司常使用 TVM (結合其 BYOC - Bring Your Own Codegen 功能) 快速為自家的 AI 加速器建立軟體生態堆疊。

## 挑戰與未來發展
雖然 TVM 強大，但在面對動態形狀 (Dynamic Shape) 或是極其複雜的現代架構 (如 [[MoE]]) 時，編譯時間極長且搜尋難度高。未來，與 [[MLIR]] 的整合與互補，將是編譯器領域的重要發展方向。
