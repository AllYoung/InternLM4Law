import pandas as pd
import json

def csv_to_jsonl(input_file, output_file):
    # 读取 CSV 文件
    df = pd.read_csv(input_file)

    # 初始化输出数据列表
    output_data = []

    # 遍历 DataFrame 的每一行
    for index, row in df.iterrows():
        # 创建对话条目
        conversation = {
            "system": "你是一位专业、经验丰富的民法专家，总是根据输入的问题提供准确、全面和详细的答案。",
            "input": row["0"],  # 替换成实际的输入列名称
            "output": row["1"]  # 替换成实际的输出列名称
        }

        # 将对话条目添加到输出数据列表
        output_data.append({"conversation": [conversation]})

    # 将输出数据写入 JSONL 文件
    with open(output_file, 'w', encoding='utf-8') as jsonl_file:
        for item in output_data:
            json.dump(item, jsonl_file, ensure_ascii=False)
            jsonl_file.write('\n')

# 替换成实际的输入 CSV 文件名和输出 JSONL 文件名
csv_to_jsonl('/root/Law-Data-useful/法律问答.csv', '/root/Law-Data-useful/model/data_json/minfa.jsonl')
