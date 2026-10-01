# 虛擬團隊任務分派：Wiki 過時架構更新

根據 `wiki_inspection_report.md`，發現知識庫中有過時的架構描述（Volta, TPU v1/v2）。
依據 `.jules/instructions.md` 規範，啟動虛擬團隊進行更新：

## 接待員 (Receptionist)
- **需求確認**: 需要將文件中的早期架構 (Volta, TPU v1/v2) 對齊當前最新架構 (Hopper/Blackwell, Trillium/TPU v6)，並保留早期架構的歷史脈絡標記（例如標記為「早期架構」）。

## 知識架構師 (Knowledge Architect)
- **架構規劃**: 相關文件需引入 `[[Hopper架構]]`、`[[Blackwell架構]]`、`[[Trillium架構]]` 等新連結，確保知識地圖隨技術演進更新。

## 研究員 (Researcher)
- **知識更新**:
  1. NVIDIA GPU: 從 Volta 的初代 Tensor Core，演進至 Hopper 的 Transformer Engine 與 Blackwell 的第二代 Transformer Engine 及 FP4 支援。
  2. Google TPU: 從 TPU v1 (僅推論)、v2/v3 (訓練與 HBM 引入)，演進至 Trillium (TPU v6) 的高頻寬與大規模稀疏模型優化。

## 驗證員 (Validator)
- **事實查核**: 確認 Trillium 就是 TPU v6 (正確)。確保不會憑空創造未發布的硬體規格。

## 教育員 (Educator)
- **內容轉換**: 將上述知識轉化為易懂的 Markdown，整合至 `content/GPU架構與演進.md` 與 `content/TPU架構深度解析.md`，並確保 `level` 與 `Prerequisites` 完整。

請研究員與教育員接手更新 `content/GPU架構與演進.md` 與 `content/TPU架構深度解析.md`。
