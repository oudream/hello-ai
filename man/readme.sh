#!/usr/bin/env bash


jupyter notebook --no-browser --port 2290 --ip=0.0.0.0 --notebook-dir=/opt


### 正在开发的项目

# https://github.com/google-research/google-research

# 数据分析项目
# https://github.com/slackliu/data_analysis_project
# https://github.com/wesm/pydata-book



### colab
# https://juejin.im/post/5d07b8cd6fb9a07eb94f8c94
# in jupyter
from google.colab import drive
drive.mount("/content/drive")

print('Files in Drive:')
!ls /content/drive/'My Drive'

!cd /content/drive/'My Drive'/'Colab Notebooks'
!ls -R