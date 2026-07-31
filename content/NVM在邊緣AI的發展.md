---
title: NVM在邊緣AI的發展
level: intermediate
tags:
  - NVM
  - edge-ai
  - memory
  - hardware
---

# NVM在邊緣AI的發展

## 摘要
非揮發性記憶體（Non-Volatile Memory, NVM）如 MRAM、RRAM、PCM 等，在電源關閉後仍能保存資料。在資源受限且對功耗極度敏感的邊緣 AI 設備（Edge AI）中，NVM 展現出取代傳統 Flash 與 SRAM 的巨大潛力。透過提供高密度儲存、快速喚醒（Instant-On）與極低的待機功耗，NVM 正推動邊緣設備實現更強大的本地推論能力。

## 邊緣應用與架構觀點

### 方案一：使用 MRAM 作為嵌入式記憶體 (Embedded MRAM for Edge Inference)
利用磁阻式隨機存取記憶體（MRAM）取代邊緣微控制器（MCU）中的嵌入式 Flash（eFlash）甚至部分 SRAM。
- **優點 (Pros):** 寫入速度與壽命遠優於 eFlash，且待機漏電極低，非常適合電池供電的邊緣設備實現快速喚醒與本地模型推論。
- **缺點 (Cons):** 寫入功耗仍略高於 SRAM，且讀取裕度（Read Margin）在極端溫度下可能受限。
- **成本 (Costs):** 需要晶圓代工廠提供特殊的後段金屬製程（BEOL）支援，生產成本高於傳統 MCU 製程。
- **維護性 (Maintainability):** MRAM 具有高耐用性（High Endurance），長期運作不易像 Flash 般老化，維護需求低。
- **風險 (Risks):** 外部強磁場可能干擾資料儲存，需在封裝或設計上加入磁屏蔽機制。

### 方案二：使用 RRAM 進行類比記憶體內運算 (Analog CIM with RRAM)
利用電阻式記憶體（RRAM）的交叉陣列直接儲存神經網路權重，並在邊緣設備上執行極低功耗的類比乘加運算。
- **優點 (Pros):** 徹底消除資料搬移，達成極致的能源效率（TOPS/W），非常適合語音喚醒、關鍵字辨識等 Always-On 應用。
- **缺點 (Cons):** 類比運算的精度受限，僅能支援低精度的量化模型（如 4-bit 或 8-bit）。
- **成本 (Costs):** 雖然 RRAM 結構簡單，但整合高精度 ADC/DAC 的混合訊號電路會佔據相當大的晶片面積並增加設計成本。
- **維護性 (Maintainability):** RRAM 元件存在電導漂移（Conductance Drift）現象，隨著時間推移模型準確率可能下降，需定期重新校準。
- **風險 (Risks):** 寫入壽命有限，若需頻繁進行邊緣學習（Edge Learning）更新權重，會快速耗損元件壽命。

### 方案三：採用 3D NAND 實現邊緣大容量儲存 (3D NAND for High-Capacity Edge Storage)
不追求極致運算速度，而是利用成熟的 3D NAND 結合高效能控制器，在邊緣設備中儲存更大、更複雜的 AI 模型（如小型語言模型 SLM）。
- **優點 (Pros):** 技術極度成熟，提供最高的儲存容量與最低的每 GB 成本。
- **缺點 (Cons):** 存取延遲極高，無法直接用於運算，需頻繁將權重載入 SRAM 或 DRAM，導致龐大的功耗與頻寬瓶頸。
- **成本 (Costs):** 記憶體元件本身極為廉價，是低成本邊緣設備的首選方案。
- **維護性 (Maintainability):** 控制器已內建完善的垃圾回收與耗損平均技術，系統級維護極其簡單。
- **風險 (Risks):** 頻繁的讀寫會導致 SSD 或 eMMC 提早報廢，且極端的環境溫度（如車載應用）會嚴重影響資料保留時間（Data Retention）。
