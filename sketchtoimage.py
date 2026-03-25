# generateimage.py

import torch
from diffusers import StableDiffusionControlNetPipeline
from PIL import Image
import matplotlib.pyplot as plt

# Load model
pipe = StableDiffusionControlNetPipeline.from_pretrained("diffusion_model/").to("cuda")
pipe.safety_checker = None

# Preprocess sketch
def preprocess_sketch(image_path):
    sketch = Image.open(image_path).convert("L")  # Convert to grayscale
    sketch = sketch.resize((512, 512))           # Resize image
    return sketch

# Input sketch
image_path = "rough_drawing.png"
sketch = preprocess_sketch(image_path)

# User prompt
prompt = input("Enter your prompt: ")

# Generate image
generated_image = pipe(prompt, image=sketch).images[0]

# Save output
generated_image_path = "generated_image.png"
generated_image.save(generated_image_path)

print(f"Generated image saved as {generated_image_path}")