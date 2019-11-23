import os
import itertools
from gensim.utils import simple_preprocess, tokenize, deaccent

path = "/Users/Olamilekan/Desktop/Machine Learning/OpenSource/yoruba-text/Quran_Mimo/"
yo_path = "/Users/Olamilekan/Desktop/Machine Learning/OpenSource/yoruba-text/Quran_Mimo/yo/"

def get_text(idx, current, lines):
    current_pos = lines.index(current)
    g = [li for li in lines if li[:1].isdigit()]
    next_idx = int(idx) + 1
    k = [lr for lr in g if lr[:1] == str(next_idx)]
    try:
        indx = lines.index(k[0])
        if g[-1] == k[0]:
            out = lines[indx:]
        else:
            out = lines[current_pos:indx]
        return out
    except IndexError:  
        print('Index Error')


def flatten_data(data):
    return [y for x in data for y in x]



for ij in range(1, 100):
    pathed = path + str(ij)
    for i in os.walk(pathed):
        current_chapter = []
        for j in sorted(i[2]):
            if j == ".DS_Store":
                pass
            else:
                current_file = pathed + '/' + j
                with open(current_file, 'r') as r:
                        le = r.readlines()
                        le = [k for k in le if len(k) > 2]
                        shh = '\t'.join([line.strip() for line in le])
                        sh = ["".join(x).replace('.', '').strip() for _, x in itertools.groupby(shh, key=str.isdigit)]
                        sh = [i for i in sh if not i.isdigit()]
                        if len(sh) > 1 and sh[0] != '1':
                            sh = sh[1:]                            
                        sh = [i.replace('\t', ' ') for i in sh]
                        sh = [" ".join(tokenize(i)) for i in sh]
                        current_chapter.append(sh)
                with open(yo_path + f'/{ij}.txt', 'w') as w:
                            d = flatten_data(current_chapter)
                            for item in d:
                                print(item + '\n')
                                w.writelines(item + '\n\n')
