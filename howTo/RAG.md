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

![image-20240203145624345](README.assets/image-20240203145624345.png)
