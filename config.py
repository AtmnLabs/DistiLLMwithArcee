
# This file will store the configurations for the distillation scripts.
# By centralizing the configurations, we can easily manage them from the GUI.

LOGITS_CONFIG = {
    "project_name": "distil-logits",
    "dataset": {
        "name": "mlabonne/FineTome-100k",
        "split": "train",
        # "num_samples": , # You can pass a number here to limit the number of samples to use.
        "seed": 42
    },
    "models": {
        "teacher": "arcee-ai/Arcee-Spark",
        "student": "Qwen/Qwen2-1.5B"
    },
    "tokenizer": {
        "max_length": 4096,
        "chat_template": "{% for message in messages %}{% if loop.first and messages[0]['role'] != 'system' %}{{ '<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n' }}{% endif %}{{'<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>' + '\n'}}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant\n' }}{% endif %}"
    },
    "training": {
        "output_dir": "./results",
        "num_train_epochs": 3,
        "per_device_train_batch_size": 1,
        "gradient_accumulation_steps": 8,
        "save_steps": 1000,
        "logging_steps": 1,
        "learning_rate": 2e-5,
        "weight_decay": 0.05,
        "warmup_ratio": 0.1,
        "lr_scheduler_type": "cosine",
        "resume_from_checkpoint": None,  # Set to a path or True to resume from the latest checkpoint
        "fp16": False,
        "bf16": True
    },
    "distillation": {
        "temperature": 2.0,
        "alpha": 0.5
    },
    "model_config": {
        "use_flash_attention": True
    }
    # "spectrum": {
    #     "layers_to_unfreeze": "/workspace/spectrum/snr_results_Qwen-Qwen2-1.5B_unfrozenparameters_50percent.yaml" # You can pass a spectrum yaml file here to freeze layers identified by spectrum.
    # }
}
HIDDEN_CONFIG = {
    "project_name": "distil-multilayer",
    "dataset": {
        "name": "mlabonne/FineTome-100k",
        "split": "train",
        "num_samples": 1000, # You can pass a number here to limit the number of samples to use.
        "seed": 42
    },
    "models": {
        "teacher": "arcee-ai/Arcee-Spark",
        "student": "Qwen/Qwen2-1.5B"
    },
    "tokenizer": {
        "max_length": 4096,
        "chat_template": "{% for message in messages %}{% if loop.first and messages[0]['role'] != 'system' %}{{ '<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n' }}{% endif %}{{'<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>' + '\n'}}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant\n' }}{% endif %}"
    },
    "training": {
        "output_dir": "./results",
        "num_train_epochs": 3,
        "per_device_train_batch_size": 1,
        "gradient_accumulation_steps": 8,
        "save_steps": 1000,
        "logging_steps": 2,
        "save_total_limit": 2,
        "learning_rate": 2e-5,
        "weight_decay": 0.01,
        "warmup_ratio": 0.2,
        "lr_scheduler_type": "linear",
        "resume_from_checkpoint": None,
        "fp16": False,
        "bf16": True,
        "max_grad_norm": 1.0,
        "group_by_length": False
    },
    "distillation": {
        "temperature": 2.0,
        "alpha": 0.5
    },
    "model_config": {
        "use_flash_attention": True
    }
}
DPO_CONFIG = {
    "project_name": "dpo-distil-logit",
    "dataset": {
        "name": "Intel/orca_dpo_pairs",
        "split": "train",
        "val_split": 0.05,          # % of samples held out for eval
        "seed": 42,
    },
    "models": {
        "student": "Qwen/Qwen2.5-1.5B-Instruct",
        "teacher": "Qwen2.5-3B-DPO-intel-orca/merge", # Dpo trained model
    },
    "tokenizer": {
        "pad_side": "left",
        "chat_template": None,      # keep default that ships with Qwen
    },
    "lora": {                       # DPO requires higher Vram so LORA is suitable for consumer based GPUS <= 24GB Vram
        "r": 16,
        "alpha": 16,
        "dropout": 0.05,
        "target_modules": [
            "k_proj","v_proj","q_proj","o_proj",
            "gate_proj", "up_proj", "down_proj"
        ],
    },
    "quant": {
        "bits": 4,
        "quant_type": "nf4",
        "compute_dtype": "bfloat16",
    },
    "dpo": {
        "num_train_epochs": 3,
        "per_device_batch": 1,
        "grad_accum": 4,
        "lr": 5e-5,
        "logging_steps": 50,
        "save_steps": 1000,
        "max_length": 4096,
        # KD
        "kd_temperature": 1.0,
        "kd_weight": 1e-3,
    },
    "wandb": {
        "entity": "my-team",
        "name": "exp-name",  # run name
        "tags": ["dpo", "knowledge-distillation"],
    },
    "paths": {
        "output_dir": "path-to-save-ckpts",
        "final_merged": "final-lora-merged-model",
    }
}
