# From the Ground Up to the Model: Notes on AI Infrastructure

**[中文](../README.md) | English**

An English edition of **从地皮到模型：AI Infra 杂谈**, by **Wang Honglei (王洪磊)**.

[Original Chinese repository](https://gitee.com/honglei_wang/Notes-on-AI-Infrastructure) · [Bilingual edition and maintenance notes](../TRANSLATIONS.md)

The book follows the entire AI infrastructure chain: data center construction, GPU cluster delivery, networking, Kubernetes scheduling, platform development, SRE, distributed training, inference, and the engineer's career.

It is written for engineers entering AI infrastructure, cloud and SRE practitioners moving into model infrastructure, technical managers building compute facilities, and developers interested in practical AI systems.

This edition includes all **11 chapters**, the **three part introductions**, the **preface**, and the **afterword**. Every page links to its Chinese counterpart. The original 24 figures have English equivalents presented as Mermaid diagrams or tables; GitHub renders the diagrams directly.

## Contents

- [Preface](preface.md)

### [Part I Introduction: Building the Foundation](part-1-infrastructure/introduction.md)

- [Chapter 1: Data Center and AI Data Center Construction](part-1-infrastructure/ch01-data-center-construction.md)
- [Chapter 2: GPU Cluster Hardware Selection and Delivery](part-1-infrastructure/ch02-gpu-selection-and-delivery.md)
- [Chapter 3: AI Networking and RDMA/RoCEv2](part-1-infrastructure/ch03-networking-rdma-rocev2.md)

### [Part II Introduction: Building the Platform](part-2-platforms/introduction.md)

- [Chapter 4: Kubernetes and Volcano Scheduling](part-2-platforms/ch04-kubernetes-volcano.md)
- [Chapter 5: Developing yunyun—From Requirements to Architecture](part-2-platforms/ch05-yunyun-platform.md)
- [Chapter 6: SRE and Operational Change Management](part-2-platforms/ch06-sre-change-management.md)

### [Part III Introduction: Running the Workloads](part-3-workloads/introduction.md)

- [Chapter 7: Distributed Training Communication—NCCL, HCCL, and Ring AllReduce](part-3-workloads/ch07-distributed-training-communication.md)
- [Chapter 8: Training Tuning and Troubleshooting](part-3-workloads/ch08-training-tuning-troubleshooting.md)
- [Chapter 9: Inference Engine Deployment and Load Testing](part-3-workloads/ch09-inference-deployment-benchmarking.md)
- [Chapter 10: The AI Infrastructure Engineer](part-3-workloads/ch10-ai-infrastructure-engineer.md)
- [Chapter 11: AI Infrastructure Industry Observations and Trends](part-3-workloads/ch11-industry-observations.md)

### Closing

- [Afterword](afterword.md)

## About this translation

This is an AI-assisted English translation and editorial adaptation of the Chinese source at commit `f78f73a7ebb4b8c513f49788f8ce6b8ba762b002`. It preserves the chapter structure, technical examples, reference lists, and the author's explicitly labeled opinions. Some repetitive wording has been condensed, and figures have been redrawn or expressed as tables. First-person statements belong to the original author.

This is a translation of that source edition, not an independently updated technical reference. Hardware estimates, software settings, code examples, and forecasts retain the source's context. Where the source contains internal inconsistencies, brief notes identify them. Technical and language review is welcome.

Paths such as `docs/...` and `yidian/...` in reference lists are the author's original reference names; those materials were not included in the source repository. Their names are retained for traceability.

## Maintaining both languages

The Chinese edition remains in the original directories; English pages live under `en/`. Update paired pages together, record the reviewed source revision, and run:

```sh
python3 scripts/check_translations.py
```

[TRANSLATIONS.md](../TRANSLATIONS.md) explains how the page manifest, source and image hashes, navigation, and CI checks keep the editions aligned.

## Attribution and license notices

The original author is Wang Honglei. The upstream history, Chinese text, original figures, and [LICENSE](../LICENSE) are preserved. This repository adds the English edition and bilingual maintenance tools.

Upstream includes an Apache License 2.0 file. Its original README also says that noncommercial sharing and modification are allowed and that the specific license is pending. Both original notices are retained in this repository.
