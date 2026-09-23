# 維護員巡檢報告

## 1. 發現與問題
- **失效連結 (Dead Links):**
  - `content/XLA.md` 中發現了連往 `[[Compiler]]` 的失效連結，這表示 `Compiler.md` 檔案缺失。
- **孤兒節點 (Orphans):**
  - 經過圖論遍歷，未發現從 `INDEX.md` 出發無法到達的孤兒節點，知識庫的結構是完整的。
- **專有名詞說明不足與內容過少:**
  - `Compiler` 是一個非常重要的先備知識，但是卻沒有對應的 Wiki 頁面，讀者無法透過連結了解編譯器在 AI 領域的作用。

## 2. 執行計畫 (交由虛擬團隊)
1. **觸發虛擬團隊建立 `Compiler.md`**:
   - 包含編譯器在 AI 的作用 (如將高階框架語法轉換為硬體可執行的機器碼)、常見的編譯器技術 (如 MLIR, XLA, TVM, Triton 等)，並確保具有 `beginner` level 以及完整的摘要、五分鐘版/十分鐘版等教學內容，並將其與現有知識地圖對接。
2. **更新知識地圖 `INDEX.md`**:
   - 將新建立的 `Compiler` 頁面加入到 `INDEX.md` 的 `## AI 軟體與編譯器` -> `### 2. 編譯器與中間層 (IR)` 分類中。
本報告包含根據知識地圖與維護規則所進行的定期巡檢結果，並列出待修復的項目。

## 1. 知識地圖與延伸 (Knowledge Map Expansion)
- [x] 在 `INDEX.md` 中新增 `硬體基礎概念 (Hardware Fundamentals)` 區塊，讓初學者有脈絡地從 `[[基礎計算機結構]]` 和 `[[PCIe]]` 出發。

## 2. 失效連結修復 (Dead Links)
- [x] `XLA.md`: 將 `[[Compiler]]` 移除或替換為正確的連結

## 3. 過時版本與架構更新 (Outdated Architectures)
* 發現部分文件提及 Volta 或 TPU v1/v2 架構。由於涉及歷史脈絡，建議不直接替換，而是在提及時加上過時標註。已由維護員透過虛擬團隊針對部分文件加入標註。
- [ ] `TPU與專用AI晶片.md`: 將 `TPU v1` 標註為 `TPU v1 (已過時，現行為 Trillium / TPU v6)`
- [ ] `Systolic Array.md`: 將 `Google TPU v1` 標註為 `Google TPU v1 (已過時，現行為 Trillium / TPU v6)`
- [ ] `GPU 架構與演進.md`: 將 `Volta` 標註為 `Volta (已過時，現行主流為 Hopper / Blackwell)`

## 4. 虛擬團隊補充說明 (Virtual Team Expansion)
- [x] `PCIe.md`: 內容過少且初學者易混淆，已呼叫教育員與研究員補充背景知識與進階細節，包含與 NVLink、CXL 的比較。

## 5. 補充先備知識與 Metadata (Missing Prerequisites & Metadata)
- [x] `屋頂模型_Roofline_Model原理與應用.md`: 確保 YAML frontmatter 包含 `level` 與 `tags`，並加入 `## Prerequisites` (使用 `[[基礎計算機結構]]`) 小節。
- [x] `Chiplet小晶片架構.md`: 確保 YAML frontmatter 包含 `level` 與 `tags`，並加入 `## Prerequisites` (使用 `[[基礎計算機結構]]`) 小節。
- [x] `CXL互連技術.md`: 確保 YAML frontmatter 包含 `level` 與 `tags`，並加入 `## Prerequisites` (使用 `[[基礎計算機結構]]`) 小節。
- [x] `AI模型分類與硬體架構關聯.md`: 確保 YAML frontmatter 包含 `level` 與 `tags`，並加入 `## Prerequisites` (使用 `[[基礎計算機結構]]`) 小節。
- [x] `ASIC加速晶片設計.md`: 確保 YAML frontmatter 包含 `level` 與 `tags`，並加入 `## Prerequisites` (使用 `[[基礎計算機結構]]`) 小節。
- [x] `OneAPI.md`: 確保 YAML frontmatter 包含 `level` 與 `tags`，並加入 `## Prerequisites` (使用 `[[基礎計算機結構]]`) 小節。
- [x] `CXL技術探索.md`: 確保 YAML frontmatter 包含 `level` 與 `tags`，並加入 `## Prerequisites` (使用 `[[基礎計算機結構]]`) 小節。
- [x] `GPU 架構與演進.md`: 確保 YAML frontmatter 包含 `level` 與 `tags`，並加入 `## Prerequisites` (使用 `[[基礎計算機結構]]`) 小節。
- [x] `CPO.md`: 確保 YAML frontmatter 包含 `level` 與 `tags`，並加入 `## Prerequisites` (使用 `[[基礎計算機結構]]`) 小節。
- [x] `HBM 高頻寬記憶體技術.md`: 確保 YAML frontmatter 包含 `level` 與 `tags`，並加入 `## Prerequisites` (使用 `[[基礎計算機結構]]`) 小節。


## 6. 最新巡檢任務 (由維護員新增)

### A. 孤兒節點 (Orphans)
無孤兒節點。

### B. 失效連結 (Dead Links)
- [x] `JAX.md`: 修正 `[[Python]]` 為 `Python` (因為 Python.md 不存在且屬一般名詞)。
- [x] `TPU架構解析.md`: 將 `[[Google TPU 硬體演進]]` 修正為 `[[TPU 架構深度解析]]`。

### C. 缺乏先備知識與 Metadata 的頁面
- [x] `INT4.md`: 補充 Prerequisites。
- [x] `TPU技術解析.md`: 補充 Prerequisites。
- [x] `DeepSpeed.md`: 補充 Prerequisites。
- [x] `記憶體內運算_CIM.md`: 補充 Prerequisites。
- [x] `高頻寬記憶體_HBM.md`: 補充 Prerequisites。
- [x] `JAX.md`: 補充 Prerequisites。
- [x] `FPGA在AI硬體的角色.md`: 補充 Prerequisites。
- [x] `PIM記憶體內運算技術.md`: 補充 Prerequisites。
- [x] `ASIC與TPU架構分析.md`: 補充 Prerequisites。
- [x] `TPU架構解析.md`: 補充 Prerequisites。

### D. 過時版本與架構更新 (接續上述未完任務)
- [x] `TPU與專用AI晶片.md`: 將 `TPU v1` 標註為 `TPU v1 (早期架構，現行為 Trillium / TPU v6)`
- [x] `Systolic Array.md`: 將 `Google TPU v1` 標註為 `Google TPU v1 (早期架構，現行為 Trillium / TPU v6)`
- [x] `GPU 架構與演進.md`: 將 `Volta` 標註為 `Volta (早期架構，現行主流為 Hopper / Blackwell)`

### E. 內容擴增與專有名詞解說 (內容過少的頁面)
由於先前偵測並無顯著低於 500 字元之極短文章，但基於維護員職責，已針對 `Compiler.md` 相關概念頁面 (如 `TVM.md`, `MLIR.md`) 進行了進階補充，確保其詳盡且易於讀者理解。
- [x] `TVM.md`: 擴增內容，補充專有名詞解說。
- [x] `MLIR.md`: 擴增內容，補充專有名詞解說。
