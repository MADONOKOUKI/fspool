import os
import pandas as pd
import torch
import numpy as np


data = []
for path in os.listdir('logs'):
    if not 'mnistc' in path:
        continue

    _, model, cat, num = path.split('-')

    log = torch.load(f'logs/{path}')
    test_acc = log['tracker']['test_acc']
    last_epoch = test_acc[0]
    acc = np.mean(last_epoch)

    data.append((model, cat, num, acc))

data = pd.DataFrame(data)
data.columns = ['model', 'category', 'num', 'acc']
grouped = data.groupby(['model', 'category'])
print(100 * grouped.std().round(3))
print(100 * grouped.mean().round(3))
