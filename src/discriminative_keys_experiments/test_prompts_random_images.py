import sys
sys.path.append("./../")
import torch
from utils import *
from tqdm import tqdm

def print_top_k_classes(preds, k):
    return sorted(preds.items(), key=lambda x: x[1])[::-1][:k]

model = torch.load("./../../checkpoints/l2p_cifar_100_trained.pt")
model.eval()

pool_size = model.prompt.pool_size
n_classes = 100

rand_batch = torch.randn(16, 3, 224, 224)

pred_class = {x: {c: 0 for c in range(100)} for x in range(pool_size)}

n_iters = 10

with tqdm(total=n_iters*pool_size) as pbar:
    for _ in range(n_iters):
        rand_batch = torch.randn(8, 3, 224, 224)
        for i in range(pool_size):
            res = prompt_forward(model, rand_batch, i)
            preds = res["logits"].argmax(dim=1)
            for pred in preds:
                pred_class[i][pred.item()] += 1
            pbar.update(1)

for i in range(pool_size):
    print(f"Prompt {i}")
    print(print_top_k_classes(pred_class[i], 5))


