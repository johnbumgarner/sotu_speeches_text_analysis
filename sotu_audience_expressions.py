import pandas as pd

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
        if 'laughter' in line.lower():
            laughter_counter += 1
    return laughter_counter


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
        if 'applause' in line.lower():
            applause_counter += 1
    return applause_counter


def get_sotu_speech(current_speech):
    '''
    This function opens a particular State of the Union Address file,
    and returns it as a file object.

    :param current_speech: the sotu being processed
    :return: file object
    '''
    infile = open(current_speech, 'r', encoding='utf-8')
    return infile

def number_of_laughs(sotu_speeches):
    '''
    This function processes all the sotu speeches, while
    searching for a particular audible expression.

    :param sotu_speeches: a dictionary of sotu speeches filename
    :return: pandas dataframe
    '''
    col_names_laughter = ['president_name', 'speech_year', 'number_of_laughs']
    df_laughter = pd.DataFrame(columns=col_names_laughter)

    number_of_speeches = len(sotu_speeches)
    if number_of_speeches != 0:
        for key, value in sotu_speeches.items():
            number_of_speeches -= 1
            president_name = value[0]
            speech = value[1]

            current_speech = get_sotu_speech(speech)

            laughter = find_audible_expressions(current_speech)

            df1 = {'president_name': president_name, 'speech_year': key, 'number_of_laughs': laughter}
            df_laughter = df_laughter.append(df1, ignore_index=True)

    return df_laughter


def number_of_claps(sotu_speeches):
    '''
    This function processes all the sotu speeches, while
    searching for a particular ovation expression.

    :param sotu_speeches: a dictionary of sotu speeches filename
    :return: pandas dataframe
    '''
    col_names_applause =  ['president_name', 'speech_year', 'number_of_claps']
    df_applause = pd.DataFrame(columns = col_names_applause)

    number_of_speeches = len(sotu_speeches)
    if number_of_speeches != 0:
        for key, value in sotu_speeches.items():
            number_of_speeches -= 1
            president_name = value[0]
            speech = value[1]

            current_speech = get_sotu_speech(speech)
            applause = find_ovation_expressions(current_speech)

            df1 = {'president_name': president_name, 'speech_year': key, 'number_of_claps': applause}
            df_applause = df_applause.append(df1, ignore_index=True)

    return df_applause

sotu_speeches = {'2019':('Trump','trump_sotu_2019.txt'),
                 '2018':('Trump','trump_sotu_2018.txt'),
                 '2017':('Trump','trump_sotu_2017.txt'),
                 '2016':('Obama', 'obama_sotu_2016.txt'),
                 '2015':('Obama', 'obama_sotu_2015.txt'),
                 '2014':('Obama', 'obama_sotu_2014.txt'),
                 '2013':('Obama', 'obama_sotu_2013.txt'),
                 '2012':('Obama', 'obama_sotu_2012.txt'),
                 '2011':('Obama', 'obama_sotu_2011.txt'),
                 '2010':('Obama', 'obama_sotu_2010.txt')}

presidential_laughs = number_of_laughs(sotu_speeches)
presidential_applause = number_of_claps(sotu_speeches)