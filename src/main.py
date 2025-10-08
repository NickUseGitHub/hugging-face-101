from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from diffusers import StableDiffusionPipeline
import torch
import uuid
import os

app = FastAPI()

# Select device (MPS for Apple Silicon, fallback to CPU)
device = "mps" if torch.backends.mps.is_available() else "cpu"

# Load model once at startup
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    safety_checker = None,
    requires_safety_checker = False
)
pipe = pipe.to(device)

# Directory to save outputs
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.get("/generate")
async def generate_image(prompt: str = Query(..., description="Text prompt for the image")):
    # Generate image
    image = pipe(prompt).images[0]

    # Save with unique name
    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    image.save(filepath)

    # Return the image file
    return FileResponse(filepath, media_type="image/png", filename=filename)
