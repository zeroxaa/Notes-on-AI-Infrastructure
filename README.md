# 从地皮到模型：AI Infra 杂谈

**中文 | [English](en/README.md)**

一本关于 AI 基础设施（AI Infra）的开源电子书，现提供完整中文与英文两个版本。

原作者：**王洪磊**。中文原书来自 [honglei_wang/Notes-on-AI-Infrastructure](https://gitee.com/honglei_wang/Notes-on-AI-Infrastructure)。

本仓库在原书基础上新增英文译本、英文图表、双语目录与同步检查；中文正文和原图保留。每页顶部可切换对应语言，或按上一页、下一页顺序阅读。英文包含全部 11 章、3 篇辑前言、序言与后记。翻译范围与维护流程见 [双语维护说明](TRANSLATIONS.md)。

## 简介

本书从 IDC 建设、GPU 集群交付、智算网络，到 Kubernetes 调度、训练平台开发、SRE 运维，再到分布式训练、推理部署与 AI Infra 工程师成长，试图把散落的 AI Infra 知识串成一张完整地图。

目标读者：

- 想进入 AI Infra 领域的初中级工程师
- 传统云计算 / SRE 背景，想理解大模型基础设施差异的人
- 需要建设或运营智算中心的技术管理者
- 对 AI 工程落地感兴趣的开发者

## 目录

- [序言](%E5%BA%8F%E8%A8%80.md)

### [第一辑前言：造场子](%E7%AC%AC%E4%B8%80%E8%BE%91%EF%BC%9A%E9%80%A0%E5%9C%BA%E5%AD%90/%E7%AC%AC%E4%B8%80%E8%BE%91%E5%89%8D%E8%A8%80.md)

- [第 1 章 IDC 与智算中心建设](%E7%AC%AC%E4%B8%80%E8%BE%91%EF%BC%9A%E9%80%A0%E5%9C%BA%E5%AD%90/%E7%AC%AC01%E7%AB%A0-IDC%E4%B8%8E%E6%99%BA%E7%AE%97%E4%B8%AD%E5%BF%83%E5%BB%BA%E8%AE%BE.md)
- [第 2 章 GPU 集群硬件选型与交付](%E7%AC%AC%E4%B8%80%E8%BE%91%EF%BC%9A%E9%80%A0%E5%9C%BA%E5%AD%90/%E7%AC%AC02%E7%AB%A0-GPU%E9%9B%86%E7%BE%A4%E7%A1%AC%E4%BB%B6%E9%80%89%E5%9E%8B%E4%B8%8E%E4%BA%A4%E4%BB%98.md)
- [第 3 章 智算网络与 RDMA/RoCEv2](%E7%AC%AC%E4%B8%80%E8%BE%91%EF%BC%9A%E9%80%A0%E5%9C%BA%E5%AD%90/%E7%AC%AC03%E7%AB%A0-%E6%99%BA%E7%AE%97%E7%BD%91%E7%BB%9C%E4%B8%8ERDMA-RoCEv2.md)

### [第二辑前言：搭平台](%E7%AC%AC%E4%BA%8C%E8%BE%91%EF%BC%9A%E6%90%AD%E5%B9%B3%E5%8F%B0/%E7%AC%AC%E4%BA%8C%E8%BE%91%E5%89%8D%E8%A8%80.md)

- [第 4 章 Kubernetes 与 Volcano 调度平台](%E7%AC%AC%E4%BA%8C%E8%BE%91%EF%BC%9A%E6%90%AD%E5%B9%B3%E5%8F%B0/%E7%AC%AC04%E7%AB%A0-Kubernetes%E4%B8%8EVolcano%E8%B0%83%E5%BA%A6%E5%B9%B3%E5%8F%B0.md)
- [第 5 章 yunyun 平台开发：从需求到架构](%E7%AC%AC%E4%BA%8C%E8%BE%91%EF%BC%9A%E6%90%AD%E5%B9%B3%E5%8F%B0/%E7%AC%AC05%E7%AB%A0-yunyun%E5%B9%B3%E5%8F%B0%E5%BC%80%E5%8F%91.md)
- [第 6 章 SRE 与运维变更规范](%E7%AC%AC%E4%BA%8C%E8%BE%91%EF%BC%9A%E6%90%AD%E5%B9%B3%E5%8F%B0/%E7%AC%AC06%E7%AB%A0-SRE%E4%B8%8E%E8%BF%90%E7%BB%B4%E5%8F%98%E6%9B%B4%E8%A7%84%E8%8C%83.md)

### [第三辑前言：跑业务](%E7%AC%AC%E4%B8%89%E8%BE%91%EF%BC%9A%E8%B7%91%E4%B8%9A%E5%8A%A1/%E7%AC%AC%E4%B8%89%E8%BE%91%E5%89%8D%E8%A8%80.md)

- [第 7 章 分布式训练通信：NCCL / HCCL 与 Ring AllReduce](%E7%AC%AC%E4%B8%89%E8%BE%91%EF%BC%9A%E8%B7%91%E4%B8%9A%E5%8A%A1/%E7%AC%AC07%E7%AB%A0-%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%AD%E7%BB%83%E9%80%9A%E4%BF%A1.md)
- [第 8 章 训练任务调优与排障](%E7%AC%AC%E4%B8%89%E8%BE%91%EF%BC%9A%E8%B7%91%E4%B8%9A%E5%8A%A1/%E7%AC%AC08%E7%AB%A0-%E8%AE%AD%E7%BB%83%E4%BB%BB%E5%8A%A1%E8%B0%83%E4%BC%98%E4%B8%8E%E6%8E%92%E9%9A%9C.md)
- [第 9 章 推理引擎部署与压测](%E7%AC%AC%E4%B8%89%E8%BE%91%EF%BC%9A%E8%B7%91%E4%B8%9A%E5%8A%A1/%E7%AC%AC09%E7%AB%A0-%E6%8E%A8%E7%90%86%E5%BC%95%E6%93%8E%E9%83%A8%E7%BD%B2%E4%B8%8E%E5%8E%8B%E6%B5%8B.md)
- [第 10 章 AI Infra 工程师](%E7%AC%AC%E4%B8%89%E8%BE%91%EF%BC%9A%E8%B7%91%E4%B8%9A%E5%8A%A1/%E7%AC%AC10%E7%AB%A0-AI%20Infra%E5%B7%A5%E7%A8%8B%E5%B8%88.md)
- [第 11 章 AI Infra 行业观察与趋势判断](%E7%AC%AC%E4%B8%89%E8%BE%91%EF%BC%9A%E8%B7%91%E4%B8%9A%E5%8A%A1/%E7%AC%AC11%E7%AB%A0-AI%20Infra%E8%A1%8C%E4%B8%9A%E8%A7%82%E5%AF%9F%E4%B8%8E%E8%B6%8B%E5%8A%BF%E5%88%A4%E6%96%AD.md)

### 结语

- [后记](%E5%90%8E%E8%AE%B0.md)

## 双语维护

中文文件沿用原目录，英文文件位于 [en/](en/README.md)。修改正文或原图时，请同步更新对应英文页面，再运行：

```sh
python3 scripts/check_translations.py
```

页面对应关系与源文件摘要记录在 [translations.json](translations.json)，GitHub Actions 会检查遗漏、失效的本地链接及需要同步的修改。具体操作见 [TRANSLATIONS.md](TRANSLATIONS.md)。

## 许可证

以下保留原 README 的许可证说明：

> 本书采用开源电子书形式发布，允许非商业用途的分享与修改。具体许可证待定。

上游仓库同时包含 Apache License 2.0 格式的 [LICENSE](LICENSE) 文件；两处原始声明均予保留。
