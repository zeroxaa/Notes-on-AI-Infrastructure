<!-- bilingual-navigation:start -->
[中文原文](../../%E7%AC%AC%E4%B8%89%E8%BE%91%EF%BC%9A%E8%B7%91%E4%B8%9A%E5%8A%A1/%E7%AC%AC%E4%B8%89%E8%BE%91%E5%89%8D%E8%A8%80.md) | [English](introduction.md) | [Contents](../README.md) | [Previous](../part-2-platforms/ch06-sre-change-management.md) | [Next](ch07-distributed-training-communication.md)

English translation of Wang Honglei's Chinese original. Edition and maintenance notes: [TRANSLATIONS.md](../../TRANSLATIONS.md).
<!-- bilingual-navigation:end -->

# Part III Introduction: Running the Workloads

Once the platform is built, the real workloads can begin. Part III covers the two central workloads—training and inference—and the people and judgment that support them.

Large model training is the most visible AI infrastructure use case. When thousands of GPUs run a single job, a problem in communication, storage, the framework, or configuration can interrupt training or reduce efficiency. Communication matters because gradient synchronization takes substantial time. NCCL timeouts require investigation because the slowest node can hold everyone back. A high `data_time` means GPUs are waiting for data.

Inference is the other central workload. After training, a model must become a service. Inference emphasizes latency and cost: users want the first token quickly, while the platform wants each GPU to serve more users. Engines such as vLLM, TensorRT-LLM, and SGLang balance latency and throughput.

The five chapters in Part III cover:

- Distributed training communication: NCCL, HCCL, Ring AllReduce, and why communication becomes a bottleneck.
- Training tuning and troubleshooting: an investigative approach to failed jobs, from parameters to logs.
- Inference engine deployment and load testing: choosing vLLM, TensorRT-LLM, or SGLang in production.
- The AI infrastructure engineer: what the role involves and the capabilities and judgment it requires.
- AI infrastructure industry observations and trends: views on the current stack, Chinese alternatives, and future directions.

Working workloads are the final deliverable of AI infrastructure. Every preceding investment in facilities, platforms, and operating standards serves this moment: training runs efficiently, inference remains stable, and costs stay under control.
