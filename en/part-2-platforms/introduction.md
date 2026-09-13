<!-- bilingual-navigation:start -->
[中文原文](../../%E7%AC%AC%E4%BA%8C%E8%BE%91%EF%BC%9A%E6%90%AD%E5%B9%B3%E5%8F%B0/%E7%AC%AC%E4%BA%8C%E8%BE%91%E5%89%8D%E8%A8%80.md) | [English](introduction.md) | [Contents](../README.md) | [Previous](../part-1-infrastructure/ch03-networking-rdma-rocev2.md) | [Next](ch04-kubernetes-volcano.md)

English translation of Wang Honglei's Chinese original. Edition and maintenance notes: [TRANSLATIONS.md](../../TRANSLATIONS.md).
<!-- bilingual-navigation:end -->

# Part II Introduction: Building the Platform

Once the site, hardware, and network are ready, the next step is to make those resources usable. This is the purpose of the platform.

A platform must do more than connect machines to a network. It needs to let multiple teams share GPUs, submit and schedule training jobs, deploy and scale inference services, manage changes, and respond to failures.

Kubernetes has become the foundation of most platforms. It was originally designed for microservices, but scheduling Pods individually with its native scheduler can cause problems for AI training. If a job requires eight GPU Pods to start together and only seven are scheduled, the entire job can stall. Batch schedulers such as Volcano address this problem.

Scheduling is only part of the platform. A training platform also needs to manage images, data, logs, monitoring, quotas, and permissions. An inference platform must manage model versions, canary releases, autoscaling, and costs. Native Kubernetes resources cannot provide all these capabilities by themselves; substantial engineering is needed above them.

The three chapters in Part II cover:

- Kubernetes and Volcano scheduling: why the native scheduler does not fit training jobs, and how to use Volcano's gang scheduling and queues.
- Developing the yunyun platform: how an internal, integrated training and inference platform grew from requirements into an architecture.
- SRE and operational change management: controlling changes in large clusters, rolling them back, and recovering from incidents.

The platform connects infrastructure with applications. A poorly designed platform makes researchers spend their days requesting resources, writing YAML, and searching logs. A good platform lets them focus on models and algorithms.
