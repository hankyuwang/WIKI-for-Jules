---
title: AI晶片記憶體架構
level: advanced
tags:
  - memory
  - architecture
  - hardware
---

# AI 晶片記憶體架構

在探討硬體加速器時，我們常將焦點放在算力 (如 TOPS 或是 FLOPS)。然而，強大的運算核心如果沒有足夠快、足夠大的記憶體來餵養資料，只能處於閒置狀態等待。這就是業界常說的「記憶體牆 (Memory Wall)」問題。本篇將深入解析 AI 晶片為了解決此瓶頸所採用的多層次記憶體架構。

## 什麼是記憶體牆 (Memory Wall)？
記憶體牆是指處理器運算速度的提升幅度，遠遠超越了記憶體存取速度（頻寬）的提升幅度。在 AI 運算中，我們需要頻繁地讀取龐大的模型權重 (Weights)，並寫入中間計算產生的特徵圖 (Feature Maps)。資料在運算單元與外部記憶體之間的搬移，不僅消耗了大量的時間，更是系統功耗的主要來源。在如今動輒千億參數的 LLM 時代，AI 負載往往是「Memory-bound (受限於記憶體頻寬)」而非「Compute-bound」。

## 記憶體階層 (Memory Hierarchy) 與創新技術
為了解決記憶體牆，AI 晶片設計了由快到慢、由小到大、由內而外的多層次記憶體結構：

### 1. 暫存器 (Registers) 與 運算單元內部
速度最快，緊貼著 ALU (算術邏輯單元)。為了減少存取，架構師會設計如脈動陣列 (Systolic Array) 的結構，讓資料在運算單元間直接傳遞復用。

### 2. 晶片內建 SRAM (On-chip SRAM / Shared Memory)
相比於 GPU 中複雜的多級 Cache，許多 AI 專用加速器 (如 TPU 或 Groq LPU) 傾向採用巨大且由軟體直接管理的 SRAM (例如 TPU 中的 Unified Buffer 或是 Scratchpad Memory)。
- **優勢**: 提供極高頻寬與確定性的低延遲。
- **挑戰**: SRAM 佔用極大的晶片面積 (Die Area) 且成本高昂，無法無限制地擴大。編譯器必須非常聰明地進行 Tiling (分塊)，將資料分批送入 SRAM。

### 3. 高頻寬記憶體 (HBM, High Bandwidth Memory)
當模型大到 SRAM 無法容納時，就必須依賴封裝內的記憶體。傳統的 GDDR 雖然頻寬高但功耗驚人。
HBM 透過 3D 堆疊技術 (將多個 DRAM 晶粒垂直堆疊) 與 2.5D 先進封裝 (透過矽中介層 Silicon Interposer 與 GPU 連接)，在極短的物理距離內提供了超寬的資料匯流排。這使得晶片能以較低的時脈達到 Tbps 等級的超高頻寬，是目前頂級 AI 訓練晶片 (如 NVIDIA H100) 的標配。

### 4. 突破極限的前瞻技術
當單一節點的 HBM 容量依然不夠時，業界正在發展：
- **CXL (Compute Express Link)**: 透過高速互連協議，讓多個運算節點共享龐大的記憶體池，打破伺服器主機板的容量限制。
- **存算一體 (Processing in Memory, PIM)**: 這被視為終極解決方案，試圖將運算單元直接做進記憶體內部，讓資料原地計算，徹底消滅資料搬移造成的功耗與延遲。這也是 [[AI晶片未來發展趨勢]] 的重點探索方向。
