from diffusers import DiffusionPipeline, UNet2DConditionModel
from transformers import CLIPTextModel
import torch
import os

trained_model_path = "/output/model/path/" # 替換成train.py中的output_dir路徑

unet = UNet2DConditionModel.from_pretrained(trained_model_path + '/unet')
text_encoder = CLIPTextModel.from_pretrained(trained_model_path + '/text_encoder')

pipeline = DiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", 
    unet=unet, 
    text_encoder=text_encoder, 
    dtype=torch.float16,
    safety_checker=None,
).to("cuda")

prompt = "A photo of [unique identifier] [name]" # 可以直接使用train.py中的instance prompt
negative_prompt = "watermark, distorted shapes, bad, low quality"

generated_img_path = "/generated/image/path/" # 替換成生成圖片的路徑
if not os.path.exists(generated_img_path):
    os.makedirs(generated_img_path)

for i in range(1, 3):
    image = pipeline(prompt=prompt, negative_prompt=negative_prompt, num_inference_steps=100, guidance_scale=7.5, height=512, width=512).images[0]

    image_path = os.path.join(generated_img_path, f"generated_{i}.png")  
    image.save(image_path)

