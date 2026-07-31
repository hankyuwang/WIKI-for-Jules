---
title: Chiplet (小晶片) 架構探索
level: intermediate
tags:
  - hardware
  - chiplet
  - packaging
  - architecture
---

# Chiplet (小晶片) 架構探索

## 摘要

隨著摩爾定律 (Moore's Law) 逼近物理極限，單一超大晶片 (Monolithic Die) 的製造成本呈指數上升且良率急遽下降。Chiplet (小晶片) 架構應運而生，其核心概念是將原本單一的巨大晶片拆解成多個較小的、具有特定功能 (如運算、記憶體控制、I/O 等) 的裸晶 (Dies/Chiplets)，再透過先進封裝技術 (如 2.5D CoWoS 或 3D 堆疊) 和高速互連標準 (如 UCIe) 將它們整合在同一個封裝內。此架構不僅能大幅提升整體良率，還能實現異質整合 (Heterogeneous Integration)，允許不同功能的 Chiplet 使用最適合的製程節點製造。

## Chiplet 的互連與封裝技術方案

### 方案一：基於標準有機載板的高密度 2D 封裝 (如 MCM)

最基礎的 Chiplet 整合方式，將多個裸晶平鋪在標準的有機基板 (Organic Substrate) 上，透過基板內的佈線進行連接 (例如 AMD 早期 EPYC 處理器設計)。

*   **優點 (Pros)：** 封裝成本最低；製程成熟度高；散熱相對容易處理。
*   **缺點 (Cons)：** 晶片間互連的頻寬密度較低，功耗較高，延遲較大；無法滿足 AI 加速器等極高頻寬需求的應用。
*   **成本 (Costs)：** 較低，適合對成本敏感或頻寬要求中等的應用。
*   **維護性 (Maintainability)：** 相對於先進封裝，製程變異造成的除錯與分析較為直接。
*   **風險 (Risks)：** 互連頻寬可能成為系統效能的瓶頸 (Die-to-Die 延遲過高)。

### 方案二：基於矽中介層 (Silicon Interposer) 的 2.5D 封裝 (如 CoWoS)

在有機載板之上加入一層矽中介層，利用半導體製程在矽中介層中製作極高密度的微小導線和矽穿孔 (TSV)，連接上方的多個 Chiplets 和底層載板。這是目前高階 GPU (如 Nvidia Hopper/Blackwell) 和 AI 加速器的標準做法。

*   **優點 (Pros)：** 可提供極高的 Die-to-Die 互連頻寬 (支援 HBM 等高頻寬記憶體)；佈線密度遠高於有機基板。
*   **缺點 (Cons)：** 矽中介層的尺寸受限於光罩極限 (Reticle Limit)，雖然可以透過 Stitching 擴展，但難度高；成本顯著增加。
*   **成本 (Costs)：** 高昂的矽中介層製造與高精度封裝成本，產能受限於台積電等先進封裝廠。
*   **維護性 (Maintainability)：** 封裝過程的熱應力和良率控制極為複雜，測試覆蓋率 (Test Coverage) 要求高 (Known Good Die, KGD 是關鍵)。
*   **風險 (Risks)：** 先進封裝產能不足可能導致嚴重的供應鏈瓶頸。

### 方案三：3D 堆疊與異質整合 (如 Foveros, SoIC)

不局限於平面的 2.5D 排列，而是將不同功能的 Chiplets 直接垂直堆疊 (例如將 SRAM 堆疊在 Logic 上，或將 Logic 堆疊在 I/O Die 上)，使用微凸塊 (Micro-bumps) 甚至混合鍵合 (Hybrid Bonding) 進行面對面 (Face-to-Face) 的直接連接。

*   **優點 (Pros)：** 實現了最短的互連距離，提供極限的頻寬密度和極低的通訊功耗；可大幅縮減封裝面積 (Footprint)。允許真正的 "System on Package"。
*   **缺點 (Cons)：** 史無前例的散熱挑戰，下層晶片的熱量很難排出；設計極為複雜，需要 3D 感知的 EDA 工具協同設計。
*   **成本 (Costs)：** 目前最為昂貴的封裝方案。
*   **維護性 (Maintainability)：** 一旦堆疊失敗，所有疊加的晶圓皆報廢，良率要求達到極致；測試極度困難，通常需要內建自測試 (BIST) 電路。
*   **風險 (Risks)：** 熱管理失敗可能導致降頻或晶片燒毀；跨廠牌的 Chiplet 互通性 (如 UCIe 標準) 尚未完全普及，目前多為單一廠商的封閉生態。
