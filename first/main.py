import jieba  # 导入jieba分词库，用于中文文本分词
import os  # 导入os模块，用于处理文件和目录路径
import argparse  # 导入argparse模块，用于解析命令行参数
from math import sqrt  # 从math模块导入sqrt函数，用于计算平方根
from datetime import datetime  # 导入datetime模块，用于获取时间戳
import re       # 导入re模块用于去除标点常见的符号
from line_profiler import LineProfiler
import unittest


def preprocess_text(content):

    """
    预处理文本，去除标点符号。
    """
    # 使用正则表达式去除标点符号
    # 这里定义了一个包含常见中文标点符号的字符集，你可以根据需要扩展或修改它
    punctuation_pattern = r'[\u3000\u3001\u3002\uff0c\uff0e\uff1a\uff1b' \
                          r'\uff1c\uff1d\uff1e\uff1f\uff01\uff20\u300a\u300b' \
                          r'\uff3c\uff3e\u3010\u3011\u3008\u3009\u300c\u300d\u' \
                          r'300f\u3014\u3015\u3016\u3017\uff5b\uff5d' \
                          r'\uff5e\u2018\u2019\u201c\u201d\u2022\u2013\u2014\uff0' \
                          r'8\uff09\u3012\u3013\u3005\u3030\u303d\u30a0\u30fb\uffe5\uffe3\uffe4]'
    # 使用re.sub()函数替换文本中的所有标点符号为空字符
    cleaned_content = re.sub(punctuation_pattern, '', content)
    return cleaned_content


def read_file(file_path):
    """
    读取文件内容。如果文件不存在，则抛出 FileNotFoundError 异常。
    """
    if not os.path.exists(file_path):  # 检查文件是否存在
        raise FileNotFoundError(f"File {file_path} does not exist. Please check!")  # 文件不存在时抛出异常
    with open(file_path, 'r', encoding='utf-8') as file:  # 以只读和utf-8编码打开文件
        return file.read()  # 读取文件内容并返回


def tokenize_and_count(content):
    """
    对文本进行分词，并统计每个词的出现次数。
    """
    words = list(jieba.cut(content))  # 使用jieba对文本进行分词
    word_count = {}  # 初始化一个空字典用于存储词频
    for word in words:  # 遍历分词后的每个词
        if word in word_count:  # 如果该词已在字典中
            word_count[word] += 1  # 则其计数加1
        else:  # 如果该词不在字典中
            word_count[word] = 1  # 则添加到字典中并设置计数为1
    return word_count  # 返回词频字典


def cosine_similarity(vec1, vec2):
    """
    计算两个向量（词频字典）之间的余弦相似度。
    """
    inner_product = sum(vec1[key] * vec2.get(key, 0) for key in vec1)  # 计算两个向量的内积
    square_length_vec1 = sum(val ** 2 for val in vec1.values())  # 计算第一个向量的模的平方
    square_length_vec2 = sum(val ** 2 for val in vec2.values())  # 计算第二个向量的模的平方
    if square_length_vec1 == 0 or square_length_vec2 == 0:  # 如果任一向量的模为0
        return 0  # 则余弦相似度为0
    return inner_product / (sqrt(square_length_vec1) * sqrt(square_length_vec2))  # 计算并返回余弦相似度


def main():
    """
    程序的主入口点。
    """
    parser = argparse.ArgumentParser(
        description='Compute similarity between two files using word frequency.')  # 创建命令行参数解析器
    parser.add_argument('file1', help='path to the first file')  # 添加第一个文件路径的命令行参数
    parser.add_argument('file2', help='path to the second file')  # 添加第二个文件路径的命令行参数
    parser.add_argument('output_file', help='path to the output file for similarity score')  # 添加输出文件路径的命令行参数
    args = parser.parse_args()  # 解析命令行参数

    try:
        content1 = read_file(args.file1)  # 读取第一个文件的内容
        content2 = read_file(args.file2)  # 读取第二个文件的内容
        # 预处理文本，去除标点符号
        content1 = preprocess_text(content1)
        content2 = preprocess_text(content2)
        word_count1 = tokenize_and_count(content1)  # 统计第一个文件的词频
        word_count2 = tokenize_and_count(content2)  # 统计第二个文件的词频
        similarity = cosine_similarity(word_count1, word_count2)  # 计算两个文件的余弦相似度

        # 添加时间戳到输出文件中
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获取当前时间并格式化为字符串
        with open(args.output_file, 'a', encoding='utf-8') as file:  # 以追加模式打开输出文件
            file.write(
                f"Similarity: {similarity:.4f} (Computed on {os.path.basename(args.file1)} "
                f"" f"and {os.path.basename(args.file2)}) at {current_time}\n")  # 写入相似度和时间戳到文件
        print(f"Similarity between the two files: {similarity:.4f}")  # 打印相似度到控制台

    except FileNotFoundError as e:  # 捕获并处理FileNotFoundError异常
        print(e)  # 打印异常信息


# 注意，请在cmd窗口运行代码，按照我的博客所介绍的步骤
if __name__ == "__main__":
    lp = LineProfiler()  # 构造分析对象
    """如果想分析多个函数，可以使用add_function进行添加"""
    lp.add_function(read_file)  # 添加第一个待分析函数
    lp.add_function(preprocess_text)  # 添加第二个待分析函数
    lp.add_function(tokenize_and_count)  # 添加第三个待分析函数
    lp.add_function(cosine_similarity)  # 添加第四个待分析函数
    test_func = lp(main)  # 添加分析主函数，注意这里并不是执行函数，所以传递的是是函数名，没有括号。
    test_func()  # 执行主函数，如果主函数需要参数，则参数在这一步传递，例如test_func(参数1, 参数2...)
    lp.print_stats()  # 打印分析结果
    unittest.main()  # 调用主函数以启动程序
    # main()
