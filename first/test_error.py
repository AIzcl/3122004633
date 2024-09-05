import unittest
from main import read_file


class TestFileOperations(unittest.TestCase):

    def test_read_file_nonexistent(self):
        """
        测试当文件不存在时，read_file函数是否抛出FileNotFoundError。
        """
        nonexistent_file = 'nonexistent_file.txt'
        with self.assertRaises(FileNotFoundError) as context:
            read_file(nonexistent_file)
        self.assertTrue('File {} does not exist'.format(nonexistent_file) in str(context.exception))


if __name__ == '__main__':
    unittest.main()
