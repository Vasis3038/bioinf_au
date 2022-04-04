from utils.IOUtils import IOUtils


class TranslTable:

    @staticmethod
    def get_transl_table():
        transl_list = IOUtils().read_file("transl_table.txt").split()
        i = 0
        while i < len(transl_list):
            if transl_list[i] != transl_list[i].upper():
                transl_list.pop(i)
                i -= 1
            i += 1
        transl_table = {}
        for j in range(0, len(transl_list) - 1, 2):
            transl_table[transl_list[j]] = transl_list[j + 1]
        return transl_table
