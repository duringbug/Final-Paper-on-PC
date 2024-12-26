# training.py
import torch
import torch.optim as optim
import torch.nn as nn

def train_local_model(model, data, targets, epochs=5, learning_rate=0.4):
    """
    训练客户端的本地模型
    """
    criterion = nn.MSELoss()  # 均方误差损失
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, targets)
        loss.backward()
        optimizer.step()

    return model.state_dict()  # 返回更新后的模型参数

def federated_averaging(models_state_dicts):
    """
    聚合多个客户端的模型参数
    """
    # 假设每个客户端上传相同数量的数据，直接做平均
    avg_state_dict = {}
    for key in models_state_dicts[0].keys():
        avg_state_dict[key] = torch.mean(torch.stack([state_dict[key].float() for state_dict in models_state_dicts]), dim=0)
    return avg_state_dict
