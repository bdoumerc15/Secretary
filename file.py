import pathlib
import os


class File:

    total_files = 0
    default_path = str(pathlib.Path("c:/users/bdoum/documents"))

    def __init__(self, filename='text.txt', text='', path=default_path):
        self.filename = pathlib.Path(filename)
        self.text = text
        self.path = pathlib.Path(path)
        File.total_files += 1

    def __repr__(self):
        return self.filename

    @property
    def create_directory(self):
        directory = 'File'
        join_path = os.path.join(self.path, directory)
        return os.mkdir(join_path)

    @property
    def absolute_path(self):
        return self.create_directory / str(self.filename)

    @property
    def read_file(self):
        with open(self.path) as file:
            print(file.read())
            print('Archivo leido')

    @property
    def create_file(self):
        with open(self.absolute_path, 'w') as file:
            file.write(self.text)
            print('Archivo escrito correctamente')


file = File()