---
title: GDDR 與 AI 推理應用
level: intermediate
tags:
  - hardware
  - memory
  - GDDR
---

# GDDR 與 AI 推理應用

## 摘要
Graphics Double Data Rate (GDDR) 記憶體最初專為圖形處理單元（GPU）渲染遊戲畫面所設計，具備極高的單引腳頻寬（Pin Bandwidth）。隨著 AI 模型逐漸普及，特別是在終端裝置（Edge Devices）與主流伺服器中的 AI 推理（Inference）應用，GDDR 憑藉其相對 HBM 更低的成本與成熟的封裝技術，成為許多中高階 AI 加速晶片（如特定 NPU 與平價 AI GPU）的首選記憶體架構。本文將探討 GDDR 在 AI 推理場景下的設計權衡與挑戰。

## 設計觀點與分析

### 觀點一：採用 GDDR 作為平價/中階 AI 加速卡的記憶體標準
在不需要頂級訓練算力的場景（如企業內部小規模推理伺服器或自駕車邊緣運算平台），採用標準的 GDDR（如 GDDR6 或 GDDR7）取代 HBM。

*   **優點 (Pros)**：提供極具競爭力的頻寬（GDDR6 頻寬可達數百 GB/s），且採用成熟的 PCB 佈線封裝，完全免除昂貴且良率挑戰大的 2.5D 矽中介層（Silicon Interposer）製程。
*   **缺點 (Cons)**：單晶片容量較小（通常為 16Gb 或 24Gb），要達成大容量需要極寬的匯流排（如 256-bit 或 384-bit），佔用大量電路板面積。
*   **成本 (Costs)**：硬體建置成本顯著低於 HBM 系統，且多家記憶體大廠穩定供貨，供應鏈風險低。
*   **維護性 (Maintainability)**：使用標準 SMT（表面貼焊）製程打件，損壞時在工程上（如原廠維修）有機會針對單顆記憶體進行替換，維護彈性較高。
*   **風險 (Risks)**：隨著大語言模型（LLM）的參數與 Context Window 持續增長，GDDR 的總容量上限容易成為 AI 推理的效能瓶頸。

### 觀點二：透過高速訊號介面最佳化 (High-Speed IO Design)
為了支援 GDDR7 高達 30Gbps 以上的單引腳傳輸速率，晶片設計必須引入進階的調變技術（如 PAM3）與複雜的訊號完整性（Signal Integrity, SI）設計。

*   **優點 (Pros)**：在有限的匯流排寬度下（可縮小晶片封裝面積），榨出極限頻寬，縮小與 HBM 系統在頻寬上的差距。
*   **缺點 (Cons)**：高速 SerDes 與 PHY（實體層）的設計難度極高，功耗也隨頻率呈非線性上升。
*   **成本 (Costs)**：需要購買昂貴的高速 IP 與測試儀器，設計週期長，NRE（一次性工程費用）高昂。
*   **維護性 (Maintainability)**：對於 PCB 板材的要求極為嚴苛（需使用極低損耗板材），微小的阻抗不匹配或生產變異都可能導致訊號衰減，除錯困難。
*   **風險 (Risks)**：如果訊號完整性設計未能達標，實際運作時必須降頻（Downclocking）以維持穩定，導致產品達不到標稱的 AI 算力效能。

### 觀點三：架構層面的容量擴充與批次處理優化 (Batching & Swap)
由於 GDDR 系統總容量有限，對於無法完全塞入記憶體的巨型模型，軟體層需實作複雜的動態載入（Weight Swapping）或優化批次處理（Batching）策略。

*   **優點 (Pros)**：透過純軟體的排程與管線化（Pipelining）設計，讓較廉價的 GDDR 硬體系統也能越級執行龐大的 AI 模型。
*   **缺點 (Cons)**：從系統主記憶體（或 SSD）與 GDDR 之間頻繁搬移權重，會導致嚴重的延遲（Latency），且佔用 PCIe 頻寬。
*   **成本 (Costs)**：增加了推理引擎（Inference Engine）軟體的開發與測試成本。
*   **維護性 (Maintainability)**：這類優化高度依賴特定模型架構（如對特定 Transformer 網路層進行優化），當模型結構改變時，排程器可能需要重新設計。
*   **風險 (Risks)**：對於需要極低延遲的互動式應用（如語音助理或即時客服），權重切換帶來的延遲抖動（Jitter）可能導致嚴重的使用者體驗下降。
