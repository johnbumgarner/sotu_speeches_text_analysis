import matplotlib.pyplot as plt
import pandas as pd

def get_sotu_speech(current_speech):
    '''
    This function opens a particular State of the Union Address file,
    and returns it as a file object.

    :param current_speech: the sotu being processed
    :return: file object
    '''
    infile = open(current_speech, 'r', encoding='utf-8')
    return infile

def find_ovation_expressions(input_file):
    '''
    This function looks for the word applause in a particular
    State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of mentions of applause in the speech
    '''
    readlines = input_file.readlines()
    applause_counter = 0
    for line in readlines:
        # speech transcripts contain the word applause to
        # signify audience applause
        if 'applause' in line.lower():
            applause_counter += 1
    return applause_counter

def number_of_claps(sotu_speeches):
    '''
    This function processes all the sotu speeches, while
    searching for a particular ovation expression.

    :param sotu_speeches: a dictionary of sotu speeches filename
    :return: pandas dataframe
    '''
    col_names_applause =  ['president', 'year', 'claps']
    df_applause = pd.DataFrame(columns = col_names_applause)

    number_of_speeches = len(sotu_speeches)
    if number_of_speeches != 0:
        for key, value in sotu_speeches.items():
            number_of_speeches -= 1
            president_name = value[0]
            speech = value[1]

            current_speech = get_sotu_speech(speech)
            applause = find_ovation_expressions(current_speech)

            df1 = {'president': president_name, 'year': key, 'claps': applause}
            df_applause = df_applause.append(df1, ignore_index=True)

    return df_applause

def find_audible_expressions(input_file):
    '''
    This function looks for the word laughter in a particular
    State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of mentions of laughter in the speech
    '''
    readlines = input_file.readlines()
    laughter_counter = 0
    for line in readlines:
        # speech transcripts contain the word laughter to
        # signify audience laughter
        if 'laughter' in line.lower():
            laughter_counter += 1
    return laughter_counter

def number_of_laughs(sotu_speeches):
    '''
    This function processes all the sotu speeches, while
    searching for a particular audible expression.

    :param sotu_speeches: a dictionary of sotu speeches filename
    :return: pandas dataframe
    '''
    col_names_laughter = ['president', 'year', 'laughs']
    df_laughter = pd.DataFrame(columns=col_names_laughter)

    number_of_speeches = len(sotu_speeches)
    if number_of_speeches != 0:
        for key, value in sotu_speeches.items():
            number_of_speeches -= 1
            president_name = value[0]
            speech = value[1]

            current_speech = get_sotu_speech(speech)

            laughter = find_audible_expressions(current_speech)

            df1 = {'president': president_name, 'year': key, 'laughs': laughter}
            df_laughter = df_laughter.append(df1, ignore_index=True)

    return df_laughter

sotu_speeches = {'2019':('Trump','trump_sotu_2019.txt'),
                 '2018':('Trump','trump_sotu_2018.txt'),
                 '2017':('Trump','trump_sotu_2017.txt'),
                 '2016':('Obama', 'obama_sotu_2016.txt'),
                 '2015':('Obama', 'obama_sotu_2015.txt'),
                 '2014':('Obama', 'obama_sotu_2014.txt'),
                 '2013':('Obama', 'obama_sotu_2013.txt'),
                 '2012':('Obama', 'obama_sotu_2012.txt'),
                 '2011':('Obama', 'obama_sotu_2011.txt'),
                 '2010':('Obama', 'obama_sotu_2010.txt'),
                 '2008':('Bush', 'georgewbush_sotu_2008.txt'),
                 '2007':('Bush', 'georgewbush_sotu_2007.txt'),
                 '2006':('Bush', 'georgewbush_sotu_2006.txt'),
                 '2005':('Bush', 'georgewbush_sotu_2005.txt'),
                 '2004':('Bush', 'georgewbush_sotu_2004.txt'),
                 '2003':('Bush', 'georgewbush_sotu_2003.txt'),
                 '2002':('Bush', 'georgewbush_sotu_2002.txt')}


presidential_applause = number_of_claps(sotu_speeches)
presidential_laughs = number_of_laughs(sotu_speeches)

# This code creates a bar chart that shows the number of times that
# the audience clapped during a particular State of the Union Address
presidential_applause.plot(kind='bar', x='year', y='claps', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n audience applause', fontweight='demibold')
plt.ylabel('applause count', fontsize=10, fontweight='demibold')
plt.show()

# # This code creates a bar chart that shows the number of times that
# # the audience laughed during a particular State of the Union Address
presidential_laughs.plot(kind='bar', x='year', y='laughs', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n audience laughter', fontweight='demibold')
plt.ylabel('laughter count', fontsize=10, fontweight='demibold')
plt.show()