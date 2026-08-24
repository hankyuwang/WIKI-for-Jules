---
title: AI 晶片軟體堆疊與 SDK 設計
level: intermediate
tags:
  - ai-chip
  - software-stack
  - sdk
  - cuda
  - rocm
---

# AI 晶片軟體堆疊與 SDK 設計

硬體的效能上限由架構決定，但能發揮多少效能，則完全取決於軟體堆疊 (Software Stack) 與 SDK 的設計。這也是 NVIDIA 能夠稱霸 AI 領域的核心護城河。

## 1. 軟體堆疊的核心挑戰

當開發者使用 PyTorch 寫下一行 `C = torch.matmul(A, B)` 時，底下需要經過無數層的轉換才能在晶片上執行：
1. **Framework Layer**: PyTorch / JAX。
2. **Graph/Compiler Layer**: 將計算圖優化 (如算子融合 Operator Fusion)、記憶體分配。
3. **Kernel Library Layer**: 呼叫預先寫好、高度最佳化的矩陣乘法底層函數 (如 cuBLAS)。
4. **Driver/Runtime Layer**: 將指令與資料送到晶片，管理非同步執行與通訊 (DMA)。
5. **Hardware**: 實際執行。

## 2. 幾種主流的 SDK 設計哲學

### A. The "Kernel Library" Approach (NVIDIA CUDA)
NVIDIA CUDA 是最成功、也最龐大的生態系。它依賴大量工程師「手工打造」極致優化的底層函式庫。

*   **設計哲學**: 提供一套像 C++ 一樣靈活的底層語言 (CUDA C++)。對於常見操作 (Matmul, Convolution, Attention)，NVIDIA 提供官方手工榨乾硬體效能的 Library (cuBLAS, cuDNN, FlashAttention)。
*   **優勢**:
    *   **極致效能**: 手工寫的 Kernel 通常能達到硬體理論上限的 80%~90%。
    *   **靈活性極高**: 如果有全新的模型架構出現，開發者可以馬上用 CUDA 寫出新的 Kernel。
*   **劣勢**:
    *   **開發門檻極高**: 要寫出高效的 CUDA 程式碼，開發者必須深入了解 GPU 的硬體架構 (Warp, Shared Memory bank conflict, Memory coalescing)。
    *   **維護成本高昂**: 每出一代新硬體 (如 Hopper 到 Blackwell)，NVIDIA 都要花龐大資源重寫/優化這些 Library。

### B. The "Compiler" Approach (Google TPU XLA / TVM / MLIR)
與其讓人寫 Kernel，不如讓編譯器自動生成 Kernel。這是 Google TPU (XLA) 與許多新創晶片公司的選擇。

*   **設計哲學**: 開發者在 PyTorch/JAX 寫好高階圖形，編譯器 (Compiler) 負責分析整張圖，自動進行算子融合 (Fusion)、記憶體分配 (Tiling)，然後生成對應的硬體指令。
*   **優勢**:
    *   **硬體抽象化**: 開發者不需要懂底層硬體，換一顆新晶片，只要重新 Compile 即可。
    *   **全域優化 (Global Optimization)**: 編譯器可以看到整個模型，可以把多個小算子融合成一個大算子，避免頻繁讀寫 HBM，這點人類很難手工做到。
*   **劣勢**:
    *   **Fall-off-a-cliff 效能**: 如果模型裡有編譯器看不懂的奇葩算子，編譯器可能無法優化，甚至會退回到 CPU 執行，導致效能暴跌 (從 100 掉到 1)。這被稱為「效能懸崖」。
    *   **編譯時間長**: 每次模型架構改變 (甚至只是換個 Batch size) 可能都需要重新編譯 (JIT Compilation overhead)。

### C. The "Open Ecosystem" Approach (AMD ROCm / OpenAI Triton)
為了打破 NVIDIA 的壟斷，業界正積極推動開源標準。

*   **AMD ROCm**: 基本上是「摸著 NVIDIA 過河」。提供了 HIP (Heterogeneous-Compute Interface for Portability)，這是一個類似 CUDA 的介面，甚至有工具可以把 CUDA code 自動轉成 HIP code。目標是做到 Drop-in replacement。
*   **OpenAI Triton**: 這是一個介於 Python 與底層硬體間的語言/編譯器。開發者用 Python 語法寫 Triton 程式，Triton 編譯器會自動幫你處理麻煩的 Shared Memory 管理和 Thread 同步。
    *   **優勢**: 大幅降低了寫高效率 Kernel 的門檻。而且 Triton 支援 NVIDIA GPU，也逐漸支援 AMD 與其他硬體。
    *   **意義**: 這是軟體層面「去 CUDA 化」的最強大武器。

## 3. 自研 AI 晶片的軟體困境

如果今天有一家小公司做出了硬體指標 (TOPS, HBM) 碾壓 H100 的晶片，為什麼沒人買？
因為 **SDK 太難做**。

*   如果選擇 **A 路線 (手寫 Library)**：新創公司沒有幾千名軟體工程師來維護算子庫，無法支援千奇百怪的模型。
*   如果選擇 **B 路線 (純 Compiler)**：遇到客戶自創的怪異模型，Compiler 跑不動，客戶就會退貨。
*   **解法**：目前大部分新創 (如 Groq, Tenstorrent) 選擇高度依賴開源編譯器基礎建設 (如 MLIR)，結合硬體協同設計，盡量讓編譯器更容易為其硬體生成高效程式碼。

## 總結
硬體決定了 AI 加速器的地板，但 SDK 與軟體生態決定了天花板，以及客戶買不買單。在 CUDA 的統治下，Compiler (XLA/MLIR) 與中介層 (Triton) 成為其他玩家破局的唯一希望。
