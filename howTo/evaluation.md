## 评测

### 环境包与数据集准备

- 克隆opencompass仓库安装依赖

```bash
git clone https://github.com/open-compass/opencompass
cd opencompass
pip install -e .
```

- 准备数据并解压

```bash
cp /share/temp/datasets/OpenCompassData-core-20231110.zip /root/opencompass/
unzip OpenCompassData-core-20231110.zip
```

后面评测的时候发现lawbench的数据包并没有整合在其中，所以这里单独从lawbench项目库中将数据包复制过来

```bash
git clone https://gitee.com/ljn20001229/LawBench.git
cp -r /root/personal_assistant/LawBench/data/one_shot /root/personal_assistant/opencompass/data/lawbench
cp -r /root/personal_assistant/LawBench/data/zero_shot /root/personal_assistant/opencompass/data/lawbench
```

### 评测运行

- opencompass评测可以使用一些写好的config配置文件做评测，也可以直接在命令行写指令 

```bash
python run.py --datasets ceval_ppl mmlu_ppl \
--hf-path huggyllama/llama-7b \  # HuggingFace 模型地址
--model-kwargs device_map='auto' \  # 构造 model 的参数
--tokenizer-kwargs padding_side='left' truncation='left' use_fast=False \  # 构造 tokenizer 的参数
--max-out-len 100 \  # 最长生成 token 数
--max-seq-len 2048 \  # 模型能接受的最大序列长度
--batch-size 8 \  # 批次大小
--no-batch-padding \  # 不打开 batch padding，通过 for loop 推理，避免精度损失
--num-gpus 1  # 运行该模型所需的最少 gpu 数
```

想要换不同的模型和数据集可以直接在参数后更改配置文件和模型地址，非常方便

- 直接在命令行写指令进行评测 

  `/root/personal_assistant/config/a/work_dirs/hf_merge`是sft之后的模型路径，这里必须得是完整的

```bash
python run.py \ --datasets ceval_gen \ 
--hf-path /root/personal_assistant/config/a/work_dirs/hf_merge \ 
--tokenizer-path /root/personal_assistant/config/a/work_dirs/hf_merge\ 
--tokenizer-kwargs padding_side='left' truncation='left' trust_remote_code=True \ 
--model-kwargs device_map='auto' trust_remote_code=True \ 
--max-seq-len 2048 \ 
--max-out-len 1000 \ 
--batch-size 2 \ 
--num-gpus 1 \ 
--debug
```

### 评测结果

#### 在ceval数据上的评测结果

对比对象主要是微调后的模型，原基准模型，与量化模型在ceval中eval-law数据上的对比

- 基础模型得分

  <img src=".\assets\image-20240204202322136.png" alt="image-20240204202322136" />

- 微调模型得分

  <img src=".\assets\image-20240204202313450.png" alt="20240204202313450" />

- 微调后量化模型得分

  <img src=".\assets\image-20240204202259676.png" alt="20240204202259676" />

  对比来看，模型训练之后对eval-law得分明显提高，但是量化评分不太理想。不过评测好像具有随机性，一次评测的结果也不能代表模型的整体性能

#### 在lawbench上的结果

因为lawbench长文本测评，测评时间需要十几个小时，目前还没有出结果，waiting......

<img src=".\assets\image-20240204202247277.png" alt="20240204202247277" />
