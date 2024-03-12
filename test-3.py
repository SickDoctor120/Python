import hashlib

file_path = r"d:\Users\******\桌面\adress-test.txt"

def md5_16bit(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()[:7]

def process_line(line):
    groups = [line[i:i+2] for i in range(0, len(line)-1)]
    md5_group = [md5_16bit(group) for group in groups]
    return list(zip(groups, md5_group))  # 返回每个分组的字符和对应的MD5值的元组列表

try:
    seen_results = set()  # 用于存储已经见过的结果
    with open(file_path, 'r', encoding='gbk') as file:
        for line in file:
            line = line.strip()
            results = process_line(line)
            for result in results:
                formatted_result = '#'.join(result)
                if formatted_result not in seen_results:
                    seen_results.add(formatted_result)
                    print(formatted_result)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", str(e))
