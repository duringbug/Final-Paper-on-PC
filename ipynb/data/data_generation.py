# data_generation.py
import numpy as np
import torch

def generate_data(num_samples=100):
    """
    生成简单的线性数据 (y = 2 * x + 1) 并加入噪声
    """
    X = np.random.rand(num_samples, 1)  # 输入数据
    Y = 2 * X + 1 + np.random.randn(num_samples, 1) * 0.1  # 线性目标数据，加入噪声
    return torch.tensor(X, dtype=torch.float32), torch.tensor(Y, dtype=torch.float32)
