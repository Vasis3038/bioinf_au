import os


class IOUtils:
    @staticmethod
    def read_file(file_name):
        cur_path = os.path.dirname(__file__).split("\\")
        cur_path.pop()
        cur_path = str.join("/", cur_path) + '/resources/'
        file = open(cur_path + file_name, 'r')
        content = file.read()
        file.close()
        return content

    @staticmethod
    def write_in_file(file_name, content):
        file = open("resources/" + file_name, 'w')
        file.write(content)
        file.close()
