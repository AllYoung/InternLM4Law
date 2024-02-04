一.环境包与数据集准备
1.克隆opencompass仓库安装依赖
git clone https://github.com/open-compass/opencompass
cd opencompass
pip install -e .
2.准备数据 并解压
cp /share/temp/datasets/OpenCompassData-core-20231110.zip /root/opencompass/
unzip OpenCompassData-core-20231110.zip
3.后面评测的时候发现lawbench的数据包并没有整合在其中，所以这里单独从lawbench项目库中将数据包复制过来
git clone https://gitee.com/ljn20001229/LawBench.git
cp -r /root/personal_assistant/LawBench/data/one_shot /root/personal_assistant/opencompass/data/lawbench
cp -r /root/personal_assistant/LawBench/data/zero_shot /root/personal_assistant/opencompass/data/lawbench
二.评测运行 
4.opencompass评测可以使用一些写好的config配置文件做评测，也可以直接在命令行写指令 
如
python run.py --datasets ceval_ppl mmlu_ppl \
--hf-path huggyllama/llama-7b \  # HuggingFace 模型地址
--model-kwargs device_map='auto' \  # 构造 model 的参数
--tokenizer-kwargs padding_side='left' truncation='left' use_fast=False \  # 构造 tokenizer 的参数
--max-out-len 100 \  # 最长生成 token 数
--max-seq-len 2048 \  # 模型能接受的最大序列长度
--batch-size 8 \  # 批次大小
--no-batch-padding \  # 不打开 batch padding，通过 for loop 推理，避免精度损失
--num-gpus 1  # 运行该模型所需的最少 gpu 数
 想要换不同的模型和数据集可以直接在参数后更改配置文件和模型地址，非常方便。

5.这里直接在命令行写指令进行评测 
/root/personal_assistant/config/a/work_dirs/hf_merge是我自己sft之后的模型路径，这里必须得是完整的。

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
三.评测结果
3.1在ceval数据上的评测结果
对比对象主要是微调后的模型，原基准模型，与量化模型在ceval中eval-law数据上的对比
1.基准模型结果




