# Wiki 維護巡檢報告

## 1. 失效連結 (Dead Links)
- [ ] 經檢查，目前無失效連結。

## 2. 孤立頁面 (Orphaned Files)
- [ ] 經檢查，目前無孤立頁面。

## 3. 過時版本與官方文件更新 (Outdated Content)
- [x] **Google TPU v6 名稱更新**: 官方已正式將 TPU v6 命名為 **Trillium**。需要將提及 `TPU v6` 或 `Trillium` 但未說明其關聯的地方進行統一或補充說明。
    - 雖然目前知識庫中已經有大量 `Trillium` 的出現，但為了更準確，可以建立一份獨立的 `Trillium` wiki 頁面或將 `Trillium` 納入知識地圖，並補充電明它是第六代 TPU。

## 4. 建議執行動作
- [x] 在 `content/` 新增 `Trillium.md` 介紹 Google 的第六代 TPU。
- [x] 在 `content/INDEX.md` 中將 `Trillium` 加入硬體架構分類。


## 巡檢項目：孤立節點與知識地圖延伸

發現 1 個未與知識地圖 `INDEX.md` 連結的孤立節點：
- `SSM.md`

**改善方案：**
1. 觀察 `Mamba.md` 內容，Mamba 是基於狀態空間模型 (SSM) 的新架構。
2. 將 `SSM` 歸類至 `INDEX.md` 的「基礎運算與模型架構」分類中，置於 `Mamba` 的附近，作為其基礎知識延伸。
3. 在 `INDEX.md` 中新增對 `SSM` 的連結及簡短說明。

## 巡檢項目：內容過少與專有名詞解說 (虛擬團隊補充)

發現 `SSM.md` 內容過於簡略且充斥佔位符文字（例如「狀態空間模型基礎」等字樣未有深入解釋）。讀者無法從中學習到真正的 SSM 背景知識。

**改善方案 (觸發虛擬團隊補充)：**
1. 將呼叫虛擬團隊對 `SSM.md` 進行大幅度重寫，補充其真正的數學背景（如 State Space Model 如何將連續訊號轉化為離散狀態、HiPPO 矩陣的概念）及其在硬體上的優勢（如硬體感知的平行掃描）。
2. 在 `SSM.md` 中新增 `Prerequisites` 區段，並連結至相關前置知識。
