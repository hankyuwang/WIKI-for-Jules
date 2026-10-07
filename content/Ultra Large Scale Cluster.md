---
title: Ultra Large Scale Cluster
level: research
tags:
  - ultra-large-scale-cluster
  - future-trends
---
# 超大規模叢集互連 (Ultra Large Scale Cluster)

## 摘要
未來的大型模型訓練需要百萬節點級別的算力互連。除了提升單點算力，突破跨機架、跨資料中心的網路拓撲與一致性問題是次世代 AI 基礎設施的核心挑戰。

## Prerequisites
- [[InfiniBand]]
- [[NVLink]]
- [[CXL]]

## 演進與挑戰
現有的 NVLink 網域或 TPU Pod 雖然強大，但面對超過 100K 節點的叢集時，延遲與路由開銷將成為致命傷。研究正集中在全光學網路與動態拓撲重構。
