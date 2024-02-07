#这个脚本是用来修改json文件里面的system文本的脚本
import json

def process_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = [json.loads(line) for line in infile]

    for entry in data:
        for conv in entry["conversation"]:
            conv["system"] = "你是一位专业、经验丰富的专家，总是根据输入的问题提供准确、全面和详细的答案。"

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for entry in data:
            json_line = json.dumps(entry, ensure_ascii=False)
            outfile.write(json_line + '\n')

if __name__ == "__main__":
    input_file = "Law-Data-useful/model/json/output.jsonl"
    output_file = "Law-Data-useful/model/json/out.jsonl"

    process_jsonl(input_file, output_file)
