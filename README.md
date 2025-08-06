# DistillKit

[Technical Report](https://arcee-ai-distillkit.my.canva.site/)


## Overview

DistillKit is an open-source research effort in model distillation by Arcee.AI. Our goal is to provide the community with easy-to-use tools for researching, exploring, and enhancing the adoption of open-source Large Language Model (LLM) distillation methods. This release focuses on practical, effective techniques for improving model performance and efficiency.

## Features

- Logit-based Distillation (models must be the same architecture)
- Hidden States-based Distillation (models can be different architectures)
- Support for Supervised Fine-Tuning (SFT) - DPO and CPT to come at a later date.
- **New in this version:** A user-friendly GUI to configure and run distillation experiments.

## Recent Updates

This version of DistillKit includes a new graphical user interface (GUI) and significant code refactoring to improve usability and maintainability. These changes were implemented by **@MayankAgrawalG** from **@AtmnLabs**.

### Key Changes:

*   **Streamlit GUI**: A new web-based GUI has been added to allow users to easily configure and run the distillation scripts. This makes it much easier to experiment with different models, datasets, and training parameters without having to edit the code directly.
*   **Centralized Configuration**: The configurations for all distillation scripts have been moved to a central `config.py` file. This makes them easier to manage and modify.
*   **Command-line Configuration**: The distillation scripts now accept a path to a JSON configuration file via a `--config` command-line argument. This allows for greater flexibility and makes it possible to run experiments from the command line with different configurations.

## Installation

### Quick Install

For a quick and easy installation, you can use our setup script:

```bash
./setup.sh
Manual Installation
If you prefer to install dependencies manually, follow these steps:

Install basic requirements:

pip install torch wheel ninja packaging
Install Flash Attention:

pip install flash-attn
Install DeepSpeed:

pip install deepspeed
Install remaining requirements:

pip install -r requirements.txt
Usage
GUI
To launch the new GUI, use the following command:

streamlit run gui.py
From the GUI, you can:

Select which distillation script to run.
Edit the configuration for the selected script.
Run the script and view the live output.
Export the configuration as a JSON file.
Command Line
To launch DistillKit from the command line, use the following command:

accelerate launch <script_name>.py
You can replace <script_name>.py with whichever script you want to use (distil_logits.py, distil_hidden.py, or dpo_distil_logits.py).

You can also provide a custom configuration file:

accelerate launch <script_name>.py --config /path/to/your/config.json
Advanced Configurations
If you wish to use DeepSpeed, Fully Sharded Data Parallel (FSDP), or Megatron sharding, you can set up your configuration using:

accelerate config
Follow the prompts to configure your desired setup.

DeepSpeed Configurations
We provide sample DeepSpeed configuration files in the ./deepspeed_configs directory. These configurations are shamelessly stolen from the Axolotl (thanks to Wing Lian and the Axolotl team for their excellent work!).

To use a specific DeepSpeed configuration, you can specify it in your accelerate config.

Distillation Methods
DistillKit supports two primary distillation methods:

Logit-based Distillation: This method transfers knowledge from a larger teacher model to a smaller student model by using both hard targets (actual labels) and soft targets (teacher logits). The soft target loss, computed using Kullback-Leibler (KL) divergence, encourages the student to mimic the teacher's output distribution. This method enhances the student model's generalization and efficiency while maintaining performance closer to the teacher model.

Hidden States-based Distillation: This method involves transferring knowledge by aligning the intermediate layer representations of the student model with those of the teacher model. This process enhances the student's learning by providing richer, layer-wise guidance, improving its performance and generalization. This method allows for cross-architecture distillation, providing flexibility in model architecture choices.

Performance and Memory Requirements
While the implementation of DistillKit is relatively straightforward, the memory requirements for distillation are higher compared to standard SFT. We are actively working on scaling DistillKit to support models larger than 70B parameters, which will involve advanced techniques and efficiency improvements.

Experimental Results
Our experiments have shown promising results in both general-purpose and domain-specific tasks. Key findings include:

Both logit-based and hidden states-based distillation methods show improvements over standard SFT across most benchmarks.
Significant performance gains were observed when distilling models for domain-specific tasks.
Using the same training dataset for distillation as was used for the teacher model can lead to higher performance gains.
For detailed results and analysis, please refer to our case studies and experimental here.

Arcee-Labs
This release marks the debut of Arcee-Labs, a division of Arcee.ai dedicated to accelerating open-source research. Our mission is to rapidly deploy resources, models, and research findings to empower both Arcee and the wider community. In an era of increasingly frequent breakthroughs in LLM research, models, and techniques, we recognize the need for agility and adaptability. Through our efforts, we strive to significantly contribute to the advancement of open-source AI technology and support the community in keeping pace with these rapid developments.

Future Directions
We are excited to see how the community will use and improve DistillKit. Future releases will include Continued Pre-Training (CPT) and Direct Preference Optimization (DPO) distillation methods. We welcome community contributions in the form of new distillation methods, training routine improvements, and memory optimizations.

Contributing
We welcome contributions from the community! If you have ideas for improvements, new features, or bug fixes, please feel free to open an issue or submit a pull request.

Contact
For more information about Arcee.AI and our training platform, visit our website at https://arcee.ai.

For technical questions or support, please open an issue in this repository.

Acknowledgments
While our work is ultimately quite different - this project was inspired by Towards Cross-Tokenizer Distillation: the Universal Logit Distillation Loss for LLMs. We thank the authors for their efforts and contributions. We would like to thank the open-source community and all at arcee.ai who have helped make DistillKit possible. We're just getting started.

