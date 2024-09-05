import re
import unittest


def preprocess_text(content):
    """
    预处理文本，去除标点符号。
    """
    # 更新正则表达式以包括更多的标点符号
    punctuation_pattern = r'[\u3000\u3001\u3002\uff0c\uff0e\uff1a\uff1b\uff1c\uff1d' \
                          r'\uff1e\uff1f\uff01\uff20\u300a\u300b\uff3c\uff3e\u3010\u3011\u3008\u3009\u300c\u300d\u300f' \
                          r'\u3014\u3015\u3016\u3017\uff5b\uff5d\uff5e\u2018\u2019\u201c\u201d\u2022\u2013' \
                          r'\u2014\uff08\uff09\u3012\u3013\u3005\u3030\u303d\u30a0\u30fb\uffe5\uffe3\uffe4￥$.,!?:;"]'
    cleaned_content = re.sub(punctuation_pattern, '', content)
    return cleaned_content


class TestPreprocessText(unittest.TestCase):
    def test_remove_chinese_punctuation(self):
        self.assertEqual(preprocess_text('你好，世界！'), '你好世界')

    def test_remove_mixed_punctuation(self):
        self.assertEqual(preprocess_text('Hello, world! 你好，世界！'), 'Hello world 你好世界')

    def test_no_punctuation(self):
        self.assertEqual(preprocess_text('Hello world'), 'Hello world')

    def test_empty_string(self):
        self.assertEqual(preprocess_text(''), '')

    def test_only_punctuation(self):
        self.assertEqual(preprocess_text('！，。？！？、'), '')

    def test_unicode_spaces(self):
        # 注意：这里的预期结果应该是没有中文全角的空格
        self.assertEqual(preprocess_text('　这是　一个测试。'), '这是一个测试')

    def test_numbers_and_punctuation(self):
        self.assertEqual(preprocess_text('123，456！789'), '123456789')

    def test_quotes(self):
        self.assertEqual(preprocess_text('“这是一个测试”'), '这是一个测试')

    def test_dashes(self):
        self.assertEqual(preprocess_text('这是一个——测试'), '这是一个测试')

    def test_currency_symbols(self):
        # 注意：修改预期结果以匹配去除￥和$后的字符串
        self.assertEqual(preprocess_text('价格：￥1000，美元：$500'), '价格1000美元500')


if __name__ == '__main__':
    unittest.main()
