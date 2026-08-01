---
title: 新型非揮發性記憶體在邊緣AI的應用
level: advanced
tags:
  - NVM
  - edge-ai
  - memory
  - emerging-tech
---

# 新型非揮發性記憶體在邊緣AI的應用

## 摘要

隨著物聯網（IoT）與穿戴式裝置的普及，將人工智慧推理能力推向資料產生源頭的「邊緣 AI」（Edge AI）已成為重要趨勢。然而，邊緣裝置通常受限於極其嚴苛的功耗、電池壽命與物理面積限制，傳統的 SRAM 和 DRAM 難以同時滿足高密度與超低待機功耗的需求。新型非揮發性記憶體（Emerging Non-Volatile Memory, eNVM），如 MRAM、RRAM、PCM 和 FeRAM，因具備斷電不遺失資料、待機漏電流極低以及較高的儲存密度，成為邊緣 AI 晶片的理想選擇。本文將從三種不同的應用視角，探討 eNVM 在邊緣 AI 領域的潛力與挑戰。

## 視角一：取代傳統 eFlash 作為權重儲存 (Weight Storage Replacement)

邊緣 AI 推理晶片通常需要將預先訓練好的神經網路權重（Weights）儲存在非揮發性記憶體中。傳統上使用的是嵌入式快閃記憶體（eFlash）。然而，eFlash 寫入電壓高、微縮困難（在 28nm 以下製程遭遇瓶頸），且讀取速度較慢。此視角主張使用 MRAM 或 RRAM 來取代 eFlash。

- **優點（Pros）**：eNVM 具有更好的製程微縮能力（可輕易微縮至 22nm 甚至更小），寫入功耗較低，且與 CMOS 製程整合度高。能夠在更小的晶片面積內儲存更大的 AI 模型。
- **缺點（Cons）**：部分 eNVM（如 RRAM）的讀取穩定性較差，容易受到製程變異影響。且在頻繁讀取的情況下，可能會有輕微的讀取干擾（Read Disturb）問題。
- **成本（Costs）**：相較於成熟的 eFlash，eNVM 的製造成本目前仍然較高，需要額外的光罩與特殊材料。
- **維護性（Maintainability）**：資料保持力（Data Retention）與耐高溫特性需要嚴格的測試與驗證，以確保產品在不同環境下的可靠度。
- **風險（Risks）**：若 eNVM 的良率無法達到 eFlash 的水準，將難以在對成本極度敏感的 IoT 市場中普及。

## 視角二：整合為高密度工作記憶體 (High-Density Working Memory / L2 Cache)

傳統邊緣 AI 晶片依賴 SRAM 作為工作記憶體（儲存中間運算結果與激活值 Activation）。但 SRAM 面積太大且漏電流（Leakage Current）高。此視角探討將 eNVM（特別是讀寫速度較快的 MRAM 或 FeRAM）用於取代或部分取代 SRAM，作為高密度的 L2 快取或暫存記憶體。

- **優點（Pros）**：大幅降低晶片的靜態功耗（Static Power），且能提供比 SRAM 更高的儲存密度，減少頻繁存取外部 DRAM 的需求，進而降低系統總功耗。
- **缺點（Cons）**：eNVM 的寫入延遲（Write Latency）與寫入功耗（Write Power）通常高於 SRAM。對於頻繁寫入的 AI 工作負載，可能會成為效能瓶頸。
- **成本（Costs）**：需要重新設計記憶體控制器與快取架構，研發成本高。
- **維護性（Maintainability）**：eNVM 的寫入壽命（Endurance）通常不如 SRAM（例如 RRAM 可能只有 $10^6$ 次）。需要實作複雜的耗損平均（Wear-Leveling）演算法來延長使用壽命。
- **風險（Risks）**：若耗損平均機制設計不良，可能導致記憶體提早損壞，使得整個邊緣裝置失效。

## 視角三：實現超低功耗常時啟動系統 (Always-On System with Normally-Off Computing)

邊緣 AI 中有許多「常時啟動」（Always-On）的應用，如語音喚醒（Keyword Spotting）或異常震動偵測。此視角利用 eNVM 的非揮發特性，實現「常態關閉運算」（Normally-Off Computing）。系統在沒有事件發生時可以完全切斷電源（Zero Leakage），當感測器觸發時，能瞬間（Instant-On）從 eNVM 中喚醒狀態並進行運算。

- **優點（Pros）**：能將邊緣裝置的待機功耗降至近乎零，極大地延長電池壽命（可能達到數年甚至十年），特別適合能源採集（Energy Harvesting）系統。
- **缺點（Cons）**：系統喚醒時的電流突波（Inrush Current）與從 eNVM 載入狀態到邏輯單元的延遲，需要精密的電源管理與電路設計。
- **成本（Costs）**：硬體設計複雜，需要高度客製化的晶片架構與電源管理 IC (PMIC)，初期 NRE (Non-Recurring Engineering) 成本極高。
- **維護性（Maintainability）**：軟硬體協同設計難度極高，開發者需要精確掌握系統何時該休眠、何時該喚醒，並管理資料在揮發性與非揮發性記憶體之間的搬移。
- **風險（Risks）**：這類應用市場高度碎片化，若缺乏統一的開發平台或標準，難以達到規模經濟，導致單晶片成本過高。
