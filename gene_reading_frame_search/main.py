from utils.IOUtils import IOUtils
from utils.TranslTableUtils import TranslTable

START_CODONS = ["ATG", "GTG", "TGG"]
STOP_CODONS = ["TAG", "TGA", "TAA"]
BASES = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def get_start(sequence, start):
    for i in range(start, len(sequence), 3):
        if sequence[i:i + 3] in START_CODONS:
            return i
    return -1


def get_stop(sequence, start):
    for i in range(start, len(sequence), 3):
        if sequence[i:i + 3] in STOP_CODONS:
            return i + 3
    return -1


def get_orfs(sequence, min_pro_len=0):
    l = len(sequence)
    sequence = sequence.replace("\n", "")
    orfs = []
    start = get_start(sequence, 1)
    stop = get_stop(sequence, start)
    while start != -1 and stop != -1:
        while min_pro_len > stop - start and stop != -1:
            stop = get_stop(sequence, stop + 3)
        if stop == -1:
            return orfs
        orf = sequence[start: stop]
        orfs.append(orf)
        start = get_start(sequence, stop)
        stop = get_stop(sequence, start)
    return orfs


def translation(sequence, transl_table):
    acids = ''
    s = len(sequence)
    i = 0
    for i in range(0, len(sequence), 3):
        acids += transl_table[sequence[i:i + 3]]
    return acids


def reverse_complement(sequence):
    sequence = sequence[::-1]
    complement = ''
    for char in sequence:
        complement += BASES[char]
    return complement


def get_only_base_sequence(row):
    rows = row.split("\n")
    i = 0
    while i < len(rows):
        if len(rows[i]) == 0 or rows[i][0] == '>':
            rows.pop(i)
            i -= 1
        i += 1
    return "".join(rows)


def translate_orfs(orfs, transl_table):
    return [translation(orf, transl_table) for orf in orfs]


if __name__ == '__main__':
    sequence = get_only_base_sequence(IOUtils.read_file("sequence.fa"))
    orfs = get_orfs(sequence, 100)
    acids = translate_orfs(orfs, TranslTable.get_transl_table())
    IOUtils.write_in_file("orfs.fa", "\n\n".join(orfs) + "\n")
    IOUtils.write_in_file("acids_orfs.fa", "\n\n".join(acids) + "\n")
