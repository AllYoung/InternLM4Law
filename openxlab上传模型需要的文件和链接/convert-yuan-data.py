import sys
import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False
file_path = 'xxx.yml'
# 读取YAML文件内容
with open(file_path, 'r') as file:
 data = yaml.load(file)
# 遍历模型列表
for model in data.get('Models', []):
 # 为每个模型添加Weights键值对，确保名称被正确引用
 model['Weights'] = model['Name']

# 将修改后的数据写回文件
with open(file_path, 'w') as file:
 yaml.dump(data, file)

print("Modifications saved to the file.")
#这是一个脚本，帮你把模型文件给遍历一遍，重新填写在所需要的yml文件，但是注意原有的会便利，没有的就不会添加，要注意修改完之后对照一下有没有缺少文件
