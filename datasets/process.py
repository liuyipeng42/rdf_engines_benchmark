from urllib.parse import unquote

def process_sparql_file(file_path):
    processed_queries = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('Query String:'):
                # 提取编码部分并解码
                encoded_query = line.split('Query String: ')[1]
                decoded_query = unquote(encoded_query)

                # 清理特殊符号和格式
                cleaned_query = decoded_query.replace('+', ' ')  # 将+替换为空格
                cleaned_query = cleaned_query.replace('%0A', '\n')  # 恢复换行符

                processed_queries.append(cleaned_query)

    with open("cleaned_queries.txt", "w") as f:
        for query in processed_queries:
            if "ORDER" not in query and "UNION" not in query and "FILTER" not in query and "DESCRIBE" not in query and "AS" not in query and "CONSTRUCT" not in query:
                f.write(query.replace("\n", " ") + "\n")

def replace_prefix():
    with open("swdf-queries.txt", "w") as fout:
        with open("cleaned_queries.txt", "r") as f:
            for line in f:
                if not line.startswith("PREFIX"):
                    fout.write(line)


# process_sparql_file("swdf-queries.txt")
replace_prefix()
