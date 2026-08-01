---
title: AI加速晶片架構概覽
level: intermediate
tags:
  - hardware
  - architecture
  - npu
  - gpu
  - tpu
---

# AI加速晶片架構概覽

本文旨在深入探討並比較當前主流 AI 加速晶片的硬體架構，主要聚焦於 GPU、TPU 以及 NPU (Neural Processing Unit)。我們將分析它們的設計理念、運算單元結構、記憶體階層以及各自適用的場景，幫助讀者建立對 AI 硬體底層運作的全局認知。

## Prerequisites
* [[基礎計算機結構]]
* [[NPU架構探索]]

## 1. 核心設計理念與架構對比

AI 加速晶片的核心目標是盡可能高效地處理深度學習中大量的平行矩陣運算 (Matrix Multiplication) 和張量操作 (Tensor Operations)。不同的晶片類型在架構上做出了不同的取捨。

### GPU (Graphics Processing Unit)
*   **設計初衷**: 最初為圖形渲染設計，強調高吞吐量的平行運算 (SIMT - Single Instruction, Multiple Threads)。
*   **架構特點**:
    *   擁有數以千計的輕量級運算核心 (CUDA Cores)。
    *   加入專門針對矩陣運算的硬體單元 (如 NVIDIA Tensor Cores)。
    *   非常依賴高頻寬記憶體 (HBM, High Bandwidth Memory) 來滿足巨大的資料吞吐需求。
    *   支援高度靈活的程式設計模型 (如 CUDA)，能適應各種不同的演算法。
*   **優勢**: 生態極其完善，軟體支援度最高，通用性強，是目前 AI 訓練 (Training) 的絕對主力。

### TPU (Tensor Processing Unit)
*   **設計初衷**: Google 專為機器學習 (特別是 TensorFlow 框架) 定制的 ASIC (Application-Specific Integrated Circuit)。
*   **架構特點**:
    *   核心是由大量的乘加單元 (MAC) 組成的**脈動陣列 (Systolic Array)**。
    *   資料在陣列內部流動計算，極大地減少了對外部記憶體的存取次數 (Data Reuse)。
    *   指令集針對矩陣運算高度最佳化 (CISC 風格的複雜指令，如一次執行一個大矩陣乘法)。
    *   通常配備大容量的晶片內建 SRAM (Software-Managed On-chip Memory) 作為緩衝區。
*   **優勢**: 在處理大規模密集矩陣運算時，具有極高的能效比 (TOPS/W) 和算力密度，非常適合雲端大型模型的訓練與推論。

### NPU (Neural Processing Unit)
*   **設計初衷**: 泛指針對神經網路運算特化的處理器，設計理念多樣，常見於邊緣運算 (Edge) 和行動裝置 (Mobile) SOC 中，部分雲端加速器也以此命名。
*   **架構特點**:
    *   設計高度彈性，通常包含針對特定操作 (如卷積、池化、啟動函數) 硬體化的加速單元。
    *   強調極致的低功耗設計，以滿足電池供電設備的限制。
    *   記憶體階層可能相對簡單，更依賴於模型壓縮 (如 [[模型量化技術]]) 和編譯器優化來減少記憶體頻寬需求。
*   **優勢**: 在受限的功耗和成本預算下，提供遠超傳統 CPU 的神經網路推論能力。

## 2. 記憶體階層與資料流 (Dataflow)

AI 運算的瓶頸往往不在運算單元 (Compute-bound)，而在於資料搬運 (Memory-bound)。記憶體頻寬 (Memory Bandwidth) 決定了算力能否被有效利用。

*   **GPU**: 依賴多層次的快取 (L1/L2 Cache) 和極高頻寬的 HBM。程式設計師需要花費大量心力透過軟體 (如 Shared Memory) 來最佳化資料存取模式。
*   **TPU / 脈動陣列架構**: 透過資料在 MAC 單元間的接力傳遞 (Systolic Dataflow)，最大化資料重複使用率。常使用軟體可控的 Scratchpad Memory 取代傳統的硬體 Cache，讓編譯器能更精準地排程資料搬運 (Software-Managed Memory)。

## 3. 演進趨勢與未來挑戰

*   **Chiplet 與 2.5D/3D 封裝**: 隨著摩爾定律放緩，為了突破單一晶片面積限制 (Reticle Limit)，未來的高效能 AI 晶片將越來越依賴先進封裝技術，將多個小晶片 (Chiplets) 互連起來。
*   **軟硬體協同設計 (Hardware/Software Co-design)**: 晶片架構設計必須與深度學習編譯器 (如 XLA, TVM) 和模型架構 (如 Transformer) 緊密結合。硬體提供更強大的專用指令，軟體負責挖掘最大的平行度和最佳的資料排程。
*   **支援稀疏性 (Sparsity) 和低精度運算**: 硬體層面支援結構化稀疏 (Structured Sparsity) 和更低精度 (如 FP8, INT4 甚至更低)，是進一步提升算力密度的關鍵方向。

## 小結

選擇何種 AI 晶片取決於具體的應用場景 (訓練 vs. 推論, 雲端 vs. 邊緣)、模型複雜度、功耗預算以及軟體生態的成熟度。理解這些底層架構的差異，是開發高效能 AI 系統的基石。