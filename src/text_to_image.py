from diffusers import StableDiffusionPipeline
import torch

# Use Apple's MPS backend (works on M1/M2)
device = "mps" if torch.backends.mps.is_available() else "cpu"

# Load the pre-trained model (smallest one to get started fast)
model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    safety_checker = None,
    requires_safety_checker = False
)
pipe = pipe.to(device)

prompt = "Beautiful japanese full-image girl dress bikini"
image = pipe(prompt).images[0]

image.save("output.png")
