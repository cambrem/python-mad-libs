import nltk
import random

def main():

    filename1 = 'hobbit.txt'
    filename2 = 'sunalsorises.txt'
    try:
        file1 = open(filename1, 'r')
        file2 = open(filename2, 'r')
    except IOError:
        print('File not found')
    else:
        print("Now let's rewrite your piece using Tolkein's vocabulary!")
        string = file2.read()
        diction = load_dictionary(file1)
        words = scrambler(string, diction)
        mashup = ''
        for each in words:
            mashup = mashup + each + ' '
        revised_mashup = grammar_rules(mashup)
        print(revised_mashup)
        outfile = open('mashup.txt', 'w')
        outfile.write(revised_mashup)



def load_dictionary(file):
    string = file.read()
    string = string.lower()
    punctuation = [',', ';', '.', ':', '!', "'", "\""]
    for ch in punctuation:
        string = string.replace(ch, ' ')

    tokens = nltk.word_tokenize(string)
    tag = nltk.pos_tag(tokens)
    diction = dict()
    for item in tag:
        if item[1] in diction:
            theset = diction[item[1]]
            theset.add(item[0])
            diction[item[1]] = theset

        else:
            theset = set()
            theset.add(item[0])
            diction[item[1]] = theset

    for each in diction:
        diction[each] = list(diction[each])
    return diction


def scrambler(string, diction):
    choice = input("What part of speech would you like to scramble? Type 'N' for noun or 'V' for verb: ")
    tokens = nltk.word_tokenize(string)
    tags = nltk.pos_tag(tokens)
    punctuation = [',', ';', '.', ':', '!', "'", "\"", '-', '(', ')', '?']
    mashup_list = []
    for item in tags:
        pos = item[1]
        if choice == 'N' or choice == 'n':
            if pos in diction and pos not in punctuation and pos[0] == 'N':
                mashup_list.append(diction[pos][random.randint(0, len(diction[pos]) - 1)])
            else:
                mashup_list.append(item[0])
        elif choice == 'V' or choice == 'v':
            if pos in diction and pos not in punctuation and pos[0] == 'V':
                mashup_list.append(diction[pos][random.randint(0, len(diction[pos]) - 1)])
            else:
                mashup_list.append(item[0])
    return mashup_list


def grammar_rules(libs):
    vowels = ('a','e','i','o','u')
    for vowel in vowels:
        libs = libs.replace('a '+vowel, 'an '+vowel)
    libs = libs.replace(' i ',' I ')
    libs = libs.replace(' . ','. ')
    libs = libs.replace(' , ',', ')
    index = 0
    ch_list = []
    for each in libs:
        ch_list.append(each)

    for each in ch_list:
        if each == '.':
            if (index + 2) < len(ch_list):
                ch_list[index + 2] = ch_list[index + 2].upper()
        index += 1
    ch_list[0] = ch_list[0].upper()
    libs_out = ''
    for each in ch_list:
        libs_out += each
    return libs_out


main()