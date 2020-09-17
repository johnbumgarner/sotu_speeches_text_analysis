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
# Date Revised: September 17, 2019
# Revised by: John Bumgarner
#
# This Python script is designed to measure the frequency of various n-grams within
# a specific State of the Union address within the corpus. The n-grams frequency
# of occurrence are than displayed by year and number of occurrences using the plotting
# library Matplotlib.
#
# Modules used:
# 1. matplotlib
# 2. pandas
# 3. re
# 4. functools
#
# Module References:
# https://matplotlib.org/
# https://pandas.pydata.org/
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3.0/library/functools.html
#
##################################################################################

################################################
# Python imports required for basic operations
################################################
from functools import reduce
import matplotlib.pyplot as plt
import pandas as pd
import re as regex

# State of the Union Addresses within the corpus analyzed
sotu_speeches = {'2019': ('Trump', 'trump_sotu_2019.txt'),
                 '2018': ('Trump', 'trump_sotu_2018.txt'),
                 '2017': ('Trump', 'trump_sotu_2017.txt'),
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

topic_keywords = {'bipartisan': ['bipartisan', 'both political parties'],
                  'border_security': ['border crossings', 'border protection', 'secure our border',
                                      'secure our borders', 'security wall', 'southern border'],
                  'democrats': ['democrat', 'democrats', 'democratic party'],
                  'environmental': ['alternative fuels', 'carbon dioxide', 'carbon pollution', 'clean coal technology',
                                    'clean energy', 'clean water', 'cleaner power', 'climate change', 'co2', 'droughts',
                                    'efficient buildings', 'emissions', 'energy-efficient', 'energy wasted',
                                    'environment clean', 'extreme weather', 'floods', 'fossil fuels', 'global warming',
                                    'greenhouse gases', 'heat waves', 'hybrid vehicles', 'melting permafrost',
                                    'methane', 'ocean temperatures', 'paris accord', 'paris agreement',
                                    'renewable power', 'rising oceans', 'solar', 'temperatures increasing', 'wildfires',
                                    'wind energy'],
                  'healthcare': ['affordable care act', 'cancer research', 'cure cancer', 'experimental treatment',
                                 'generic drugs', 'health care', 'health coverage', 'healthcare', 'health insurance',
                                 'health plans', 'health security', 'high drug prices', 'medical care',
                                 'medical devices', 'medical liability', 'medical research', 'medicaid', 'medicare',
                                 'obamacare', 'prescription drugs', 'terminal conditions', 'terminal illness'],
                  'immigration': ['illegal aliens', 'illegal migration', 'immigration'],
                  'jobs': ['job', 'jobs', 'working familities'],
                  'military': ['air force', 'american forces', 'american troops', 'american soldiers', 'armed forces',
                               'army', 'coast guard', 'department of defense', 'marines', 'military', 'nato', 'navy',
                               'veterans'],
                  'nutritional': ['famine', 'feeding the hungry', 'food aid', 'food assistance', 'food stamp',
                                  'food stamps', 'global hunger', 'healthy food', 'little food', 'needy families',
                                  'snap', 'starvation'],
                  'superlative': ['most beautiful', 'biggest', 'bravest', 'brightest', 'glorious', 'greatest',
                                  'happiest', 'highest', 'hottest', 'incredible', 'largest', 'longest', 'magnificent',
                                  'marvelous', 'nicest', 'safest', 'smartest', 'spectacular', 'strongest', 'toughest',
                                  'wealthiest', 'wonderful'],
                  'religious': ['bible', 'christian', 'church', 'god', 'holiness', 'holy land', 'islam', 'jerusalem',
                                'judaism'],
                  'republican': ['republican', 'republicans', 'republican party'],
                  'retirement': ['401(k)', 'death tax', 'pension', 'retirement', 'savings accounts', 'social security',
                                 'thrift savings plan'],
                  'taxes': ['child credit', 'federal taxes', 'death tax', 'marriage penalty', ' tax code',
                            'tax credits', 'tax cuts', 'tax increase', 'tax rates', 'tax reductions', 'tax reform',
                            'taxes', 'taxpayer'],
                  'terrorism': ['al qaeda', 'bioterrorism', 'extremism', 'extremists', 'fighting terror', 'hamas',
                                'hezbollah', 'isil', 'isis', 'islamic jihad', 'jaish-i-mohammed', 'terrorism',
                                'terrorist', 'terrorists', 'terror camps', 'terror cells', 'terror states',
                                'war against terror', 'war on terror', 'weapons of terror'],
                  'trade': ['made in america', 'nafta', 'trade deficit', 'trade surplus', 'tariff',
                            'trans-pacific partnership', 'tpp', 'transatlantic trade'],
                  'WMD': ['anthrax', 'biological weapons', 'botulinum toxin', 'chemical agents', ' chemical attack',
                          'ebola', 'enrich uranium', 'germ warfare', 'nuclear materials', 'nuclear program',
                          'nuclear weapon', 'nuclear weapons', 'plague', 'sarin', 'uranium stockpile',
                          'weapons of mass destruction']}


def get_sotu_speech(current_speech):
    """
    This function opens a particular State of the Union Address file,
    and returns it as a file object.

    :param current_speech: the sotu being processed
    :return: file object
    """
    infile = open(f'sotu_speeches/{current_speech}', 'r', encoding='utf-8')
    return infile


def find_bipartisan_references(input_file):
    """
    This function looks for the word bipartisan in a particular
    State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of bipartisan references in the speech
    """
    lines = input_file.readlines()
    bipartisan_counter = 0
    values = ([value for value in topic_keywords.get('bipartisan')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                bipartisan_counter += len(result)
    return bipartisan_counter


def frequency_of_bipartisan_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for the keyword bipartisan.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_bipartisan = pd.DataFrame(columns=['president', 'year', 'bipartisan'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        bipartisan = find_bipartisan_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'bipartisan': bipartisan}
        df_bipartisan = df_bipartisan.append(df1, ignore_index=True)
    return df_bipartisan


def find_border_security_references(input_file):
    """
    This function looks for words associated with border security issues
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of border security references in the speech
    """
    lines = input_file.readlines()
    border_security_counter = 0
    values = ([value for value in topic_keywords.get('border_security')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                border_security_counter += len(result)
    return border_security_counter


def frequency_of_border_security_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for words associated with border security issues.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_border_security = pd.DataFrame(columns=['president', 'year', 'border security'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        border_security = find_border_security_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'border security': border_security}
        df_border_security = df_border_security.append(df1, ignore_index=True)
    return df_border_security


def find_democrat_references(input_file):
    """
    This function looks for words associated with the democratic party
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of democrat references in the speech
    """
    lines = input_file.readlines()
    democrat_counter = 0
    values = ([value for value in topic_keywords.get('democrats')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                democrat_counter += len(result)
    return democrat_counter


def frequency_of_democrat_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for words associated with the democratic party.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_democrat = pd.DataFrame(columns=['president', 'year', 'democrat'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        democrats = find_democrat_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'democrat': democrats}
        df_democrat = df_democrat.append(df1, ignore_index=True)
    return df_democrat


def find_environmental_references(input_file):
    """
    This function looks for words associated with environmental issues
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of environmental references in the speech
    """
    lines = input_file.readlines()
    environmental_counter = 0
    values = ([value for value in topic_keywords.get('environmental')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                environmental_counter += len(result)
    return environmental_counter


def frequency_of_environmental_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for words associated with environmental issues.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_environment = pd.DataFrame(columns=['president', 'year', 'environment'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        environment = find_environmental_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'environment': environment}
        df_environment = df_environment.append(df1, ignore_index=True)
    return df_environment


def find_healthcare_references(input_file):
    """
    This function looks for words associated with healthcare issues
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of healthcare references in the speech
    """
    lines = input_file.readlines()
    healthcare_counter = 0
    values = ([value for value in topic_keywords.get('healthcare')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                healthcare_counter += len(result)
    return healthcare_counter


def frequency_of_healthcare_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for words associated with healthcare.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_healthcare = pd.DataFrame(columns=['president', 'year', 'healthcare'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        healthcare = find_healthcare_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'healthcare': healthcare}
        df_healthcare = df_healthcare.append(df1, ignore_index=True)
    return df_healthcare


def find_immigration_references(input_file):
    """
    This function looks for words associated with immigration issues
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of immigration references in the speech
    """
    lines = input_file.readlines()
    immigration_counter = 0
    values = ([value for value in topic_keywords.get('immigration')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                immigration_counter += len(result)
    return immigration_counter


def frequency_of_immigration_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for words associated with immigration.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_immigration = pd.DataFrame(columns=['president', 'year', 'immigration'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        immigration = find_immigration_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'immigration': immigration}
        df_immigration = df_immigration.append(df1, ignore_index=True)
    return df_immigration


def find_jobs_references(input_file):
    """
    This function looks for words associated with employment issues
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of employment references in the speech
    """
    lines = input_file.readlines()
    jobs_counter = 0
    values = ([value for value in topic_keywords.get('jobs')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                jobs_counter += len(result)
    return jobs_counter


def frequency_of_jobs_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for words associated with employment.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_jobs = pd.DataFrame(columns=['president', 'year', 'jobs'])
    for key, value in sotu_speeches.items():
        current_speech = get_sotu_speech(value[1])
        jobs = find_jobs_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'jobs': jobs}
        df_jobs = df_jobs.append(df1, ignore_index=True)
    return df_jobs


def find_military_references(input_file):
    """
    This function looks for words associated with the armed forces in a
    particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of armed forces references in the speech
    """
    lines = input_file.readlines()
    military_counter = 0
    values = ([value for value in topic_keywords.get('military')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                military_counter += len(result)
    return military_counter


def frequency_of_military_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for words associated with the armed forces.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_military = pd.DataFrame(columns=['president', 'year', 'military'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        military = find_military_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'military': military}
        df_military = df_military.append(df1, ignore_index=True)
    return df_military


def find_nutritional_references(input_file):
    """
    This function looks for words associated with nutritional issues in a
    particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of nutritional references in the speech
    """
    lines = input_file.readlines()
    nutrition_counter = 0
    values = ([value for value in topic_keywords.get('nutritional')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                nutrition_counter += len(result)
    return nutrition_counter


def frequency_of_nutritional_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for words associated with nutritional issues.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_nutrition = pd.DataFrame(columns=['president', 'year', 'nutritional'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        nutritional = find_nutritional_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'nutritional': nutritional}
        df_nutrition = df_nutrition.append(df1, ignore_index=True)
    return df_nutrition


def find_superlative_references(input_file):
    """
    This function looks for superlative words in a particular
    State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of superlatives in the speech
    """
    lines = input_file.readlines()
    superlative_counter = 0
    values = ([value for value in topic_keywords.get('superlative')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                superlative_counter += len(result)
    return superlative_counter


def frequency_of_superlative_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for superlative words.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_superlative = pd.DataFrame(columns=['president', 'year', 'superlative'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        superlative = find_superlative_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'superlative': superlative}
        df_superlative = df_superlative.append(df1, ignore_index=True)
    return df_superlative


def find_religious_references(input_file):
    """
    This function looks for religious words in a particular
    State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of religious references in the speech
    """
    lines = input_file.readlines()
    religious_counter = 0
    values = ([value for value in topic_keywords.get('religious')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                religious_counter += len(result)
    return religious_counter


def frequency_of_religious_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for religious words.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_religious = pd.DataFrame(columns=['president', 'year', 'religious'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        religious = find_religious_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'religious': religious}
        df_religious = df_religious.append(df1, ignore_index=True)
    return df_religious


def find_republican_references(input_file):
    """
    This function looks for words associated with the republican party
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of republican party references in the speech
    """
    lines = input_file.readlines()
    republican_counter = 0
    values = ([value for value in topic_keywords.get('republican')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                republican_counter += len(result)
    return republican_counter


def frequency_of_republican_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for words associated with the republican party.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_republican = pd.DataFrame(columns=['president', 'year', 'republican'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        republicans = find_republican_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'republican': republicans}
        df_republican = df_republican.append(df1, ignore_index=True)
    return df_republican


def find_retirement_references(input_file):
    """
    This function looks for words associated with retirement in a
    particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of retirement references in the speech
    """
    lines = input_file.readlines()
    retirement_counter = 0
    values = ([value for value in topic_keywords.get('retirement')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                retirement_counter += len(result)
    return retirement_counter


def frequency_of_retirement_references(corpus):
    """
    This function processes all the sotu speeches, while searching
    for words associated with retirement.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_retirement = pd.DataFrame(columns=['president', 'year', 'retirement'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        retirement = find_retirement_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'retirement': retirement}
        df_retirement = df_retirement.append(df1, ignore_index=True)
    return df_retirement


def find_taxes_references(input_file):
    """
    This function looks for words associated with taxes in a particular
    State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of tax references in the speech
    """
    lines = input_file.readlines()
    taxes_counter = 0
    values = ([value for value in topic_keywords.get('taxes')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                taxes_counter += len(result)
    return taxes_counter


def frequency_of_taxes_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for words associated with taxes.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_taxes = pd.DataFrame(columns=['president', 'year', 'taxes'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        taxes = find_taxes_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'taxes': taxes}
        df_taxes = df_taxes.append(df1, ignore_index=True)
    return df_taxes


def find_terrorism_references(input_file):
    """
    This function looks for words associated with terrorism in a
    particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of terrorism references in the speech
    """
    lines = input_file.readlines()
    terrorism_counter = 0
    values = ([value for value in topic_keywords.get('terrorism')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                terrorism_counter += len(result)
    return terrorism_counter


def frequency_of_terrorism_references(corpus):
    """
    This function processes all the sotu speeches, while
    searching for words associated with terrorism.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_terrorism = pd.DataFrame(columns=['president', 'year', 'terrorism'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        terrorism = find_terrorism_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'terrorism': terrorism}
        df_terrorism = df_terrorism.append(df1, ignore_index=True)
    return df_terrorism


def find_trade_references(input_file):
    """
    This function looks for words associated with trade in a particular
    State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of trade references in the speech
    """
    lines = input_file.readlines()
    trade_counter = 0
    values = ([value for value in topic_keywords.get('trade')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                trade_counter += len(result)
    return trade_counter


def frequency_of_trade_references(corpus):
    """
    This function processes all the sotu speeches, while searching
    for words associated with weapons of mass destruction.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_trade = pd.DataFrame(columns=['president', 'year', 'trade'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        trade = find_trade_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'trade': trade}
        df_trade = df_trade.append(df1, ignore_index=True)
    return df_trade


def find_wmd_references(input_file):
    """
    This function looks for words associated with weapons of mass destruction
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of weapons of mass destruction references in the speech
    """
    lines = input_file.readlines()
    wmd_counter = 0
    values = ([value for value in topic_keywords.get('WMD')])
    for item in values:
        for line in lines:
            result = regex.findall(fr'\b{item}\b', line.lower())
            if result:
                wmd_counter += len(result)
    return wmd_counter


def frequency_of_wmd_references(corpus):
    """
    This function processes all the sotu speeches, while searching
    for words associated with weapons of mass destruction.

    :param corpus: a dictionary of sotu speeches filename
    :return: pandas dataframe
    """
    df_wmd = pd.DataFrame(columns=['president', 'year', 'wmd'])
    for key, value in corpus.items():
        current_speech = get_sotu_speech(value[1])
        wmd = find_wmd_references(current_speech)
        df1 = {'president': value[0], 'year': key, 'wmd': wmd}
        df_wmd = df_wmd.append(df1, ignore_index=True)
    return df_wmd


# bipartisan_references = frequency_of_bipartisan_references(sotu_speeches)
# democrat_references = frequency_of_democrat_references(sotu_speeches)
# republican_references = frequency_of_republican_references(sotu_speeches)
# df_combined = (bipartisan_references[['president','year','bipartisan']], democrat_references[['year','democrat']], republican_references[['year','republican']])
# political_parties_references = reduce(lambda left,right: pd.merge(left,right, on='year'), df_combined)
# political_parties_references.plot(kind='bar', x='year', legend=True)
# plt.title('State of the Union Addresses 2002-2019 \n political parties references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()

# bipartisan_references = frequency_of_bipartisan_references(sotu_speeches)
# bipartisan_references.plot(kind='bar', x='year', y='bipartisan', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n bipartisan references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# border_security_references = frequency_of_border_security_references(sotu_speeches)
# border_security_references.plot(kind='bar', x='year', y='border security', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n border security references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# environmental_references = frequency_of_environmental_references(sotu_speeches)
# environmental_references.plot(kind='bar', x='year', y='environment', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n environmental references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# healthcare_references = frequency_of_healthcare_references(sotu_speeches)
# healthcare_references.plot(kind='bar', x='year', y='healthcare', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n healthcare references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# # tight_layout automatically adjusts subplot params so that the subplot(s) fits in to the figure area.
# plt.tight_layout()
# plt.show()
#
# immigration_references = frequency_of_immigration_references(sotu_speeches)
# immigration_references.plot(kind='bar', x='year', y='immigration', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n immigration references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# jobs_references = frequency_of_jobs_references(sotu_speeches)
# jobs_references.plot(kind='bar', x='year', y='jobs', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n work references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# military_references = frequency_of_military_references(sotu_speeches)
# military_references.plot(kind='bar', x='year', y='military', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n armed forces references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# nutritional_references = frequency_of_nutritional_references(sotu_speeches)
# nutritional_references.plot(kind='bar', x='year', y='nutritional', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n nutritional references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# religious_references = frequency_of_religious_references(sotu_speeches)
# religious_references.plot(kind='bar', x='year', y='religious', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n religious references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# retirement_references = frequency_of_retirement_references(sotu_speeches)
# retirement_references.plot(kind='bar', x='year', y='retirement', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n retirement references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# superlative_references = frequency_of_superlative_references(sotu_speeches)
# superlative_references.plot(kind='bar', x='year', y='superlative', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n superlative usage', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# taxes_references = frequency_of_taxes_references(sotu_speeches)
# taxes_references.plot(kind='bar', x='year', y='taxes', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n taxes references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# terrorism_references = frequency_of_terrorism_references(sotu_speeches)
# terrorism_references.plot(kind='bar', x='year', y='terrorism', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n terrorism references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# trade_references = frequency_of_trade_references(sotu_speeches)
# trade_references.plot(kind='bar', x='year', y='trade', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n trade references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
#
# wmd_references = frequency_of_wmd_references(sotu_speeches)
# wmd_references.plot(kind='bar', x='year', y='wmd', legend=False)
# plt.title('State of the Union Addresses 2002-2019 \n weapons of mass destruction references', fontweight='demibold')
# plt.tick_params(direction='out', length=5, color='orange')
# plt.tight_layout()
# plt.show()
