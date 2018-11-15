import unittest
from tempfile import mkdtemp
from os import mkdir, path
from src.util.folders import WorkingDirectory, TempHandler, make_folder


class TestWorkingDir(unittest.TestCase):
    def setUp(self):
        self.temp_dir = mkdtemp()
        self.working_dirs = [WorkingDirectory(),
                             WorkingDirectory(self.temp_dir),
                             WorkingDirectory('some/random/path')]
        self.futures = ['a', 'b', 'c', 'd', 'e', 'f']

    def test_immutable_properties(self):
        for working_dir in self.working_dirs:
            with self.subTest():
                with self.assertRaises(AttributeError):
                    working_dir.root = 'x'
                    working_dir.relative_dir = 'x'
                    working_dir.absolute_dir = 'x'

    def test_properties(self):
        test = WorkingDirectory()
        self.assertEqual(test.root, '.')
        self.assertEqual(test.relative_dir, '')
        self.assertEqual(test.absolute_dir, '.')

        dir_str = 'some/path'
        test = WorkingDirectory(dir_str)
        self.assertEqual(test.root, dir_str)
        self.assertEqual(test.relative_dir, '')
        self.assertEqual(test.absolute_dir, dir_str)

    def test_push(self):
        for working_dir in self.working_dirs:
            with self.subTest():
                for dir_ in self.futures:
                    working_dir.push(dir_)
                self.assertEqual(self.futures, working_dir.directories)
                self.assertEqual('a/b/c/d/e/f', working_dir.relative_dir)

    def test_pop(self):
        for working_dir in self.working_dirs:
            with self.subTest():
                for dir_ in self.futures:
                    working_dir.push(dir_)
                self.assertEqual(self.futures, working_dir.directories)
                popped = working_dir.pop()
                self.assertEqual(self.futures[-1], popped)
                self.assertEqual('a/b/c/d/e', working_dir.relative_dir)

    def test_empty_pop(self):
        for working_dir in self.working_dirs:
            with self.subTest():
                popped = working_dir.pop()
                self.assertEqual(working_dir.root, popped)

    def test_push_and_pop(self):
        for working_dir in self.working_dirs:
            with self.subTest():
                for dir_ in self.futures:
                    working_dir.push(dir_)
                self.assertEqual(self.futures, working_dir.directories)
                len_ = len(self.futures)
                for i in range(len_):
                    popped = working_dir.pop()
                    self.assertEqual(popped, self.futures[len_ - 1 - i])

        for working_dir in self.working_dirs:
            with self.subTest():
                for dir_ in self.futures:
                    working_dir.push(dir_)
                self.assertEqual(self.futures, working_dir.directories)
                working_dir.pop()
                working_dir.push('g')
                self.assertEqual(['a', 'b', 'c', 'd', 'e', 'g'],
                                 working_dir.directories)
                self.assertEqual('a/b/c/d/e/g', working_dir.relative_dir)

    def test_size(self):
        for working_dir in self.working_dirs:
            with self.subTest():
                for dir_ in self.futures:
                    working_dir.push(dir_)
                self.assertEqual(self.futures, working_dir.directories)
                self.assertEqual(len(self.futures), working_dir.size)
                working_dir.pop()
                self.assertEqual(len(self.futures) - 1, working_dir.size)

    def test_absolute_dir(self):
        for working_dir in self.working_dirs:
            for dir_ in self.futures:
                working_dir.push(dir_)

        self.assertEqual('./a/b/c/d/e/f', self.working_dirs[0].absolute_dir)
        self.assertEqual(self.temp_dir + '/a/b/c/d/e/f',
                         self.working_dirs[1].absolute_dir)
        self.assertEqual('some/random/path/a/b/c/d/e/f',
                         self.working_dirs[2].absolute_dir)


class TestTempHandler(unittest.TestCase):
    def setUp(self):
        self.destinations = ['home', 'home/prog']
        self.handlers = []
        for dir_ in self.destinations:
            self.handlers.append(TempHandler(dir_))

    def test_destination(self):
        for i, handler in enumerate(self.handlers):
            self.assertEqual(self.destinations[i],
                             handler.destination_dir)


class TestFolderCreation(unittest.TestCase):
    def setUp(self):
        root = mkdtemp()
        self.folders = ['src', 'test']
        self.current_folders = ['design', 'agile']

    def _helper(self, array):
        root = mkdtemp()
        to_return = []
        for folder in array:
            to_return.append(path.join(root, folder))
        return to_return

    def test_new_folder(self):
        for folder in self._helper(self.folders):
            with self.subTest():
                path_ = make_folder(folder)
                self.assertTrue(path.exists(path_))
                self.assertTrue(path.isdir(path_))

    def test_old_folder(self):
        folders = self._helper(self.current_folders)
        for folder in folders:
            with self.subTest():
                mkdir(folder)
                self.assertTrue(path.exists(folder))

        for folder in folders:
            with self.subTest():
                path_ = make_folder(folder)
                self.assertTrue(path.exists(path_))
                self.assertTrue(path.isdir(path_))

    def test_file_conflict(self):
        folders = self._helper(self.folders)
        for folder in folders:
            with self.subTest():
                name = folder + '.rst'
                with open(name, 'w+') as f:
                    f.write('TEST')
                    f.close()
                self.assertTrue(path.isfile(name))

                with self.assertRaises(Exception):
                    make_folder(name)




if __name__ == '__main__':
    unittest.main()
