import math
import unittest


def cosine_similarity(vec1, vec2):
    """
    计算两个向量（词频字典）之间的余弦相似度。
    """
    inner_product = sum(vec1[key] * vec2.get(key, 0) for key in vec1)  # 计算两个向量的内积
    square_length_vec1 = sum(val ** 2 for val in vec1.values())  # 计算第一个向量的模的平方
    square_length_vec2 = sum(val ** 2 for val in vec2.values())  # 计算第二个向量的模的平方
    if square_length_vec1 == 0 or square_length_vec2 == 0:  # 如果任一向量的模为0
        return 0  # 则余弦相似度为0
    return inner_product / (math.sqrt(square_length_vec1) * math.sqrt(square_length_vec2))  # 计算并返回余弦相似度


class TestCosineSimilarity(unittest.TestCase):
    def test_case_1(self):
        vec1 = {'a': 1, 'b': 2, 'c': 3}
        vec2 = {'a': 1, 'b': 2, 'c': 3}
        self.assertAlmostEqual(cosine_similarity(vec1, vec2), 1.0, places=5)

    def test_case_2(self):
        vec1 = {'a': 1, 'b': 2, 'c': 3}
        vec2 = {'a': 2, 'b': 4, 'c': 6}
        self.assertAlmostEqual(cosine_similarity(vec1, vec2), 1.0, places=5)

    def test_case_3(self):
        vec1 = {'a': 1, 'b': 0, 'c': 0}
        vec2 = {'a': 0, 'b': 1, 'c': 0}
        self.assertAlmostEqual(cosine_similarity(vec1, vec2), 0.0, places=5)

    def test_case_4(self):
        vec1 = {'a': 1, 'b': 1, 'c': 1}
        vec2 = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
        self.assertAlmostEqual(cosine_similarity(vec1, vec2), 0.8660254037844386, places=5)

    def test_case_5(self):
        vec1 = {'a': 0, 'b': 0, 'c': 0}
        vec2 = {'a': 1, 'b': 2, 'c': 3}
        self.assertAlmostEqual(cosine_similarity(vec1, vec2), 0.0, places=5)

    def test_case_6(self):
        vec1 = {'a': 1, 'b': 2, 'c': 3}
        vec2 = {'x': 1, 'y': 2, 'z': 3}
        self.assertAlmostEqual(cosine_similarity(vec1, vec2), 0.0, places=5)

    def test_case_7(self):
        vec1 = {'a': 1, 'b': 2, 'c': 3}
        vec2 = {'a': 1, 'b': 2, 'c': 2}
        # 检查是否在预期的大致范围内
        self.assertGreaterEqual(cosine_similarity(vec1, vec2), 0.979)
        self.assertLessEqual(cosine_similarity(vec1, vec2), 0.980)

    def test_case_8(self):
        vec1 = {'a': 1}
        vec2 = {'a': -1}
        self.assertAlmostEqual(cosine_similarity(vec1, vec2), -1.0, places=5)

    def test_case_9(self):
        vec1 = {'a': 1, 'b': 2}
        vec2 = {'a': 2, 'b': 4}
        self.assertAlmostEqual(cosine_similarity(vec1, vec2), 1.0, places=5)

    def test_case_10(self):
        vec1 = {'a': 1}
        vec2 = {'a': 0}
        self.assertAlmostEqual(cosine_similarity(vec1, vec2), 0.0, places=5)


if __name__ == '__main__':
    unittest.main()
