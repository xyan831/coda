# import module
import torch

# install torch for cuda 12.2
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# check if cuda available
print(torch.cuda.is_available())
