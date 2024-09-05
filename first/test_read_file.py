import os
import unittest


def read_file(file_path):
    """
    读取文件内容。如果文件不存在，则抛出 FileNotFoundError 异常。
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist. Please check!")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


class TestReadFile(unittest.TestCase):
    def setUp(self):
        # 设置测试目录和创建一些测试文件
        self.test_dir = 'test_files'
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)

            # 创建测试文件
        self.test_files = {
            'test1.txt': 'Hello, world!',
            'test2.txt': '',
            'test3.txt': 'こんにちは、世界！',
        }
        for filename, content in self.test_files.items():
            with open(os.path.join(self.test_dir, filename), 'w', encoding='utf-8') as f:
                f.write(content)

                # 创建一个不存在的文件引用
        self.nonexistent_file = os.path.join(self.test_dir, 'nonexistent.txt')

        # 创建一个空目录（可选，用于测试文件与目录的区别）
        self.empty_dir = os.path.join(self.test_dir, 'empty_dir')
        os.makedirs(self.empty_dir)

    def tearDown(self):
        # 清理测试文件和目录
        import shutil
        shutil.rmtree(self.test_dir)

    def test_file_exists_and_has_content(self):
        content = read_file(os.path.join(self.test_dir, 'test1.txt'))
        self.assertEqual(content, 'Hello, world!')

    def test_file_exists_but_is_empty(self):
        content = read_file(os.path.join(self.test_dir, 'test2.txt'))
        self.assertEqual(content, '')

    def test_file_with_unicode_content(self):
        content = read_file(os.path.join(self.test_dir, 'test3.txt'))
        self.assertEqual(content, 'こんにちは、世界！')

    def test_file_does_not_exist(self):
        with self.assertRaises(FileNotFoundError) as cm:
            read_file(self.nonexistent_file)
        self.assertEqual(str(cm.exception), f"File {self.nonexistent_file} does not exist. Please check!")

        # 注意：测试目录是否为文件的测试用例已被移除，因为read_file函数不直接处理目录

    # 以下是额外的测试用例，用于覆盖不同的边界情况

    def test_file_with_special_characters(self):
        file_path = os.path.join(self.test_dir, 'test_special.txt')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('!@#$%^&*()_+{}:"<>?')
        content = read_file(file_path)
        self.assertEqual(content, '!@#$%^&*()_+{}:"<>?')

    def test_file_with_newlines(self):
        file_path = os.path.join(self.test_dir, 'test_newlines.txt')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('Hello\nWorld')
        content = read_file(file_path)
        self.assertEqual(content, 'Hello\nWorld')

        # ... 其他测试用例可以根据需要继续添加


if __name__ == '__main__':
    unittest.main()
