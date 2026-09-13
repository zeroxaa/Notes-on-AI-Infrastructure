<!-- bilingual-navigation:start -->
[中文原文](../../%E7%AC%AC%E4%B8%80%E8%BE%91%EF%BC%9A%E9%80%A0%E5%9C%BA%E5%AD%90/%E7%AC%AC%E4%B8%80%E8%BE%91%E5%89%8D%E8%A8%80.md) | [English](introduction.md) | [Contents](../README.md) | [Previous](../preface.md) | [Next](ch01-data-center-construction.md)

English translation of Wang Honglei's Chinese original. Edition and maintenance notes: [TRANSLATIONS.md](../../TRANSLATIONS.md).
<!-- bilingual-navigation:end -->

# Part I Introduction: Building the Foundation

This book divides the AI infrastructure chain into three parts. Part I covers the physical foundation and basic hardware of an AI data center.

Discussions of large models often begin with algorithms, frameworks, and compute capacity. But when you actually need to build a cluster for training and inference, the first step is often finding a site that can supply enough power, remove enough heat, and support the network layout.

AI data centers and traditional data centers are fundamentally different. A conventional CPU facility might put more than a dozen servers in one rack and consume only a few kilowatts. A GPU facility can reach tens of kilowatts with just a few training nodes in the same space. Air cooling that sufficed in the CPU era approaches its physical limits in the GPU era. Optical transceivers become too hot to touch, fans become essential equipment, and power supplies move from single-phase 220 V to three-phase 380 V.

These changes mean that AI infrastructure engineers need to understand more than software. Electricity, cooling, rack layout, and fiber length directly affect network performance, training stability, and operating costs.

The three chapters in Part I cover:

- Data center and AI data center construction: constraints involving power, cooling, site selection, and physical deployment.
- GPU cluster hardware selection and delivery: choosing training, inference, and Chinese accelerators, and accepting equipment after delivery.
- AI networking and RDMA/RoCEv2: why ordinary Ethernet is insufficient, and how RDMA and RoCEv2 support distributed training.

These chapters form the foundation for the later discussions of Kubernetes, Volcano, training communication, and inference deployment. If the foundation is unstable, even an elegant upper layer will struggle to run well.
