# model.py
import torch.nn as nn

class LinearRegressionModel(nn.Module):
    """
    简单的线性回归模型
    """
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.fc = nn.Linear(1, 1)  # 输入特征1维，输出1维

    def forward(self, x):
        return self.fc(x)
