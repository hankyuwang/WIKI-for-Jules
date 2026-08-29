# Wiki 維護巡檢報告 - 2026-08-29

本報告由維護員產生，針對知識庫進行定期巡檢，包含失效連結、過時版本、已棄用架構、官方文件更新與新最佳實務。

## 1. 發現與分析

### 1.1 失效連結與孤兒節點 (Broken Links & Orphans)
* 經腳本檢查，目前知識庫中 **無失效連結 (Broken Links)**。
* 經腳本檢查，目前知識庫中 **無孤兒節點 (Orphan Files)**。

### 1.2 過時版本與官方更新 (Outdated Versions & Official Updates)
* **發現問題**：多處文件提到 Google TPU v8 時標註「(規格尚未公開)」。
* **實際情況**：Google 已正式發表最新一代 TPU，命名為 **Trillium** (即第六代 TPU v6)，而並非 v8，且規格已經公開。
* **影響範圍**：
    * `TPUv8架構與演進.md` 標題與內文需要更新。
    * `知名大廠AI加速晶片研究.md`
    * `INDEX.md`

### 1.3 最佳實務與架構演進 (Best Practices & Architecture Evolution)
* **發現問題**：多處文件提到 FlashAttention 時，標註為 `FlashAttention (如 FlashAttention-2, FlashAttention-3)` 或是較為攏統的稱呼。
* **實際情況**：FlashAttention-3 已經是主流最佳實務，且我們已經有專門的頁面 `FlashAttention3與極低精度量化硬體需求.md`。

## 2. 建議行動清單 (Action Items)

- [ ] **Task 1: 修正 TPU Trillium (v6) 的命名與資訊**
  - 將 `TPUv8架構與演進.md` 重新命名並修改內容，正確反映其為 Trillium (TPU v6)，並移除「(規格尚未公開)」。
  - 修改 `INDEX.md` 中對應的連結名稱。
  - 在 `知名大廠AI加速晶片研究.md` 中，將 `TPU v8 (規格尚未公開)` 的相關描述修正為 Trillium。

- [ ] **Task 2: 統一 FlashAttention 的連結與描述**
  - 將文件中攏統的 `FlashAttention (如 FlashAttention-2, FlashAttention-3)` 替換為直接連結到 `[[FlashAttention3與極低精度量化硬體需求|FlashAttention-3]]` 或是更新描述。

---
> 請直接觸發虛擬團隊執行上述建議行動。
