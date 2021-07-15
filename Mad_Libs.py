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
        stats1 = process_excerpt(file1)
        stats2 = process_excerpt(file2)
        pun_count1 = stats1[1]
        pos_count1 = stats1[0]
        pun_count2 = stats2[1]
        pos_count2 = stats2[0]
        print('Stats for', filename1, '---------')
        display_stats(pos_count1, pun_count1)
        print('Stats for', filename2, '---------')
        display_stats(pos_count2, pun_count2)
        print('/////////////////////////////////////////////////')



def display_stats(pos_count, pun_count):
    PER = 100
    words = 0
    for each in pos_count:
        words += pos_count[each]
    avg_sent_len = words / (pun_count['.'] + pun_count['?'] + pun_count['!'])
    print('\nTotal Words:', words)
    print('Average Sentence Length:', format(avg_sent_len, '.0f'), 'words\n')
    for each in pun_count:
        pun_count[each] = format((pun_count[each] * PER) / words, '.0f')
    for each in pos_count:
        pos_count[each] = format((pos_count[each] * 100) / words, '.0f')

    print('Punctuation Frequency (average per 100 words):')
    print('----------------------------------------------')
    print('Commas:', pun_count[','])
    print('Semicolons:', pun_count[';'])
    print('Periods:', pun_count['.'])
    print('Colons:', pun_count[':'])
    print('Exclamation Points:', pun_count['!'])
    print('Apostrophes:', pun_count["'"])
    print('Quotation Marks:', pun_count['"'])
    print('Dashes:', pun_count['-'])
    print('Question Marks:', pun_count['?'])
    print('Parenthesis (sets):', pun_count[')'])
    print('\nParts of Speech Frequency (average per 100 words):')
    print('----------------------------------------------------')
    print('Coordinating Conjunctions:', pos_count['CC'])
    print('Cardinal Digits:', pos_count['CD'])
    print('Determiners:', pos_count['DT'])
    print('Existentials:', pos_count['EX'])
    print('Foreign Words:', pos_count['FW'])
    print('Prepositions / Subordinating Conjunctions:', pos_count['IN'])
    print('Adjectives:', pos_count['JJ'])
    print('Comparative Adjectives:', pos_count['JJR'])
    print('Superlative Adjectives:', pos_count['JJS'])
    print('Modals:', pos_count['MD'])
    print('Singular Nouns:', pos_count['NN'])
    print('Plural Nouns:', pos_count['NNS'])
    print('Proper Nouns:', pos_count['NNP'])
    print('Plural Proper Nouns:', pos_count['NNPS'])
    print('Predeterminers:', pos_count['PDT'])
    print('Possessives:', pos_count['POS'])
    print('Personal Pronouns:', pos_count['PRP'])
    print('Possessive Pronouns:', pos_count['PRP$'])
    print('Adverbs:', pos_count['RB'])
    print('Comparative Adverbs:', pos_count['RBR'])
    print('Superlative Adverbs:', pos_count['RBS'])
    print('Particles:', pos_count['RP'])
    print('TOs:', pos_count['TO'])
    print('Interjections:', pos_count['UH'])
    print('Verbs:', pos_count['VB'])
    print('Past Tense Verbs:', pos_count['VBD'])
    print('Gerunds:', pos_count['VBG'])
    print('Past Participles:', pos_count['VBN'])
    print('Singular Present Verbs:', pos_count['VBP'])
    print('Third Person Singular Present Verbs:', pos_count['VBZ'])
    print('Determiners:', pos_count['WDT'])
    print('Wh-Pronouns:', pos_count['WP'])
    print('Possessive Wh-Pronouns:', pos_count['WP$'])
    print('Wh-Adverbs:', pos_count['WRB'])
    print('==================================')



def mashup(string, diction):
    tokens = nltk.word_tokenize(string)
    tag = nltk.pos_tag(tokens)
    mashup_list = []
    for item in tag:
        pos = tag[1]
        mashup_list.append(diction[pos][random.randint(0, len(diction[pos]) - 1)])
    return mashup_list


def process_excerpt(file):
    string = file.read()
    string = string.lower()
    punctuation = [',', ';', '.', ':', '!', "'", "\"", '-', '(', ')', '?']
    pun_count = dict()
    for ch in punctuation:
        pun_count[ch] = 0
        for character in string:
            if ch == character:
                pun_count[ch] += 1
        string = string.replace(ch, ' ')

    tokens = nltk.word_tokenize(string)
    tag = nltk.pos_tag(tokens)
    pos_count = dict()
    word_forms = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'MD', 'NN',
                  'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS',
                  'RP', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT',
                  'WP', 'WP$', 'WRB']
    for each in word_forms:
        pos_count[each] = 0
    for item in tag:
        if item[1] in pos_count:
            pos_count[item[1]] += 1
        else:
            print(item)

    return pos_count, pun_count




main()


# TODO: read in excerpt and analyze sentence structure (tally up parts of speech, length, grammar ect.)
# TODO: compare professional writing to your own?
# TODO:then write sentences using said structure and random parts of speech from excerpt REWRITE YOUR PEICE WITH TOLKEIN'S VOCABULARY

