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
        print('Stats for', filename1, 'vs', filename2)
        display_stats(pos_count1, pun_count1, pos_count2, pun_count2)
        print('/////////////////////////////////////////////////')



def display_stats(pos_count1, pun_count1, pos_count2, pun_count2):
    PER = 100
    words1 = 0
    words2 = 0
    for each in pos_count1:
        words1 += pos_count1[each]
    avg_sent_len1 = words1 / (pun_count1['.'] + pun_count1['?'] + pun_count1['!'])
    for each in pun_count1:
        pun_count1[each] = format((pun_count1[each] * PER) / words1, '.0f')
    for each in pos_count1:
        pos_count1[each] = format((pos_count1[each] * 100) / words1, '.0f')

    for each in pos_count2:
        words2 += pos_count2[each]
    avg_sent_len2 = words2 / (pun_count2['.'] + pun_count2['?'] + pun_count2['!'])
    for each in pun_count2:
        pun_count2[each] = format((pun_count2[each] * PER) / words2, '.0f')
    for each in pos_count2:
        pos_count2[each] = format((pos_count2[each] * 100) / words2, '.0f')

    print('\nTotal Words:', words1, '/', words2)
    print('Average Words Per Sentence:', format(avg_sent_len1, '.0f'), '/', format(avg_sent_len2, '.0f'), '\n')



    print('Punctuation Frequency (average per 100 words):')
    print('----------------------------------------------')
    print('Commas:', pun_count1[','], '/', pun_count2[','])
    print('Semicolons:', pun_count1[';'], '/', pun_count2[';'])
    print('Periods:', pun_count1['.'], '/', pun_count2['.'])
    print('Colons:', pun_count1[':'], '/', pun_count2[':'])
    print('Exclamation Points:', pun_count1['!'], '/', pun_count2['!'])
    print('Apostrophes:', pun_count1["'"], '/', pun_count2["'"])
    print('Quotation Marks:', pun_count1['"'], '/', pun_count2['"'])
    print('Dashes:', pun_count1['-'], '/', pun_count2['-'])
    print('Question Marks:', pun_count1['?'], '/', pun_count2['?'])
    print('Parenthesis (sets):', pun_count1[')'], '/', pun_count2[')'])
    print('\nParts of Speech Frequency (average per 100 words):')
    print('----------------------------------------------------')
    print('Coordinating Conjunctions:', pos_count1['CC'], '/', pos_count2['CC'])
    print('Cardinal Digits:', pos_count1['CD'], '/', pos_count2['CD'])
    print('Determiners:', pos_count1['DT'], '/', pos_count2['DT'])
    print('Existentials:', pos_count1['EX'], '/', pos_count2['EX'])
    print('Foreign Words:', pos_count1['FW'], '/', pos_count2['FW'])
    print('Prepositions / Subordinating Conjunctions:', pos_count1['IN'], '/', pos_count2['IN'])
    print('Adjectives:', pos_count1['JJ'], '/', pos_count2['JJ'])
    print('Comparative Adjectives:', pos_count1['JJR'], '/', pos_count2['JJR'])
    print('Superlative Adjectives:', pos_count1['JJS'], '/', pos_count2['JJS'])
    print('Modals:', pos_count1['MD'], '/', pos_count2['MD'])
    print('Singular Nouns:', pos_count1['NN'], '/', pos_count2['NN'])
    print('Plural Nouns:', pos_count1['NNS'], '/', pos_count2['NNS'])
    print('Proper Nouns:', pos_count1['NNP'], '/', pos_count2['NNP'])
    print('Plural Proper Nouns:', pos_count1['NNPS'], '/', pos_count2['NNPS'])
    print('Predeterminers:', pos_count1['PDT'], '/', pos_count2['PDT'])
    print('Possessives:', pos_count1['POS'], '/', pos_count2['POS'])
    print('Personal Pronouns:', pos_count1['PRP'], '/', pos_count2['PRP'])
    print('Possessive Pronouns:', pos_count1['PRP$'], '/', pos_count2['PRP$'])
    print('Adverbs:', pos_count1['RB'], '/', pos_count2['RB'])
    print('Comparative Adverbs:', pos_count1['RBR'], '/', pos_count2['RBR'])
    print('Superlative Adverbs:', pos_count1['RBS'], '/', pos_count2['RBS'])
    print('Particles:', pos_count1['RP'], '/', pos_count2['RP'])
    print('TOs:', pos_count1['TO'], '/', pos_count2['TO'])
    print('Interjections:', pos_count1['UH'], '/', pos_count2['UH'])
    print('Verbs:', pos_count1['VB'], '/', pos_count2['VB'])
    print('Past Tense Verbs:', pos_count1['VBD'], '/', pos_count2['VBD'])
    print('Gerunds:', pos_count1['VBG'], '/', pos_count2['VBG'])
    print('Past Participles:', pos_count1['VBN'], '/', pos_count2['VBN'])
    print('Singular Present Verbs:', pos_count1['VBP'], '/', pos_count2['VBP'])
    print('Third Person Singular Present Verbs:', pos_count1['VBZ'], '/', pos_count2['VBZ'])
    print('Determiners:', pos_count1['WDT'], '/', pos_count2['WDT'])
    print('Wh-Pronouns:', pos_count1['WP'], '/', pos_count2['WP'])
    print('Possessive Wh-Pronouns:', pos_count1['WP$'], '/', pos_count2['WP$'])
    print('Wh-Adverbs:', pos_count1['WRB'], '/', pos_count2['WRB'])
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