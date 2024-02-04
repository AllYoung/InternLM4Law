# Gradio 应用

浦源内容平台应用中心提供通过 Gradio 的SDK快速创建应用的功能，[Gradio (opens new window)](https://gradio.app/)是一个简单直观的交互界面的SDK组件，支持多种输入输出格式。只需要在原有程序中新增几行代码，便可快速构建交互式的机器学习模型，将已有的算法模型以 Web 服务形式呈现给用户。关于 Gradio 的简单入门可查看：https://gradio.app/quickstart/

## 快速构建Gradio应用的步骤

### 步骤1：创建代码仓库

在 GitHub 中创建存放应用代码的仓库，其代码大致目录树如下：

```shell
├─GitHub repo
│  ├─app.py                       # 应用代码相关的文件，包含模型推理，应用的前端配置代码，默认应用的启动脚本为根目录下的app.py文件
│  ├─requirements.txt             # 安装运行所需要的 Python 库依赖（pip 安装）
│  ├─packages.txt                 # 安装运行所需要的 Debian 依赖项（ apt-get 安装）
│  └─... 
copy
```

### 步骤2：编写应用代码

基于 Gradio 组件库编写 app.py 代码，需要注意的事项如下：

1. GitHub 根目录下的 `app.py` 文件会作为应用的启动的脚本，请务必在根目录下创建 `app.py` 的文件，若有自定义启动文件，也可以在创建过程中选择自定义启动文件
2. 应用会强制在 **`7860`** 端口启动，请您不要占用或改写个人 gradio 应用的启动端口
3. 应用平台应用代码默认存储的位置为 **`/home/xlab-app-center`**
4. 若存在不想在代码中直接暴露的变量（API Key等），可直接在您个人创建的应用详情-设置添加环境变量的方式解决，在代码中使用环境变量的方式：

```python
import os
env_value = os.getenv({``env_value``})
copy
```

> 备注：
>
> 1. 设置环境变量的步骤：应用详情-“设置”添加环境变量，关于环境变量详细介绍，详情可参考 [环境变量配置示例](https://openxlab.org.cn/docs/apps/应用设置.html#环境变量配置示例)
> 2. 若需要在app.py中快速导入模型，可前往 模型中心上传模型权重后，通过平台提供的 openxlab python SDK进行调用，详情可参考 [应用如何导入模型中心的模型](https://openxlab.org.cn/docs/apps/应用创建流程.html#应用如何导入模型中心的模型)
> 3. 模型上传的详细步骤可查看 [模型上传详细流程](https://openxlab.org.cn/docs/models/上传模型.html)

### 步骤3：配置应用环境

#### **常规环境安装方式**

配置应用所需的运行环境,如有 Python 依赖项（ pip 安装）可写入requirements.txt中，Debian 依赖项（ apt-get 安装）可写入 packages.txt 中，并存放至代码仓库的根目录下。

requirement.txt示例

```text
numpy                             # 默认（存在不替换，不存在安装最新版）
numpy==1.19.5                     # 指定版本 (最日常的写法)
numpy>=1.19.2                     # 大于某个版本
copy
```

packages.txt示例

```text
tmux                              #默认最常用的写法
tmux=3.3                          #安装指定版本的包
copy
```

应用中心资源容器预置环境如下：

| 硬件资源名称                     | 容器预置环境                                     | 获取方式                                                |
| -------------------------------- | ------------------------------------------------ | ------------------------------------------------------- |
| 2vCPU 8GB RAM                    | python:3.9_torch: 1.13.1_gradio:3.18.0           | 直接获取                                                |
| 4vCPU 16GB RAM                   | python:3.9_torch: 1.13.1_gradio:3.18.0           | [申请获取](https://openxlab.org.cn/apps/apply-hardware) |
| 4vCPU 16GB RAM NVIDIA vGPU 8GB   | python:3.9_cuda:11.7_torch: 1.13.1_gradio:3.18.0 | [申请获取](https://openxlab.org.cn/apps/apply-hardware) |
| 4vCPU 16GB RAM NVIDIA vGPU 16GB  | python:3.9_cuda:11.7_torch: 1.13.1_gradio:3.18.0 | [申请获取](https://openxlab.org.cn/apps/apply-hardware) |
| 12vCPU 48GB RAM NVIDIA A10 24GB  | python:3.9_cuda:11.7_torch: 1.13.1_gradio:3.18.0 | [申请获取](https://openxlab.org.cn/apps/apply-hardware) |
| 12vCPU 48GB RAM NVIDIA A100 40GB | python:3.9_cuda:11.7_torch: 1.13.1_gradio:3.18.0 | [申请获取](https://openxlab.org.cn/apps/apply-hardware) |

#### **其他环境安装方式**

若您需要安装除了python以外的包，如需要通过 mim 安装 mmcv，您可先在 requirement.txt 中填写 mim，然后在 `app.py` 中写入以下代码，即可完成相关包的安装：

```python
import os
os.system("mim install mmcv-full")

```

#### **启动特定的脚本的方式**

若需要启动特定的脚本，您可在`app.py` 代码中通过`import os`的方式进行启动，例如：

```python
import os
os.system("bash webui.sh")
os.system("python -u launch.py")

```

#### 其他 pip 镜像源选择

在应用中心中，默认提供的系统的版本是 Ubuntu 18.04 ，为方便不同的用户进行 `pip` 依赖包的安装，默认提供清华大学镜像源进行安装 `pip` 依赖项，若用户想用其他的镜像源进行安装依赖项，可以在高级配置中，切换需要的镜像源进行安装，平台提供的镜像源如下：

|     镜像源名称     |                       镜像源地址                        |
| :----------------: | :-----------------------------------------------------: |
|    Pypi 官方源     |                https://pypi.org/simple/                 |
| 清华大学源（默认） |        https://pypi.tuna.tsinghua.edu.cn/simple         |
|      阿里云源      |         https://mirrors.aliyun.com/pypi/simple/         |
|      中科大源      |        https://pypi.mirrors.ustc.edu.cn/simple/         |
|   北京理工大学源   |            https://pypi.bjut.edu.cn/simple/             |
|   西北工业大学源   |            https://pypi.nwpu.edu.cn/simple/             |
|       豆瓣源       |             https://pypi.douban.com/simple/             |
|      华为云源      | https://mirrors.huaweicloud.com/repository/pypi/simple/ |
|       网易源       |          https://mirrors.163.com/pypi/simple/           |
|      腾讯云源      |     https://mirrors.cloud.tencent.com/pypi/simple/      |

------

## 构建您的第一个Gradio应用：图像分类器

### 步骤1：创建代码仓库

前往GitHub创建应用所需的代码仓库，传送门：https://github.com/new

备注：创建GitHub仓库记得勾选 `Add a README file`

![img](assets\create_github_repo.7b92053f.png)

### 步骤2：编写应用代码

编写应用代码，本例采用Pytorch构建分类预测函数，创建一个命名为 `app.py` 的文件，代码如下所示：

![img](assets\create_github_repo1.8a5a44c7.png)

构建分类器的 `app.py` 代码如下：

```python
import gradio as gr
import torch
import requests
from torchvision import transforms

torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def predict(inp):
  inp = transforms.ToTensor()(inp).unsqueeze(0)
  with torch.no_grad():
    prediction = torch.nn.functional.softmax(model(inp)[0], dim=0)
    confidences = {labels[i]: float(prediction[i]) for i in range(1000)}    
  return confidences

demo = gr.Interface(fn=predict, 
             inputs=gr.inputs.Image(type="pil"),
             outputs=gr.outputs.Label(num_top_classes=3),
             examples=[["cheetah.jpg"]],
             )
             
demo.launch()
copy
```

**上传示例的图片至github仓库中，并命名为cheetah.jpg**

![img](assets\cheetah.17dc37eb.jpg)

> 备注：若应用所需的模型文件较大，可尝试先将模型存放至模型中心进行托管，再通过平台提供的openxlab的SDK进行使用
>
> 1. 模型上传的详细步骤可查看 [模型上传详细流程](https://openxlab.org.cn/docs/models/上传模型.html)
> 2. 应用中心如何导入模型中心的步骤可查看 [应用如何导入模型中心的模型](https://openxlab.org.cn/docs/apps/应用创建流程.html#应用如何导入模型中心的模型)

### 步骤3：配置应用环境

配置应用运行所需的环境，将python相关的依赖包写入 `requirements.txt` 文档中

![img](assets\create_github_repo2.db2a9ef9.png)

`requirements.txt` 填入的环境如下：

```text
requests
torch
torchvision
copy
```

上传图片后完整仓库图如下：

![img](assets\create_github_repo10.cd94543e.png)

### 步骤4：创建应用仓库

在浦源内容平台中，创建应用仓库，填写应用基础信息，包括应用的名称、应用所属任务类型、标签、关联的模型和关联的论文信息，以及上传合适的应用封面，填写完成后，点击立即创建

创建入口在导航栏的右侧 +创建，如下如所示：

![img](assets\crate_app_step1.00ba92bc.png)

选择Gradio组件，开始创建

![img](assets\create_app_2.c9d69e14.png)

### 步骤5：进行应用配置

填写图像分类器应用的基础信息，包括应用的名称和应用对应的任务类型，还有记得填入存储有图像分类器的GitHub仓库，选择硬件资源后，即可立即创建啦~

![img](assets\create_github_repo4.dda927ce.png)

> 备注：
>
> 1. 若未进行GitHub授权,请先前往授权
> 2. 若您有需要自定义启动的文件,可以通过配置选择启动文件的路径
> 3. 若当前您的资源quota不能满足您的应用需求,也可以填写硬件资源申请表单进行 [申请获取](https://openxlab.org.cn/apps/apply-hardware)
> 4. 若您有不方便在代码中暴露的变量信息,可通过高级配置中的环境变量进行配置

### 步骤6：完成应用构建和启动

查看日志，调试应用代码，若应用代码无问题，运行成功，可体验应用，并将应用进行公开![img](assets\create_github_repo6.c666feb0.png)



![img](assets/create_github_repo6.c666feb0.png)

> 备注：构建应用过程中，您也可以尽量去完善您的应用信息，包括应用封面、中文别称、关联论文和关联模型等信息

构建过程中，可查看应用的构建日志，及时查看应用的构建进度



![img](assets\create_github_repo7.0b562676.png)

### 步骤7：查看应用并公开

应用成功运行后，可以用示例进行测试应用是否能跑通，跑通后可以将应用进行公开，让更多人可以看到您的应用哦~

![img](assets\create_github_repo8.95e2e48d.png)

公开后，可以在应用中心的列表页-全部中找到您构建的应用

![img](assets\create_github_repo9.82bb801d.png)