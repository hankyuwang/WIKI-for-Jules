# 知識庫巡檢報告 (維護員)

## 1. 失效連結 (Broken Links)
- [x] `ASIC加速晶片設計.md`: 修正 `[[GPU架構與演進|GPU]]`, `[[FPGA在AI加速的應用|FPGA]]`
- [x] `FPGA在AI加速的應用.md`: 修正 `[[GPU架構與演進|GPU]]`, `[[ASIC加速晶片設計|ASIC]]`
- [x] `TPU深度解析.md`: 修正 `[[GPU架構與演進|GPU]]` (重複兩次)
- [x] `AI加速晶片架構師學習地圖.md`: 確認 `[[FlashAttention3與極低精度量化硬體需求|Attention]]`, `[[LLM推理擴展與效能瓶頸分析|LLM]]`, `[[TPU與脈動陣列|脈動陣列]]`
- [x] `AI加速晶片與邊緣運算部署策略.md`: 確認 `[[NPU架構探索|NPU]]`
- [x] `AI加速晶片的記憶體架構.md`: 修正 `[[GPU架構與演進|GPU]]`, `[[TPU深度解析|TPU]]`, `[[ASIC加速晶片設計|ASIC]]`

## 2. 過時版本與已棄用架構 (Outdated Versions & Deprecated Architectures)
- [x] 知識庫中多處提及 `Google TPU v6`，但根據官方命名，TPU v6 正式名稱為 **Trillium**。確保沒有遺漏的 TPU v6。
- [x] 文件中提及了 `TPUv8 (規格尚未公開)`，確保所有相關檔案都有一致的免責聲明。

## 3. 官方文件或是論文更新 (Official Docs / Paper Updates)
- [x] 更新 `知名大廠AI加速晶片研究.md` 和 `主流AI加速晶片架構分析.md` 等檔案中提到的 Blackwell (B200), MI325X 以及 Trillium 的規格。
- [x] 新增關於 FlashAttention-3 和 FP4/INT4 等極低精度量化對最新硬體架構影響的細節。 (已存在於知識庫內)

## 4. 新最佳實務 (New Best Practices)
- [x] 將 MoE 模型叢集網路互連 (如 NVLink, ICI) 變得比單晶片算力更重要的新最佳實務，整合進 `AI模型分類與硬體架構關聯.md` 等文件。
