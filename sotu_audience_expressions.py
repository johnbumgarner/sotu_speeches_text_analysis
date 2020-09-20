#!/usr/local/bin/python3

##################################################################################
# “AS-IS” Clause
#
# Except as represented in this agreement, all work produced by Developer is
# provided ​“AS IS”. Other than as provided in this agreement, Developer makes no
# other warranties, express or implied, and hereby disclaims all implied warranties,
# including any warranty of merchantability and warranty of fitness for a particular
# purpose.
##################################################################################

##################################################################################
#
# Date Completed: September 30, 2019
# Author: John Bumgarner
#
# Date Revised: September 17, 2020
# Revised by: John Bumgarner
#
# This Python script is designed to measure the frequency of ovation expressions
# (applause) and auditory cues (laugher) during a specific State of the Union
# address within the corpus. These frequencies are than displayed by year and
# number of occurrences using the plotting library Matplotlib.
#
# Modules used:
# 1. matplotlib
# 2. pandas
# 3. re
#
# Module References:
# https://matplotlib.org/
# https://pandas.pydata.org/
# https://docs.python.org/3/library/re.html
#
##################################################################################

################################################
# Python imports required for basic operations
################################################
import matplotlib.pyplot as plt
import pandas as pd
import re as regex


def get_sotu_speech(current_speech):
    """
    This function opens a particular State of the Union Address file,
    and returns it as a file object.

    :param current_speech: the sotu being processed
    :return: file object
    """
    infile = open(f'sotu_speeches_unprepared_text/{current_speech}', 'r', encoding='utf-8')
    return infile


def find_ovation_expressions(input_file):
    """
    This function looks for the word applause in a particular
    State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of mentions of applause in the speech
    """
    readlines = input_file.readlines()
    applause_counter = 0
    keywords = {'ovation': ['applause']}
    for key, values in keywords.items():
        for line in readlines:
            for item in values:
                result = regex.findall(fr'\b{item}\b', line.lower())
                if result:
                    applause_counter += len(result)
    return applause_counter


def measure_number_of_claps(sotu_speeches):
    """
    This function processes all the sotu speeches, while
    searching for a particular ovation expression.

    :param sotu_speeches: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_applause = pd.DataFrame(columns=['president', 'year', 'claps'])

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
    """
    This function looks for the word laughter in a particular
    State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of mentions of laughter in the speech
    """
    readlines = input_file.readlines()
    laughter_counter = 0
    keywords = {'audible': ['laughter']}
    for key, values in keywords.items():
        for line in readlines:
            for item in values:
                result = regex.findall(fr'\b{item}\b', line.lower())
                if result:
                    laughter_counter += len(result)
    return laughter_counter


def measure_number_of_laughs(sotu_speeches):
    """
    This function processes all the sotu speeches, while
    searching for a particular audible expression.

    :param sotu_speeches: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_laughter = pd.DataFrame(columns=['president', 'year', 'laughs'])

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


# State of the Union Addresses within the corpus analyzed
sotu_speeches = {'2019': ('Trump','trump_sotu_2019.txt'),
                 '2018': ('Trump','trump_sotu_2018.txt'),
                 '2017': ('Trump','trump_sotu_2017.txt'),
                 '2016': ('Obama', 'obama_sotu_2016.txt'),
                 '2015': ('Obama', 'obama_sotu_2015.txt'),
                 '2014': ('Obama', 'obama_sotu_2014.txt'),
                 '2013': ('Obama', 'obama_sotu_2013.txt'),
                 '2012': ('Obama', 'obama_sotu_2012.txt'),
                 '2011': ('Obama', 'obama_sotu_2011.txt'),
                 '2010': ('Obama', 'obama_sotu_2010.txt'),
                 '2008': ('Bush', 'georgewbush_sotu_2008.txt'),
                 '2007': ('Bush', 'georgewbush_sotu_2007.txt'),
                 '2006': ('Bush', 'georgewbush_sotu_2006.txt'),
                 '2005': ('Bush', 'georgewbush_sotu_2005.txt'),
                 '2004': ('Bush', 'georgewbush_sotu_2004.txt'),
                 '2003': ('Bush', 'georgewbush_sotu_2003.txt'),
                 '2002': ('Bush', 'georgewbush_sotu_2002.txt')}


presidential_applause = measure_number_of_claps(sotu_speeches)
presidential_laughs = measure_number_of_laughs(sotu_speeches)

# This code creates a bar chart that shows the number of times that
# the audience clapped during a particular State of the Union Address
presidential_applause.plot(kind='bar', x='year', y='claps', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n audience applause', fontweight='demibold')
plt.ylabel('applause count', fontsize=10, fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
# tight_layout automatically adjusts subplot params so that the subplot(s) fits in to the figure area.
plt.tight_layout()
plt.show()

# This code creates a bar chart that shows the number of times that
# the audience laughed during a particular State of the Union Address
presidential_laughs.plot(kind='bar', x='year', y='laughs', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n audience laughter', fontweight='demibold')
plt.ylabel('laughter count', fontsize=10, fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
# tight_layout automatically adjusts subplot params so that the subplot(s) fits in to the figure area.
plt.tight_layout()
plt.show()
