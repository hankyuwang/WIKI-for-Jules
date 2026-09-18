# Wiki 巡檢報告

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
