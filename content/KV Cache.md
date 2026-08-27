---
title: KV Cache (Key-Value Cache)
level: intermediate
tags:
  - transformer
  - llm
  - memory
---

# KV Cache (Key-Value Cache)

摘要：KV Cache 是提升大型語言模型 (LLM) 推論速度的關鍵優化技術。透過暫存先前的計算結果，避免在生成新字詞時進行重複計算，但這也帶來了巨大的記憶體頻寬挑戰。

## Prerequisites
- [[Transformer]]
- [[Prefill]]
- [[Decode]]

## 什麼是 KV Cache？

在 Transformer 架構中，模型的文本生成是一個**自回歸 (Autoregressive)** 的過程。也就是說，模型必須根據之前生成的所有文字，來預測下一個文字。

如果沒有優化，當模型要生成第 $N$ 個字時，它必須重新計算第 $1$ 到第 $N-1$ 個字的注意力 (Attention) 權重。這種做法的時間複雜度是 $O(N^2)$，效率極低。

為了加速這個過程，**KV Cache 技術被引入**。在注意力機制中，運算涉及 Query (Q)、Key (K) 和 Value (V) 矩陣。由於先前已生成的文字其 K 和 V 的值是固定不變的，我們可以在記憶體中把這些 K 和 V 矩陣儲存（Cache）起來。

當生成下一個字時，我們只需要計算**當前新字的 Q**，並將其與 Cache 中**所有過去的 K 和 V** 進行運算即可。

## 對硬體的影響與挑戰

> **虛擬團隊教育員補充**：把 KV Cache 想像成你在做筆記。每次寫新句子時，你不需要重頭把整本書讀一遍，只要看你之前做好的筆記 (Cache) 就好。這雖然省時間，但你的書桌 (記憶體) 空間很快就會被筆記塞滿。

1. **記憶體容量危機 (Memory Capacity Crisis)**
   - 隨著生成文本的長度（Context Length）增加，KV Cache 佔用的記憶體會線性成長。對於千億參數模型與超長上下文，KV Cache 的大小甚至可能超過模型權重本身。

2. **記憶體頻寬瓶頸 (Memory Bandwidth Bottleneck)**
   - 在生成階段 (Decode phase)，每一次生成新的 Token，硬體都必須將龐大的 KV Cache 從主記憶體（如 HBM）載入到運算單元（SRAM）中。這使得推論過程變成嚴重的 **Memory-bound (受限於記憶體頻寬)** 問題。

## 虛擬團隊補充說明：KV Cache 的記憶體容量挑戰

> **教育員白話文解釋**：想像你在聽一場演講並做筆記。一開始，你的筆記本（記憶體）還有很多空白。但隨著演講（Context Length）越來越長，你做的筆記（KV Cache）也越來越多。很快地，整本筆記本都被寫滿了！如果筆記本爆了，你就無法再記下任何新的東西。這就是大型語言模型在面對超長文本時，KV Cache 會把記憶體撐爆的原因。

**為什麼 KV Cache 容量是個大問題？**

在自回歸生成的過程中，為了不重複計算過去已經生成的 Attention 權重，模型會將每一層神經網路中，所有歷史 Token 的 Key 和 Value 矩陣儲存在 GPU 的記憶體中。

對於千億級參數的模型（如 Llama 3 70B）或是超大 Context Length（如 128k 或 1M tokens）的應用場景，KV Cache 佔用的記憶體容量甚至會遠大於模型權重本身。這不僅限制了單一 GPU 能處理的最大文本長度，也極大地限制了 Batch Size（能同時服務的使用者數量），進而影響整體的推論吞吐量與成本效益。

為了解決這個「記憶體容量危機」，業界採用了如 **PagedAttention** 等系統級優化技術，將 KV Cache 像作業系統管理虛擬記憶體一樣，切割成分頁並動態分配，大幅減少了記憶體碎片的浪費。

## 解決方案與最佳實務
為了緩解 KV Cache 帶來的瓶頸，業界提出了多種優化方法：
- **架構層面**：採用 Multi-Query Attention (MQA) 或 Grouped-Query Attention (GQA) 來減少需要儲存的 KV Head 數量。
- **系統層面**：使用 PagedAttention (如 vLLM 框架所採用)，將 KV Cache 分頁管理，解決記憶體碎片化問題。
- **硬體層面**：依賴更高頻寬的 [[HBM 高頻寬記憶體技術]]。
