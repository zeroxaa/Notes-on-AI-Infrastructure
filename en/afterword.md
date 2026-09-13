<!-- bilingual-navigation:start -->
[中文原文](../%E5%90%8E%E8%AE%B0.md) | [English](afterword.md) | [Contents](README.md) | [Previous](part-3-workloads/ch11-industry-observations.md)

English translation of Wang Honglei's Chinese original. Edition and maintenance notes: [TRANSLATIONS.md](../TRANSLATIONS.md).
<!-- bilingual-navigation:end -->

# Afterword

After finishing the first draft, my strongest impression is that AI infrastructure is a web of connections rather than a single technology.

That web begins with the site itself. You need to consider whether the facility can supply enough electricity, remove enough heat, and accommodate the necessary fiber runs. Above that come GPUs, networks, scheduling, platforms, training, and inference. Every layer depends on the one below and affects the one above. A break anywhere makes the whole system harder to operate.

Working in this web, it is difficult to become a leading expert in every field. You can specialize in networking, training communication, or platform development, but you also need enough understanding of the other areas to know where to start investigating a failure and where the boundaries lie when designing a system.

This is the value of an AI infrastructure engineer. The job is to keep an entire system running continuously, reliably, and efficiently. You need to write code, read logs, and communicate with suppliers, facility engineers, network teams, and algorithm researchers. You must make tradeoffs between cost and performance, stability and new features, and ideal designs and real constraints.

This book is only a starting point. The AI infrastructure stack continues to evolve rapidly: new GPUs, networks, inference engines, schedulers, and Chinese accelerator ecosystems. Some of what is written today may be outdated in two or three years. I hope the end-to-end perspective—from the ground up to the model—retains some lasting value.

If you are entering this field, I hope this book helps you build a map. If you already work in it, I hope some chapters resonate with your experience or offer a new idea.

Technology ultimately exists to help researchers build better models and users access better services. AI infrastructure engineers build the roads and bridges that make this possible.

Thank you for reading.
