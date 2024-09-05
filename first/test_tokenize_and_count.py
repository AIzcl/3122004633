import unittest
import jieba


def tokenize_and_count(content):
    """
    对文本进行分词，并统计每个词的出现次数。
    """
    words = list(jieba.cut(content))  # 使用jieba对文本进行分词
    word_count = {}  # 初始化一个空字典用于存储词频
    for word in words:  # 遍历分词后的每个词
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


class TestTokenizeAndCount(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(tokenize_and_count(""), {})

    def test_single_word(self):
        self.assertEqual(tokenize_and_count("hello"), {"hello": 1})

    def test_multiple_words(self):
        self.assertEqual(tokenize_and_count("hello world"), {"hello": 1, " ": 1, "world": 1})

    def test_repeated_words(self):
        self.assertEqual(tokenize_and_count("hello hello"), {"hello": 2, " ": 1})

    def test_mixed_characters(self):
        self.assertEqual(tokenize_and_count("hello 你好"), {"hello": 1, " ": 1, "你好": 1})

    def test_punctuation(self):
        self.assertEqual(tokenize_and_count("hello, world!"), {"hello": 1, ",": 1, " ": 1, "world": 1, "!": 1})

    def test_multiple_punctuations(self):
        self.assertEqual(tokenize_and_count("hello!! world??"), {"hello": 1, "!": 2, " ": 1, "world": 1, "?": 2})

    def test_special_characters(self):
        # 注意：jieba可能不会将@和#与单词合并，除非在自定义词典中定义
        self.assertEqual(tokenize_and_count("@hello #world"), {"@": 1, "hello": 1, " ": 1, "#": 1, "world": 1})

    def test_mixed_content(self):
        self.assertEqual(tokenize_and_count("hello 你好, 世界！"),
                         {"hello": 1, " ": 2, "你好": 1, ",": 1, "世界": 1, "！": 1})

    def test_long_text(self):
        long_text = "hello world this is a test of the tokenize and " \
                    "count function with long text to ensure it works correctly"
        word_count = tokenize_and_count(long_text)
        # 只检查部分词汇以简化测试
        self.assertEqual(word_count["hello"], 1)
        self.assertEqual(word_count["world"], 1)
        self.assertEqual(word_count["this"], 1)
        self.assertEqual(word_count["is"], 1)
        self.assertEqual(word_count["a"], 1)
        self.assertEqual(word_count["test"], 1)
        self.assertEqual(word_count["of"], 1)
        self.assertEqual(word_count["the"], 1)
        self.assertEqual(word_count["tokenize"], 1)
        self.assertEqual(word_count["and"], 1)
        self.assertEqual(word_count["count"], 1)
        self.assertEqual(word_count["function"], 1)
        self.assertEqual(word_count["with"], 1)
        self.assertEqual(word_count["long"], 1)
        self.assertEqual(word_count["text"], 1)
        self.assertEqual(word_count["to"], 1)
        self.assertEqual(word_count["ensure"], 1)
        self.assertEqual(word_count["it"], 1)
        self.assertEqual(word_count["works"], 1)
        self.assertEqual(word_count["correctly"], 1)


if __name__ == '__main__':
    unittest.main()
