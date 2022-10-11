import csv
from collections import OrderedDict
def word_freq(file_name):
    words_list = []

    d = OrderedDict()

    with open(file_name,'rt')as f:
        data = csv.reader(f)
        for row in data:
            words_list = row

    for word in words_list:
        if word in d:
            d[word] = d[word] +1
        else:
            d[word] =1

    for key in list(d.keys()):
        print(key,d[key])

if __name__ == '__main__':
    file_name = input('')
    word_freq(file_name)