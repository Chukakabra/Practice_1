import os
import sys
import tarfile


class Home:
    def __init__(self, tar_file):
        self.tar_file = tar_file
        self.cwd = "/"
        self.fs = {}
        self.mount()

    def mount(self):
        try:
            with tarfile.open(self.tar_file, 'r') as f:
                for file in f.getnames():
                    self.fs[file] = None
        except FileNotFoundError:
            print(f"File {self.tar_file} not found.")
            sys.exit(1)

    def ls(self):
        current_path = self.cwd.strip("/")
        for file in self.fs:
            if file.startswith(current_path) and (file[len(current_path):].count('/') == 1 or current_path == ""):
                print(file)

    def cd(self, args):
        if not args:
            self.cwd = "/"
            return
        self.cwd = os.path.join(self.cwd, args)

    def exit(self):
        sys.exit(0)

    def pwd(self):
        print(self.cwd)

    def find(self, filename):
        found = [file for file in self.fs if filename in file]
        if found:
            print("\n".join(found))
        else:
            print(f"File '{filename}' not found.")

    def uniq(self):
        unique_files = set(self.fs.keys())
        for file in unique_files:
            print(file)

    def parse_command(self, command):
        cmd, *args = command.split()
        if hasattr(self, cmd):
            getattr(self, cmd)(*args)

    def run(self):
        while True:
            try:
                command = input(f"{self.cwd}% ").strip()
                if not command:
                    continue
                self.parse_command(command)
            except KeyboardInterrupt:
                print()
                continue

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python home.py <tar_file>")
        sys.exit(1)
    tar_file = sys.argv[1]
    shell = Home(tar_file)
    shell.run()