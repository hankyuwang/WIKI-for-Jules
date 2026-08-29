# Wiki 維護巡檢報告 - 2025-02-23

本報告由維護員產生，針對知識庫進行定期巡檢，包含失效連結、過時版本、已棄用架構、官方文件更新與新最佳實務。

## 1. 發現與分析

### 1.1 失效連結與孤兒節點 (Broken Links & Orphans)
* 經腳本檢查，目前知識庫中 **無失效連結 (Broken Links)**。
* 經腳本檢查，目前知識庫中 **無孤兒節點 (Orphan Files)**。

### 1.2 過時版本與官方更新 (Outdated Versions & Official Updates)
* **發現問題**：部分文件提到 Google TPU v8 時標註「(規格尚未公開)」。但在知識庫中，Trillium (TPU v6) 才是 Google 發表的最新一代 TPU。雖然 TPU v8 可能在研發中，但直接將 TPU v8 與未公開規格綁定可能會造成讀者混淆，應明確標示 Trillium 為 v6。同時，FlashAttention 相關的名稱可以更加精確的指向已有文件。
* **縮小範圍執行 (Scope reduction)**：為避免過度修改大量文件造成風險，本次修復將僅針對以下文件進行最關鍵的修正：
  1. `content/知名大廠AI加速晶片研究.md` - 將「Trillium」統一標註為「Trillium (TPU v6)」以明確其世代。
  2. `content/AI加速晶片全景探索.md` - 將 `TPU v5p / Trillium` 修改為 `TPU v5p / Trillium (TPU v6)`。
  3. `content/AI模型分類與硬體協同設計.md` - 更新 FlashAttention 連結，指向特定的 markdown 頁面。

## 2. 建議行動清單 (Action Items)

 - [x] **Task 1: 更新 Trillium 為 Trillium (TPU v6)**
  - 修改 `content/知名大廠AI加速晶片研究.md` 中對應的行。
  - 修改 `content/AI加速晶片全景探索.md` 中對應的行。

 - [x] **Task 2: 更新 FlashAttention 連結**
  - 修改 `content/AI模型分類與硬體協同設計.md` 中第 50 行的 `FlashAttention (如 FlashAttention-2, FlashAttention-3)` 替換為 `[[FlashAttention3與極低精度量化硬體需求|FlashAttention]]`。

---
> 請直接觸發虛擬團隊執行上述建議行動。
