# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 3:49
# @Author  : Yujin Wang


import torch
from IPython.display import Image,clear_output
clear_output()
print('Setup complete, Using torch %s %s' % (torch.__version__,torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))

import torch
print(torch.cuda.get_device_capability(0))