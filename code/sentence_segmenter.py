from nltk.tokenize import sent_tokenize
from os import listdir

def read_file(filepath):
    with open(filepath) as f:
        return map(lambda x: sent_tokenize(x), f.read().split('\n'))


def main():
    folder = '/home/adam/git/phase-1-development-corpus/txt/en/'
    for f in sorted(listdir(folder)):
        text = read_file(folder+f)
        with open(f'/home/adam/git/SANTA/data/source/{f}', '+w') as o:
            for parag in text:
                for sentence in parag:
                    o.write(f'{sentence.lstrip()}\n')
                o.write('\n') 
        print(f, 'complete')
    return 1

if __name__ == '__main__':
    r = main()