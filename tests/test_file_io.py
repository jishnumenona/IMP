import unittest
from utilities.file_io import (
    list_directory,
    create_directory,
    delete_directory,
    get_file_path,
    copy_file,
    move_file,
)


class FileIOTest(unittest.TestCase):
    def test_list_directory(self):
        test_dir = "tests/data"
        files = list_directory(test_dir)
        self.assertEqual(len(files), 2)
        self.assertIn("file1.txt", files)

    def test_create_directory(self):
        test_dir = "tests/new_dir"
        create_directory(test_dir)
        self.assertTrue(os.path.exists(test_dir))
        delete_directory(test_dir)

    def test_delete_directory(self):
        test_dir = "tests/temp_dir"
        create_directory(test_dir)
        delete_directory(test_dir)
        self.assertFalse(os.path.exists(test_dir))

    def test_get_file_path(self):
        test_dir = "tests/data"
        filename = "file1.txt"
        file_path = get_file_path(filename, test_dir)
        self.assertEqual(file_path, os.path.join(test_dir, filename))

    def test_copy_file(self):
        src_path = "tests/data/file1.txt"
        dst_path = "tests/data/file1_copy.txt"
        copy_file(src_path, dst_path)
        self.assertTrue(os.path.exists(dst_path))
        os.remove(dst_path)

    def test_move_file(self):
        src_path = "tests/data/file2.txt"
        dst_path = "tests/data/moved_file.txt"
        move_file(src_path, dst_path)
        self.assertFalse(os.path.exists(src_path))
        self.assertTrue(os.path.exists(dst_path))
        os.move(dst_path, src_path)


if __name__ == "__main__":
    unittest.main()
