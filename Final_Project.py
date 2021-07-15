# import necessary libraries
import nltk
import random


def main():
    # prompt user for two file names
    filename2 = input("Enter the filename to a piece of your writing: ")
    filename1 = input("Enter the filename to an excerpt from your favorite author: ")
    # open both files to read (if file is found)
    try:
        file1 = open(filename1, 'r')
    except IOError:
        print('File not found')
    else:
        try:
            file2 = open(filename2, 'r')
        except IOError:
            print('File not found')
        else:
            # read contents of both files to strings
            excerpt_1 = file1.read()
            excerpt_2 = file2.read()
            # get stats for excerpts (process_excerpt function takes string as input and returns
            # dictionaries containing punctuation and part of speech counts)
            stats1 = process_excerpt(excerpt_1)
            stats2 = process_excerpt(excerpt_2)
            # set variables for dictionaries for punctuation and part of speech counts for both excerpts
            pun_count1 = stats1[1]
            pos_count1 = stats1[0]
            pun_count2 = stats2[1]
            pos_count2 = stats2[0]
            print('\n=====================================================')
            # display stats for both files (display_stats function takes punctuation and part of speech
            # dictionaries and displays comparison table of stats)
            print('***Stats for', filename1, '/', filename2)
            display_stats(pos_count1, pun_count1, pos_count2, pun_count2)
            print("\nNow let's rewrite your piece using your favorite author's vocabulary...")
            print('--------------------------------------------------------------\n')
            # load dictionary containing parts of speech as keys and list of words in category as value
            diction = load_dictionary(excerpt_1)
            # get new string which has all words from one part of speech changed for random word from diction dictionary
            mashup = scrambler(excerpt_2, diction)
            # revise mashup to ensure grammatical correctness
            revised_mashup = grammar_rules(mashup)
            # add newlines to mashup to prepare for export to file
            mash_to_file = add_newlines(revised_mashup)
            # write mash_to_file to file named 'mashup.txt'
            outfile = open('mashup.txt', 'w')
            outfile.write(mash_to_file)
            # close three files
            outfile.close()
            file1.close()
            file2.close()
            print("\n***Your mashup is saved as 'mashup.txt'")


# process_excerpt function takes excerpt as input
def process_excerpt(excerpt):
    # make excerpt lowercase
    excerpt = excerpt.lower()
    # add punctuation / frequency in text to punctuation dictionary
    punctuation = [',', ';', '.', ':', '!', "'", "\"", '-', '(', ')', '?']
    pun_count = dict()
    for ch in punctuation:
        pun_count[ch] = 0
        for character in excerpt:
            if ch == character:
                pun_count[ch] += 1
        # remove punctuation marks
        excerpt = excerpt.replace(ch, ' ')
    # create tags for parts of speech using nltk (returns list of tuples)
    tokens = nltk.word_tokenize(excerpt)
    tag = nltk.pos_tag(tokens)
    # add all nltk abbreviations for parts of speech to pos dictionary
    pos_count = dict()
    word_forms = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'MD', 'NN',
                  'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS',
                  'RP', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT',
                  'WP', 'WP$', 'WRB']
    for each in word_forms:
        pos_count[each] = 0
    # tally up occurances of parts of speech in text, add to pos dictionary
    for item in tag:
        if item[1] in pos_count:
            pos_count[item[1]] += 1
        else:
            print(item)
    # returns part of speech count dictionary and punctuation count dictionary
    return pos_count, pun_count


# display stats function takes punctuation and part of speech count dictionaries for both files as input
def display_stats(pos_count1, pun_count1, pos_count2, pun_count2):
    # define constant PER (will average frequency per PER words)
    PER = 1000
    # tally up total words for both files
    words1 = 0
    words2 = 0
    for each in pos_count1:
        words1 += pos_count1[each]
    for each in pos_count2:
        words2 += pos_count2[each]
    # calculate average sentence length
    avg_sent_len1 = words1 / (pun_count1['.'] + pun_count1['?'] + pun_count1['!'])
    avg_sent_len2 = words2 / (pun_count2['.'] + pun_count2['?'] + pun_count2['!'])
    # adjust values stored in punctuation and pos dictionaries for both files
    # to account for variation in length (average per PER words)
    for each in pun_count1:
        pun_count1[each] = format((pun_count1[each] * PER) / words1, '.0f')
    for each in pos_count1:
        pos_count1[each] = format((pos_count1[each] * PER) / words1, '.0f')
    for each in pun_count2:
        pun_count2[each] = format((pun_count2[each] * PER) / words2, '.0f')
    for each in pos_count2:
        pos_count2[each] = format((pos_count2[each] * PER) / words2, '.0f')
    # display stats for both files side by side
    print('\nTotal Words:', words1, '/', words2)
    print('Average Words Per Sentence:', format(avg_sent_len1, '.0f'), '/', format(avg_sent_len2, '.0f'), '\n')
    print('Punctuation Frequency (average per 1000 words):')
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
    print('\nParts of Speech Frequency (average per 1000 words):')
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


