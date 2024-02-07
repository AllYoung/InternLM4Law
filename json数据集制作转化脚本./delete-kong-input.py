#这个脚本可以去除json文件里面input文本为空的所有conversion
import json

def process_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = [json.loads(line) for line in infile]

    # Filter out entries with empty "input"
    data = [entry for entry in data if all(conv.get("input") for conv in entry.get("conversation", []))]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for entry in data:
            json_line = json.dumps(entry, ensure_ascii=False)
            outfile.write(json_line + '\n')

if __name__ == "__main__":
    input_file = "Law-Data-useful/model/data_json/out.jsonl"
    output_file = "Law-Data-useful/model/data_json/out1.jsonl"

    process_json(input_file, output_file)
