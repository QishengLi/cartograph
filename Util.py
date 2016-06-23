import codecs
import Constants
import numpy as np


def read_tsv(filename):
    with codecs.open(filename, "r", encoding="utf-8") as f:
        headers = f.readline().rstrip("\n").split("\t")
        data = {header: [] for header in headers}
        for line in f:
            row = line.rstrip("\n").split("\t")
            for i, string in enumerate(row):
                data[headers[i]].append(string)
    return data


def read_wikibrain_vecs():
    """We need this function since the file is organized by rows, not columns"""
    matrix = []
    with open(Constants.FILE_NAME_WIKIBRAIN_VECS, "r") as vecs:
        vecs.readline()
        for line in vecs:
            matrix.append(map(float, line.rstrip("\n").split("\t")))
    return matrix


def write_tsv(filename, headers, data):
    with open(filename, "w") as f:
        s = ("\t".join(headers) + "\n").encode("utf-8")
        f.write(s)
        for row_num in range(len(data[0])):
            row = [col[row_num] for col in data]
            s = ("\t".join(map(unicode, row)) + "\n").encode("utf-8")
            print s
            f.write(s)


def calc_area(points):
    unzipped = zip(*points)
    x = unzipped[0]
    y = unzipped[1]
    # Shoelace Algorithm (a la Stackoverflow)
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
