# InternLM4Law

![robot](assets/robot.png)

## Introduction 🔊

**InternLM4Law**是一个**民法典领域**的**法律大模型**，旨在解决民法领域中常见的问题和要求，为用户提供高质量、高准确性且高专业性的法律咨询和回答。InternLM4Law是基于对[InternLM2](https://github.com/InternLM/InternLM.git)微调和利用RAG技术外挂专业知识库而得到的，主要特点如下：

- **专业性：**我们的团队将在专有的法律指令数据集上进行高效微调，确保模型具备准确的法律知识支持，并能够以专业的语气进行回答。
- **综合能力：**通过外挂专业知识库和RAG技术，我们的法律大模型将具备丰富的背景知识和能力，能够更好地理解和回答用户提出的问题。
- **可定制化：**我们将提供量化部署的模型，并产出demo，以便用户可以快速评估和使用我们的法律大模型。

## 模型demo-如何使用 💻

==demo链接==

## 数据集

### RAG数据集

**中华人民共和国民法典**：指2020年5月28日第十三届全人民代表大会第三次会议通过，自2021年1月1日起施行的《[中华人民共和国民法典](https://www.court.gov.cn/zixun-xiangqing-233181.html)》

**民法典释评**：我们还引入了三本针对**民法典的释评类书籍**作为补充数据集

### 微调数据集

**通用法律问答数据**：本项目在150k条通用法律问答数据集上进行微调，包括丰富的法律问题类型和相应的答案，例如：

- **法律概念解释**

```json
{"id": "zh_law_instruction_41954",
"conversations": [
{"from": "human",
"value": "请解释以下法律术语的涵义。\n公益诉讼"},
{"from": "gpt",
"value": "公益诉讼是指为了维护国家和社会公共利益，由依法设立的特定机关、组织或者群众团体等，行使在特定法律范围内诉讼权利，以保护、维护公共利益的一种诉讼形式。公益诉讼种类繁多，包括环境保护、消费者权益、知识产权保护、食品药品安全等方面。相关法律法规：《中华人民共和国环境保护法》、《中华人民共和国消费者权益保护法》等。"}]}
```

- **法律法规**

```json
{"instruction": "给出以下法条的具体内容:", 
"input": " 中华人民共和国民法典第二百零七条", 
"answer": " 中华人民共和国民法典第二百零七条 国家、集体、私人的物权和其他权利人的物权受法律平等保护，任何组织或者个人不得侵犯。"}
```

- **法律问题咨询**

```json
{"input": "男女双方离婚两年，年龄不到没有结婚证 又因为男方在外面找外遇出轨了。在外面与第三者同居 被我多次发现了 还是不改变抚养费也没给 这个是不是可以起诉他给抚养费并且把小孩的抚养权和小孩的姓给我？",
"output": "根据《中华人民共和国婚姻法》的规定，离婚时涉及子女的抚养问题，应当依法达成协议或者经人民法院判决。因此，您可以向法院提起诉讼，请求男方给予子女抚养费并将子女的抚养权和姓氏归您。同时，如果男方确实存在出轨行为，您可以请求法院判决男方支付精神损害赔偿。"}
```

- 法律文书理解


```json
{"id": "jud_doc_sum-909", 
"input": "段泽耀与重庆市酉水河酒业有限公司租赁合同纠纷一审民事判决书\n重庆市酉阳土家族苗族自治县人民法院\n民 事 判 决 书\n(2017)渝0242民初4437号\n原告：段泽耀，男，1976年9月12日生，土家族，本县。\n被告：重庆市酉水河酒业有限公司，住所地：重庆市酉阳县。\n组织机构代码：756225912。\n法定代表人：陈明文，该公司总经理。\n原告段泽耀诉被告重庆市酉水河酒业有限公司（以下简称酉水河公司）租赁合同纠纷一案，本院于2017年11月17日立案受理后，本案依法由本院审判员李珍适用简易程序于2017年11月29日公开开庭进行了审理。\n原告段泽耀到庭参加了诉讼，被告酉水河经传票传唤无正当理由拒不到庭参加诉讼，本院依法缺席审理。\n本案现已审理终结。\n原告段泽耀向本院提出诉讼请求：1.被告支付拖欠工资款233667.66元......\n请大致描述这篇文书的内容。", 
"output": "总结：原告与被告租赁合同纠纷一案。原告提出诉求：1、被告支付拖欠工资款233667.66元，并支付利息。被告未答辩。经查明原被告的租赁合同关系可予确认；原告按约定为被告提供挖掘机使用，被告应按约定支付原告租金；原告要求被告支付233667.66元工资款，对于已入财务账的113626元，因原告提供的证据来源不清楚，不予采信；对原告诉求的未结算入账的120041.66元，其提供未结算的票据，对这一证据不予采信，原告亦未证明挖掘机每小时租金，故对未结算入账的120041.66元，不予支持。不予支持；对其主张的逾期付款利息，亦不予支持。根据《民事诉讼法》第六十四条、第一百四十四条以及《最高人民法院关于适用<中华人民共和国民事诉讼法>的解释》第九十条的规定，判决:驳回原告诉讼请求。"}

```

- 合同类型判断


```json
{"id": "zh_contract_instruction_10",
"conversations": [
{"from": "human",
"value": "确认以下合同的类别\n深圳市劳动合同深圳市劳动合同深圳市劳动和社会保障局编制甲方（用人单位）乙方（员工）名称姓名地址性别法定代表人身份证（主要负责人）号码联系人住址联系电话联系电话根据《中华人民共和国劳动法》（以下简称《劳动法》）等有关法律法规的规定，甲乙双方按照平等自愿、诚信守法、协商一致的原则，签订本合同，共同遵守本合同所列条款。一、合同期限（一）甲乙双方同意按以下第种方式确定本合同期限。1、有固定期限：从年月日起至年月日止。2、无固定期限：从年月日起。3、以完成一定工作为期限：从年月日起至工作任务完成时止。完成工作任务的标志是。（二）试用期为（试用期包括在合同期内，如无试用期，则填写“无”）。二、工作内容乙方的工作内容（岗位或工种）为......"},
{"from": "gpt",
"value": "劳动合同"}]}
```

**民法典问答数据**：我们还专门收集了372条民法典领域的法律问答数据

```json
{"input": "法人的法定代表人如何确定?其以法人名义从事的民事活动，其法律后果是否要由法人承受?",
"output": "法人的法定代表人由谁担任,是依据法律的规定或者法人章程的规定确定的。一是根据法律规定确定。有的法律,如公司法规定了公司的法定代表人由谁担任：“公司法定代表人依照公司章程的规定,由董事长、执行董事或者经理担任,并依法登记。公司法定代表人变更,应当办理变更登记。”再如,民办教育促进法规定,民办学校的法定代表人由理事长、董事长或者校长担任。二是如果没有法律规定,就要根据法人章程来确定法人的法定代表人。法定代表人对外以法人名义进行民事活动时,其与法人之间并非代理关系,而是代表关系,且其代表职权来自法律的明确授权,故不需要有法人的授权委托书......"}
```

## RAG

### 环境配置

- 安装依赖

```bash
python -m pip install --upgrade pip

pip install modelscope==1.9.5
pip install transformers==4.35.2
pip install streamlit==1.24.0
pip install sentencepiece==0.1.99
pip install accelerate==0.24.1

pip install langchain==0.0.292
pip install gradio==4.4.0
pip install chromadb==0.4.15
pip install sentence-transformers==2.2.2
pip install unstructured==0.10.30
pip install markdown==3.3.7
```

- 下载 [Sentence Transformer](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)

```bash
pip install -U huggingface_hub
```

```python
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
os.system('huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir /root/data/model/sentence-transformer')
```

### 知识库搭建

由于源码中不支持使用pdf文件构建数据库，因此需要做一些修改，添加对pdf文件的支持。

- 安装相关的库

```bash
pip install "unstructured[pdf]"
```

- 数据收集 & 数据加载 & 构建向量数据库

  整合了数据收集 & 数据加载 & 构建向量数据库过程，详见脚本`/root/data/create_db.py`

```bash
python /root/data/create_db.py
```

### InternLM 接入 LangChain

- 从 LangChain.llms.base.LLM 类继承一个子类，并重写构造函数与 `_call` 函数，详见`/root/data/LLM.py`

```bash
python /root/data/LLM.py
```

- demo效果

  基于 Gradio 框架部署到 Web 网页，详见`/root/data/web_demo.py`

![image-20240203154129564](assets/image-20240203154129564.png)

## 微调

使用[**XTuner**](https://github.com/InternLM/xtuner)进行微调，对 InternLM2 的支持度最高

- 安装XTuner

```bash
git clone -b v0.1.9 https://gitee.com/Internlm/xtuner
cd xtuner
pip install -e '.[all]'
```

- 训练

  使用deepspeed加速，具体配置详见 `internlm2_chat_7b_qlora_law_e3_copy.py`

```bash
xtuner train ./internlm2_chat_7b_qlora_law_e3_copy.py --deepspeed deepspeed_zero2
```

- LoRA转换为HaggingFace格式

```bash
xtuner convert pth_to_hf ./internlm2_chat_7b_qlora_law_e3.py ./work_dirs/internlm_chat_7b_qlora_law_e3_copy/epoch_3.pth ./hf
```

- 合并基座模型和LoRA

```bash
xtuner convert merge ./internlm2-chat-7b-sft ./hf ./merged --max-shard-size 2GB
```

- chat

```bash
xtuner chat ./merged --prompt-template internlm_chat
```



## 量化

- 安装LMDeploy

```bash
pip install -U lmdeploy
```

- 模型转换，离线转换为TurboMind格式

```bash
lmdeploy convert internlm-chat-7b  /root/share/temp/model_repos/internlm2-chat-7b/
```

- kv量化

```bash
lmdeploy lite calibrate /root/hf4_merge/ --calib-dataset 'ptb' --calib-samples 128 --calib-seqlen 2048 --work-dir ./quant_output_kv
lmdeploy lite kv_qparams ./quant_output_kv /root/workspace/triton_models/weights/ --num-tp 1
```

- 4 bit 量化

```bash
lmdeploy lite auto_awq /root/hf4_merge/ --w-bits 4 --w-group-size 128 --work-dir ./quant_output_w4
```

- 转成TurboMind格式

```bash
lmdeploy convert internlm2-chat-7b ./quant_output_w4 --model-format awq --group-size 128 --dst-path ./workspace_w4quant
```

- chat

```bash
lmdeploy chat turbomind ./workspace_w4quant
```

如果量化显存效果不好，请减小`triton_models/config`文件中的`cache_max_entry_count`值

## 部署



## 评测

- #### 环境包与数据集准备

  克隆opencompass仓库安装依赖

  ​	

  ```
  git clone https://github.com/open-compass/opencompass
  cd opencompass
  pip install -e .
  ```

  准备数据 并解压

  ```
  cp /share/temp/datasets/OpenCompassData-core-20231110.zip /root/opencompass/
  unzip OpenCompassData-core-20231110.zip
  ```

  后面评测的时候发现lawbench的数据包并没有整合在其中，所以这里单独从lawbench项目库中将数据包复制过来

  ```
  git clone https://gitee.com/ljn20001229/LawBench.git
  cp -r /root/personal_assistant/LawBench/data/one_shot /root/personal_assistant/opencompass/data/lawbench
  cp -r /root/personal_assistant/LawBench/data/zero_shot /root/personal_assistant/opencompass/data/lawbench
  ```

- #### 评测运行 

​	opencompass评测可以使用一些写好的config配置文件做评测，也可以直接在命令行写指令 

```
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

​	想要换不同的模型和数据集可以直接在参数后更改配置文件和模型地址，非常方便。

这里直接在命令行写指令进行评测 

`/root/personal_assistant/config/a/work_dirs/hf_merge`是模型路径，这里必须得是完整的（个人操作需要对照自己模型所在位置）。

```
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

- #### 评测结果

在ceval数据上的评测结果

对比对象主要是微调后的模型，原基准模型，与量化模型在ceval中eval-law数据上的对比

​	基础模型得分

![11](assets/11.png)

​	微调后模型得分

![12](assets/12.png)

​	微调模型量化后得分

![13](assets/13.png)

对比来看，模型训练之后对eval-law得分明显提高，但是量化评分不理想。

可能原因：评测具有随机性，一次评测的结果也不能代表模型的整体性能。 

## 声明⚠

感谢您选择使用InternLM4Law。请明确几个关键点，以确保您理解使用本模型的潜在限制和风险。

1. **准确性和可靠性**：虽然我们已经尽最大努力确保模型的准确性和可靠性，但由于法律领域的复杂性和不断变化的法律环境，我们不能保证模型提供的所有回答都是完全准确和最新的。模型的回答可能会因解释、上下文或数据的不足而有所不同。

2. **非专业法律建议**：请注意，本模型提供的回答仅供参考，并不能替代专业法律咨询。在做出任何重要法律决定之前，我们强烈建议您咨询合格的法律专业人士。

3. **使用责任**：使用本模型的任何个人或组织应自行承担使用模型结果的所有风险。模型开发者或维护者不对因使用或依赖模型提供的信息而产生的任何直接或间接损失承担责任。

   

## 致谢

感谢上海人工智能实验室推出的 **[书生·浦语大模型实战营]([InternLM/tutorial (github.com)](https://github.com/InternLM/tutorial))** 学习活动！

感谢上海人工智能实验室对本项目的技术指导和算力支持！



