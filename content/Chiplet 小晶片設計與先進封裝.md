---
title: Chiplet 小晶片設計與[[AdvancedPackaging|先進封裝]]
level: intermediate
tags:
  - Chiplet
  - packaging
  - hardware
  - CoWoS
---

# Chiplet 小晶片設計與[[AdvancedPackaging|先進封裝]]

## 摘要
隨著半導體製程微縮遇到物理與經濟上的雙重挑戰，單一大型晶片（Monolithic Die）的良率與成本問題日益浮現。Chiplet（小晶片）技術應運而生，它將原本龐大的單一系統單晶片（SoC）拆解成多個功能獨立的小晶片，再透過[[AdvancedPackaging|先進封裝]]技術將它們整合在一起。這種技術已成為現代高效能運算與 AI 晶片（如 AMD MI300、Intel Ponte Vecchio）的設計主流。

## 解決方案與觀點分析

### 觀點一：突破光罩極限與提升良率
傳統單一晶片面積受限於黃光微影設備的光罩極限（約 800 mm²），且面積越大，遇到缺陷而報廢的機率呈指數上升。
- **優點 (Pros)**：將大晶片拆分為數個小晶片，能大幅提升單片晶圓的良率，並允許打造出邏輯面積遠超光罩極限的超大型處理器。
- **缺點 (Cons)**：拆分後的小晶片之間需要額外的互連電路（Die-to-Die Interface），會增加少許功耗與面積。
- **成本 (Costs)**：雖然降低了矽晶圓本身的製造成本，但被後端昂貴的[[AdvancedPackaging|先進封裝]]成本部分抵銷。
- **維護性 (Maintainability)**：硬體設計上的模組化提高了 IP 的重複使用率，減少了重新設計整個 SoC 的負擔。
- **風險 (Risks)**：測試難度增加，需要具備已知良好晶粒（Known Good Die, KGD）的測試能力，否則一顆壞掉的 Chiplet 可能導致整個封裝報廢。

### 觀點二：異質整合（Heterogeneous Integration）的靈活性
Chiplet 允許在同一個封裝內整合來自不同製程節點、甚至不同代工廠的晶片。
- **優點 (Pros)**：設計者可以將核心邏輯運算單元採用最先進、昂貴的製程（如 3nm），而將 I/O、記憶體控制器或類比電路保留在成熟、便宜的製程上（如 12nm 或 28nm），達到效能與成本的最佳化配置。
- **缺點 (Cons)**：不同製程與功能模組的整合，帶來了極大的熱力學（散熱）與供電設計挑戰。
- **成本 (Costs)**：整體開發成本初期較高，需要掌握複雜的 2.5D/3D 封裝技術與熱管理模擬。
- **維護性 (Maintainability)**：為未來的產品升級提供了靈活性，例如只需替換運算核心 Chiplet 而保留 I/O Chiplet 設計。
- **風險 (Risks)**：跨代工廠的供應鏈管理極度複雜，若其中一種晶片缺貨，將導致整個產品無法出貨。

### 觀點三：依賴[[AdvancedPackaging|先進封裝]]技術與互連標準（如 UCIe）
要讓多個 Chiplet 像單一晶片般運作，需要如 TSMC [[CoWoS]]、Intel EMIB 等[[AdvancedPackaging|先進封裝]]，以及如 UCIe 這樣的通用 Die-to-Die 互連標準。
- **優點 (Pros)**：[[AdvancedPackaging|先進封裝]]提供極高的線路密度與頻寬；UCIe 標準則有望打破封閉生態，讓不同廠商的 Chiplet 能夠互通。
- **缺點 (Cons)**：[[AdvancedPackaging|先進封裝]]產能高度集中於少數晶圓廠；目前多數產品仍採用自定義的互連協定，UCIe 生態尚未完全成熟。
- **成本 (Costs)**：對[[AdvancedPackaging|先進封裝]]產能的依賴使得產能吃緊時會面臨極高的溢價，且基礎封裝設備投資龐大。
- **維護性 (Maintainability)**：隨著標準化（UCIe）推進，未來的系統級測試與除錯工具將逐步完善。
- **風險 (Risks)**：地緣政治或供應鏈中斷可能導致[[AdvancedPackaging|先進封裝]]產能受限，成為整個 AI 硬體產業的最大瓶頸。
