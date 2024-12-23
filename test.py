import os
import unittest
import shutil
import shell_emulator


class TestHomeShell(unittest.TestCase):
    def setUp(self):
        self.tar_file = 'D:/wtf_is_this/shell_emulator2/system.tar'
        self.shell = shell_emulator.Home(self.tar_file)

    def test_ls(self):
        output = self.get_output(self.shell.ls)
        expected_output = [
            "system",
            "system/dir1",
            "system/games",
            "system/games/MasterDungeons.txt",
            "system/games/Spore 2 выйдет в 2025 году, отвечаю.txt",
            "system/games/The New GTA7 presentation!!!.pptx",
            "system/выга.txt"
        ]
        self.assertTrue(all(file in output for file in expected_output))

    def test_pwd(self):
        output = self.get_output(self.shell.pwd)
        self.assertEqual(output, ["/"])

    def test_cd(self):
        self.shell.cd("dir1")
        self.assertEqual(self.shell.cwd, "/dir1")
        self.shell.cd("..")
        self.assertEqual(self.shell.cwd, "/dir1\\..")

    def test_find(self):
        output = self.get_output(lambda: self.shell.find("MasterDungeons.txt"))
        self.assertIn("system/games/MasterDungeons.txt", output)

    def test_uniq(self):
        output = self.get_output(self.shell.uniq)
        self.assertIn("system/games/MasterDungeons.txt", output)
        self.assertIn("system/dir1", output)
        self.assertIn("system/games/The New GTA7 presentation!!!.pptx", output)

    def get_output(self, func):
        from io import StringIO
        import sys
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        func()
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        return output.strip().splitlines()


if __name__ == '__main__':
    unittest.main()
