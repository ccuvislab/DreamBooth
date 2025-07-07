import os
import subprocess
import argparse

os.chdir("./diffusers/examples/dreambooth")

command = [
    "python", "train_dreambooth.py",
    "--pretrained_model_name_or_path", "runwayml/stable-diffusion-v1-5", # 使用預訓練模型
    "--instance_data_dir", "/instance/image/path/", # 替換成實例圖片的路徑 (特定風格場景影像 eg. BDD100k)，約5~10張即可
    "--class_data_dir", "/class/image/path/", # 替換成類別圖片的路徑 (一般場景影像)，約3張即可
    "--instance_prompt", "A photo of [unique identifier] [name]", # 替換成實例提示語句，[unique identifier]需要是無任何意義的形容詞 (eg. A photo of xyz urban scene)
    "--class_prompt", "A photo of [name]", # 替換成類別提示語句 (eg. A photo of urban scene)
    "--with_prior_preservation", # 是否使用類別圖片進行先驗保留 (建議使用，需和--prior_loss_weight一起使用)
    "--prior_loss_weight", "1", # 先驗損失權重 (default值為1，調整此值可影響類別圖片的影響程度)
    "--num_class_images", "100", # 類別圖片數量 (若準備不到 eg. 100張圖片，會自動生成與已有類別圖片相關影像至100張)
    "--output_dir", "/output/model/path/", # 替換成輸出模型的路徑
    "--resolution", "512",
    "--train_text_encoder",
    "--train_batch_size", "2", # 訓練批次大小 (根據GPU記憶體大小調整)
    "--sample_batch_size", "2", # 生成樣本批次大小 (根據GPU記憶體大小調整)
    "--max_train_steps", "1000", # 訓練總步數 
    "--checkpointing_steps", "500", # 每固定步數會自動儲存模型檢查點 (建議別設置太小，模型資料夾會變很大，占空間)
    "--gradient_accumulation_steps", "1",
    "--gradient_checkpointing",
    "--learning_rate", "1e-6",
    "--lr_scheduler", "constant",
    "--lr_warmup_steps", "0",
    "--validation_prompt", "A photo of [unique identifier] [name]", # 替換成驗證提示語句 (需與instance_prompt一致)
    "--num_validation_images", "4", # 驗證圖片數量
    "--mixed_precision", "fp16",
    "--enable_xformers_memory_efficient_attention",
    "--set_grads_to_none"
]

subprocess.run(command)