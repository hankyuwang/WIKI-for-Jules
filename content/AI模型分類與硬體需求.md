---
title: AI模型分類與硬體需求
level: intermediate
tags:
  - hardware
  - ai-models
  - transformer
  - cnn
  - moe
---

# AI 模型分類與硬體需求

本文旨在對當前主流的 AI 模型架構進行分類，並分析它們在運算、記憶體頻寬和通訊等方面的不同硬體需求。這對於在不同場景下選擇合適的 [[AI加速晶片架構概覽]] 至關重要。

## Prerequisites
* [[基礎計算機結構]]

## 1. 卷積神經網路 (CNN - Convolutional Neural Networks)

CNN 在電腦視覺 (CV) 領域取得了巨大成功。

*   **運算特徵**:
    *   計算高度密集，主要由卷積層組成。
    *   具有極高的資料局部性 (Data Locality) 和權重共享 (Weight Sharing) 特性。
*   **硬體需求**:
    *   **高運算力 (Compute-bound)**: 由於資料重複使用率高，CNN 模型通常是運算受限的。需要硬體提供強大的 MAC 陣列。
    *   **較低的記憶體頻寬需求**: 相較於其他模型，CNN 對記憶體頻寬的要求相對較低，因為資料可以在運算單元附近被有效緩存。
    *   適合硬體: GPU, 各種為卷積運算特化的 NPU。

## 2. 循環神經網路 (RNN - Recurrent Neural Networks)

RNN 曾經是自然語言處理 (NLP) 和序列資料分析的主力，但逐漸被 Transformer 取代。

*   **運算特徵**:
    *   具有時序相依性 (Sequential Dependency)，下一個時間步的計算依賴前一個時間步的結果。
    *   導致平行化程度較低，難以充分利用龐大的運算陣列。
*   **硬體需求**:
    *   **記憶體頻寬受限 (Memory-bound)**: 為了處理序列，需要頻繁地從外部記憶體載入權重和隱藏狀態，導致記憶體存取成為瓶頸。
    *   需要低延遲的記憶體存取機制。

## 3. Transformer 模型

Transformer 架構是目前大語言模型 (LLM) 和許多視覺模型的基礎，其核心是自注意力機制 (Self-Attention)。

*   **運算特徵**:
    *   包含大量的矩陣乘法 (Matrix-Matrix Multiplication, GEMM)。
    *   注意力機制的計算複雜度隨著序列長度 (Context Window) 呈二次方成長 ($O(N^2)$)。
*   **硬體需求**:
    *   **巨大的記憶體容量**: 需要儲存龐大的模型權重 (動輒數十億至數百億參數) 以及長序列產生的 KV Cache。
    *   **極高的記憶體頻寬**: 在推論 (Inference) 階段的生成過程 (Decoding/Autoregressive) 通常是 Memory-bound，因為每次生成一個 token 都需要載入所有的權重。
    *   **強大的通訊頻寬**: 訓練和推論大模型通常需要多卡甚至多節點協同工作 (Pipeline Parallelism, Tensor Parallelism)，因此節點間的網路頻寬 (如 NVLink, InfiniBand) 至關重要。

## 4. 混合專家模型 (MoE - Mixture of Experts)

為了在不顯著增加運算成本的情況下擴展模型參數，MoE 架構被廣泛應用。

*   **運算特徵**:
    *   稀疏啟動 (Sparse Activation): 每次前向傳播只有少數的專家 (Experts) 子網路被啟動。
*   **硬體需求**:
    *   **更極端的記憶體容量需求**: 模型總參數量極大。
    *   **動態路由和通訊開銷**: 需要將資料動態分發給不同的專家，這在分散式系統中會帶來顯著的 All-to-All 通訊負擔。硬體需要支援高效的通訊機制來掩蓋這部分延遲。
    *   **記憶體頻寬仍然是瓶頸**: 雖然運算量相對減少，但為了載入被選中專家的權重，依然需要巨大的記憶體頻寬。

## 結論

不同 AI 模型架構的演進推動了硬體架構的變革。從早期的 CNN 推動了針對卷積優化的硬體，到現在的 Transformer 和 MoE 對記憶體容量、頻寬以及高速互連技術提出了前所未有的挑戰。未來的 AI 晶片設計必須緊跟演算法的發展趨勢。
## 新最佳實務：MoE 與網路互連
隨著 MoE (Mixture of Experts) 模型 (如 DeepSeek, Mixtral) 的流行，**叢集網路互連 (Interconnect)** (如 NVLink, ICI) 變得比單晶片算力更重要。快速的專家路由與分發是避免延遲抖動的關鍵。