# load_dictionary function takes an excerpt as input
def load_dictionary(excerpt):
    # make excerpt lower case
    excerpt = excerpt.lower()
    # remove punctuation from excerpt
    punctuation = [',', ';', '.', ':', '!', "'", "\""]
    for ch in punctuation:
        excerpt = excerpt.replace(ch, ' ')
    # tokenize and tag excerpt by part of speech using nltk
    tokens = nltk.word_tokenize(excerpt)
    tag = nltk.pos_tag(tokens)
    # create dictionary and store parts of speech as keys and set
    # of associated words as values (sets eliminate the duplicates)
    diction = dict()
    for item in tag:
        if len(item[0]) > 1:
            if item[1] in diction:
                theset = diction[item[1]]
                theset.add(item[0])
                diction[item[1]] = theset
            else:
                theset = set()
                theset.add(item[0])
                diction[item[1]] = theset
    # make sets into lists
    for each in diction:
        diction[each] = list(diction[each])
    # capitalize proper nouns
    if 'NNP' in diction:
        for each in diction['NNP']:
            each[0] = each[0].upper()
    if 'NNPS' in diction:
        for each in diction['NNPS']:
            each[0] = each[0].upper()
    # returns dictionary of parts of speech and words falling in that category
    return diction


# scrambler takes an excerpt and diction dictionary as input
def scrambler(string, diction):
    # prompt user to choose to replace nouns or verbs
    choice = input("What part of speech would you like to scramble? Type 'N' for noun or 'V' for verb: ")
    # tokenize and tag parts of speech of excerpt using nltk
    tokens = nltk.word_tokenize(string)
    tags = nltk.pos_tag(tokens)
    # write words in excerpt to list, replacing those falling in chosen part of speech with
    # random word in same part of speech from diction dictionary
    punctuation = [',', ';', '.', ':', '!', "'", "\"", '-', '(', ')', '?']
    mashup_list = []
    for item in tags:
        pos = item[1]
        if choice == 'N' or choice == 'n':
            if pos in diction and pos not in punctuation and pos[0] == 'N':
                mashup_list.append('['+diction[pos][random.randint(0, len(diction[pos]) - 1)]+']')
            else:
                mashup_list.append(item[0])
        elif choice == 'V' or choice == 'v':
            if pos in diction and pos not in punctuation and pos[0] == 'V':
                mashup_list.append('['+diction[pos][random.randint(0, len(diction[pos]) - 1)]+']')
            else:
                mashup_list.append(item[0])
    # write list to string
    mashup_string = ''
    for each in mashup_list:
        mashup_string = mashup_string + each + ' '
    # returns string with words in chosen part of speech replaced
    return mashup_string


# grammar_rules takes a string as input
def grammar_rules(libs):
    # ensure all 'a' preceding vowels are changed to 'an'
    vowels = ('a','e','i','o','u')
    libs = libs.replace(' an ', ' a ')
    for vowel in vowels:
        libs = libs.replace('a ['+vowel, 'an ['+vowel)
        libs = libs.replace('a ' + vowel, 'an ' + vowel)

    # ensure all single 'i' words are capitalized to 'I'
    libs = libs.replace('[i]', '[I]')
    # remove spaces before punctuation marks and parentheses
    punctuation = [',', ';', '.', ':', '!', '?', "'", "\""]
    for each in punctuation:
        libs = libs.replace(' ' + each, each)
    libs = libs.replace('( ', '(')
    libs = libs.replace(' )', ')')
    libs = libs.replace(" ' ", '')
    libs = libs.replace("]'", ']')
    # replace 'im' with 'I'm'
    libs = libs.replace('[im]', "[I'm]")
    # ensure first letter of every sentence is capitalized
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
    # return (more) grammatically correct string
    return libs_out


# add_newlines takes string and returns string with newlines every LENGTH characters
def add_newlines(revised_mashup):
    LENGTH = 100
    mash_to_file = ''
    done = False
    while not done:
        line = revised_mashup[:LENGTH]
        revised_mashup = revised_mashup[LENGTH:]
        if len(line) > 0:
            mash_to_file += line + "\n"
        else:
            done = True
    return mash_to_file


main()
