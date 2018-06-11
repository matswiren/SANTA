from collections import namedtuple
from operator import attrgetter
from scipy.stats.stats import pearsonr, spearmanr 
from os import listdir

sections = ['NARRATOR', 'CHARACTERS', 'AUTHOR', 'PLOT_ELEMENT']
curr_tags = {'NARRATOR':0, 
             'CHARACTERS':0, 
             'AUTHOR':0, 
             'PLOT_ELEMENT':0}

Tag = namedtuple('Tag', 'type start end')

def main(annotator_1, annotator_2, k):
    a1_units, a1_text = read_units(read_file(annotator_1))
    a2_units, a2_text = read_units(read_file(annotator_2))

    #print(len(a1_text), len(a2_text))
    #for a, b in zip(a1_text, a2_text):
    #    print(a,b)
    #    if ''.join([x for x in a if x.isalpha()]) != ''.join([x for x in b if x.isalpha()]):
    #        return 1

    a1, a2 = [], []
    for i, u in enumerate(sorted(filter(lambda x: x.type != 'PLOT_ELEMENT', a1_units), 
                       key=attrgetter('start'))):
       a1.append(u.end-u.start)
       print(f'u{i+k},Adam,{u.type},,{u.start},{u.end}')
    
    for j, u in enumerate(sorted(filter(lambda x: x.type != 'PLOT_ELEMENT', a2_units), 
                        key=attrgetter('start'))):
        a2.append(u.end-u.start)
        print(f'u{i+j+1+k},Anna,{u.type},,{u.start},{u.end}')
    print()

    return len(a1) + len(a2)

def read_file(filepath):
    with open(filepath) as f:
        return f.read().split('\n')

def read_units(a_file):
    continuum = []
    tags = []
    start_recording = False
    for line in a_file:
        # end of tag
        if line.startswith('</') or line.startswith('<\\'):
            line = line[2:-1]
            if line.islower():
                line = line.upper()
            tags.append(Tag(line, curr_tags[line], len(continuum)))
            curr_tags[line] = 0
        # start of tag
        elif line.startswith('<'):
            line = line[1:-1]
            if line.islower():
                line = line.upper()
            start_recording = True
            curr_tags[line] = len(continuum)
        # normal text
        else:
            if not start_recording:
                continue
            continuum += [ x for x in line.split() if '<' not in x ]

    return tags, continuum

def visualize_tags(annotations):
    representation = []
    for u in sorted(annotations, key=attrgetter('start')):
        if u.type[0] == 'P':
            continue
        for _ in range(u.end-u.start):
            representation.append(sections.index(u.type))
    return representation

def visualize_plot(annotations):
    representation = []
    for i, u in enumerate(annotations):
        if u.type != 'PLOT_ELEMENT':
            continue
        for i in range(u.end-u.start):
            representation.append(i)   
    return representation


if __name__ == '__main__':
    
    
    foldername1 = '/home/adam/git/SANTA/data/adam/'
    foldername2 = '/home/adam/git/SANTA/data/anna/'

    #k = main(foldername1+'02_Andersen_The+Elf+of+the+Rose_C.txt', 
    #         foldername2+'02_Andersen_The+Elf+of+the+Rose_AK_ADDS2', 0)
    
    k, m = 0, 0
    for f1, f2 in zip(sorted(listdir(foldername1)), sorted(listdir(foldername2))):   
        print(f1)
        k += main(foldername1+f1, foldername2+f2, k)
    
