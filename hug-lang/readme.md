
**Setting up a Python environment, installing dependencies, configuring GPU usage, and running a transformer model with LangChain.**

1) Create a Virtual Environment
Install Requirements
setup hugface token
huggingface-cli login

download the model from hugging face model directory
ex:1  text summarization task with hugging face

2) Running on the GPU machine 


If you don’t have CUDA installed, follow the official installation guide:
  -- Download nvidia https://developer.nvidia.com/cuda-downloads -- CUDA Toolkit 

  To check which CUDA version you have installed, run:

    nvcc --version

If you have an NVIDIA GPU, install the CUDA-enabled version of PyTorch.
Run the following command (replacing cu126 with your CUDA version):

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
  --> HERE  (12.8 cuda toolkit -- 128)

4. Check for GPU Availability
Run the following Python code to verify that your GPU is available:

```
import torch

####### Check if GPU is available
gpu_available = torch.cuda.is_available()
device_name = torch.cuda.get_device_name(0) if gpu_available else "No GPU found"

print(f"GPU Available: {gpu_available}")
print(f"GPU Name: {device_name}")

```

If torch.cuda.is_available() returns False, ensure that:

You have an NVIDIA GPU.
The correct version of CUDA is installed.
You installed the CUDA-enabled version of PyTorch.

5. Set Device in Pipeline
Once GPU availability is confirmed, specify the device in the transformer pipeline.

```
from transformers import pipeline

# Load the model and set device to GPU (device=0)
model = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.1",
    device=0  # Use GPU (0 refers to the first GPU)
)

# Generate text
output = model("What is LangChain?")
print(output)

``` 

If using a CPU instead of a GPU, change device=0 to device=-1.
