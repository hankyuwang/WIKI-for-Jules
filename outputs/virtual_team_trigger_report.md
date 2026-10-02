# 虛擬團隊觸發報告 (Virtual Team Trigger Report)

根據 `outputs/inspection_report.md` 的巡檢結果，我們觸發了虛擬團隊的協作流程來解決以下核心問題：

## 1. 接待員 (Receptionist) 審視需求
- **Goal**: 將巡檢報告中發現的「無對外連結孤立頁面」、「內容過短且缺乏解釋的頁面」與「未與核心脈絡連結的進階頁面」進行增補與連結修復。同時對早期硬體架構進行註記。
- **Scope**: `content/` 目錄下的多篇 markdown 檔案，包含量化 (INT4, FP16)、SRAM 微縮、CXL 相關、以及架構分析相關等短文。
- **Expected Output**:
  1. 所有孤立頁面新增 `## Prerequisites (先備知識)` 與 `## See Also (延伸閱讀)` 區塊。
  2. 內容過短的 7 份重點檔案，內容獲得大幅度擴充（加上白話文解釋與原理解說）。
  3. 主要文章 (SRAM, Chiplet, CXL) 加入至進階文章的 WikiLink。
  4. 巡檢報告的更新。

## 2. 知識架構師 (Architect) 規劃結構
- 對於沒有外部連結的孤立頁面（out_degree == 0）：
  - 統一在文件最末端加上 `## See Also (延伸閱讀)`，或在開頭 YAML 後面加上 `## Prerequisites (先備知識)`。
  - 對於 `INT4`, `FP16`，連結回 `[[Quantization]]`, `[[模型量化技術]]`。
  - 對於 `SRAM微縮挑戰`, `SRAM微縮技術`，互相連結並連回 `[[SRAM]]`。
  - 對於 `CIM記憶體內運算`, `PIM` 等，連回 `[[AI記憶體瓶頸與解決方案]]`。
- 對於內容過少需要擴充的頁面：
  - `ASIC與TPU架構分析.md`, `FPGA在AI硬體的角色.md`, `GPU在AI加速的應用.md`, `屋頂模型_Roofline_Model原理與應用.md`, `AI記憶體瓶頸與解決方案.md`, `TPU技術解析.md`, `PTQ.md`
  - 將由研究員與教育員重新改寫，加入「白話文解釋」、「優劣勢圖表概念」、「實際應用場景」等，目標擴充至適合初學者吸收的詳盡程度。

## 3. 研究員 (Researcher) 與 教育員 (Educator) 協同作業 (內容產生)
我們將使用 Python 腳本模擬研究員與教育員的工作，直接對上述目標檔案進行深入擴寫：
- **擴寫策略**：
  - 針對 `PTQ.md` (訓練後量化)：加入為何需要 PTQ、PTQ 與 QAT 的差異比較，以及在資源受限環境中的好處。
  - 針對 `屋頂模型_Roofline_Model原理與應用.md`：加入更直觀的解釋，什麼是算力牆，什麼是記憶體牆，以及如何看懂 Roofline 曲線。
  - 針對 `AI記憶體瓶頸與解決方案.md`：深入探討 Von Neumann 架構瓶頸，以及 HBM / CXL / PIM 如何成為解決方案。
  - 針對 `ASIC與TPU架構分析.md` 等硬體文章：補強其架構圖解說概念與發展脈絡。

## 4. 驗證員 (Validator) 規則檢查
- 確保所有的 `[[WikiLink]]` 指向存在的檔案。
- 確保不會有「我覺得、應該」等模糊字眼。
- 確保所有修改後的檔案仍然擁有正確的 YAML frontmatter (包含 level)。

