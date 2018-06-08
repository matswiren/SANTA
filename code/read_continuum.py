from collections import namedtuple
from operator import attrgetter
from scipy.stats.stats import pearsonr, spearmanr 

sections = ['NARRATOR', 'CHARACTERS', 'AUTHOR', 'PLOT_ELEMENT']
curr_tags = {'NARRATOR':0, 
             'CHARACTERS':0, 
             'AUTHOR':0, 
             'PLOT_ELEMENT':0}

Tag = namedtuple('Tag', 'type start end')

def main(annotator_1, annotator_2):
    a1_units = read_units(read_file(annotator_1))
    a2_units = read_units(read_file(annotator_2))

    a1, a2 = [], []
    for i, u in enumerate(sorted(filter(lambda x: x.type == 'PLOT_ELEMENT', a1_units), 
                        key=attrgetter('start'))):
        a1.append(u.end-u.start)
        print(f'u{i},Adam,{u.type},,{u.start/10},{u.end/10}')
    
    print()
    for j, u in enumerate(sorted(filter(lambda x: x.type == 'PLOT_ELEMENT', a2_units), 
                        key=attrgetter('start'))):
        a2.append(u.end-u.start)
        print(f'u{i+j+1},Anna,{u.type},,{u.start/10},{u.end/10}')

def read_file(filepath):
    with open(filepath) as f:
        return f.read().split('\n')

def read_units(a_file):
    continuum = []
    tags = []
    start_recording = False
    for line in a_file:
        # end of tag
        if line.startswith('</'):
            if line[2:-1].islower():
                line[2:-1].upper()
            tags.append(Tag(line[2:-1], curr_tags[line[2:-1]], len(continuum)))
            curr_tags[line[2:-1]] = 0
        # start of tag
        elif line.startswith('<'):
            if line[1:-1].islower():
                line[1:-1].upper()
            start_recording = True
            curr_tags[line[1:-1]] = len(continuum)
        # normal text
        else:
            if not start_recording:
                continue
            continuum += [ x for x in line.split() if '<' not in x ]

    return tags

def visualize_tags(annotations):
    representation = []
    for u in sorted(annotations, key=attrgetter('start')):
        if u.type[0] == 'P':
            continue
        for i in range(u.end-u.start):
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
    annotator_1 = '/home/adam/data/gamma_iaa_testdata/03_adam.txt'
    annotator_2 = '/home/adam/data/gamma_iaa_testdata/03_anna.txt'
    main(annotator_1, annotator_2)