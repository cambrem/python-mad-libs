def get_noun(words):
    return words['NN'][random.randint(0, len(words['NN']) - 1)]

def get_verb(words):
    return words['VBD'][random.randint(0, len(words['VBD']) - 1)]

def mad_libs(words):
    try:
        return 'In a', get_noun(words), 'in the ground there', get_verb(words), 'a hobbit.'
    except KeyError:
        print('Insufficient Vocabulary')