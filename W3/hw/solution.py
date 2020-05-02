class FileReader:

    def __init__(self, path_file="example.txt"):
        self.path_file = path_file

    def read(self):
        try:
            with open(self.path_file) as f:
                content = f.read()
                return content

        except FileNotFoundError:
            return ""
