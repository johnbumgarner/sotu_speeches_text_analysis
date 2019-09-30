
from functools import reduce

import matplotlib.pyplot as plt
import pandas as pd
import re as regex

def get_sotu_speech(current_speech):
    '''
    This function opens a particular State of the Union Address file,
    and returns it as a file object.

    :param current_speech: the sotu being processed
    :return: file object
    '''
    infile = open(current_speech, 'r', encoding='utf-8')
    return infile

# both political parties

def find_bipartisan_references(input_file):
  '''
	This function looks for the word bipartisan in a particular
	State of the Union Address given by a U.S. President.

	:param input_file: sotu speech being processed
	:return: number of bipartisan references in the speech
	'''
  readlines = input_file.readlines()
  bipartisan_counter = 0
  keywords = {'bipartisan': ['bipartisan', 'both political parties']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          bipartisan_counter += len(result)
  return bipartisan_counter

def number_of_bipartisan_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for the keyword bipartisan.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_bipartisan = pd.DataFrame(columns=['president', 'year', 'bipartisan'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      bipartisan = find_bipartisan_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'bipartisan': bipartisan}
      df_bipartisan = df_bipartisan.append(df1, ignore_index=True)

  return df_bipartisan

def find_border_security_references(input_file):
  '''
	This function looks for words associated with border security issues
	in a particular State of the Union Address given by a U.S. President.

	:param input_file: sotu speech being processed
	:return: number of border security references in the speech
	'''
  readlines = input_file.readlines()
  border_security_counter = 0
  keywords = {'border_security': ['border crossings', 'border protection', 'secure our border', 'secure our borders', 'security wall', 'southern border']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          border_security_counter += len(result)
  return border_security_counter

def number_of_border_security_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for words associated with border security issues.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_border_security = pd.DataFrame(columns=['president', 'year', 'border security'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      border_security = find_border_security_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'border security': border_security}
      df_border_security = df_border_security.append(df1, ignore_index=True)

  return df_border_security

def find_democrat_references(input_file):
  '''
	This function looks for words associated with the democratic party
	in a particular State of the Union Address given by a U.S. President.

	:param input_file: sotu speech being processed
	:return: number of democrat references in the speech
	'''
  readlines = input_file.readlines()
  democrat_counter = 0
  keywords = {'democrats': ['democrat', 'democrats', 'democratic party']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          democrat_counter += len(result)
  return democrat_counter

def number_of_democrat_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for words associated with the democratic party.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_democrat = pd.DataFrame(columns=['president', 'year', 'democrat'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      democrats = find_democrat_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'democrat': democrats}
      df_democrat = df_democrat.append(df1, ignore_index=True)

  return df_democrat

def find_environmental_references(input_file):
    '''
    This function looks for words associated with environmental issues
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of environmental references in the speech
    '''
    readlines = input_file.readlines()
    environmental_counter = 0
    keywords = {'environmental': ['alternative fuels', 'carbon dioxide', 'carbon pollution', 'clean coal technology', 'clean energy', 'clean water', 'cleaner power',
                                  'climate change', 'co2', 'droughts', 'efficient buildings', 'emissions', 'energy-efficient', 'energy wasted', 'environment clean',
                                  'extreme weather', 'floods', 'fossil fuels', 'global warming', 'greenhouse gases', 'heat waves', 'hybrid vehicles', 'melting permafrost',
                                  'methane', 'ocean temperatures', 'paris accord', 'paris agreement', 'renewable power', 'rising oceans', 'solar', 'temperatures increasing',
                                  'wildfires', 'wind energy']}
    for key, values in keywords.items():
      for line in readlines:
        for item in values:
          result = regex.findall(fr'\b{item}\b', line.lower())
          if result:
            environmental_counter += len(result)
    return environmental_counter

def number_of_environmental_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for words associated with environmental issues.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_environment = pd.DataFrame(columns=['president', 'year', 'environment'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      environment = find_environmental_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'environment': environment}
      df_environment  = df_environment.append(df1, ignore_index=True)

  return df_environment

def find_healthcare_references(input_file):
    '''
    This function looks for words associated with healthcare issues
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of healthcare references in the speech
    '''
    readlines = input_file.readlines()
    healthcare_counter = 0
    keywords = {'healthcare': ['affordable care act', 'cancer research', 'cure cancer', 'experimental treatment', 'generic drugs', 'health care', 'health coverage',
                               'healthcare','health insurance','health plans', 'health security', 'high drug prices', 'medical care', 'medical devices',
                               'medical liability','medical research', 'medicaid', 'medicare', 'obamacare', 'prescription drugs', 'terminal conditions',
                               'terminal illness']}
    for key, values in keywords.items():
      for line in readlines:
        for item in values:
          result = regex.findall(fr'\b{item}\b', line.lower())
          if result:
            healthcare_counter += len(result)
    return healthcare_counter

def number_of_healthcare_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for words associated with healthcare.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_healthcare = pd.DataFrame(columns=['president', 'year', 'healthcare'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      healthcare = find_healthcare_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'healthcare': healthcare}
      df_healthcare  = df_healthcare.append(df1, ignore_index=True)

  return df_healthcare

def find_immigration_references(input_file):
    '''
    This function looks for words associated with immigration issues
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of immigration references in the speech
    '''
    readlines = input_file.readlines()
    immigration_counter = 0
    keywords = {'immigration': ['illegal aliens','illegal migration', 'immigration']}
    for key, values in keywords.items():
      for line in readlines:
        for item in values:
          result = regex.findall(fr'\b{item}\b', line.lower())
          if result:
            immigration_counter += len(result)
    return immigration_counter

def number_of_immigration_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for words associated with immigration.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_immigration = pd.DataFrame(columns=['president', 'year', 'immigration'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      immigration = find_immigration_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'immigration': immigration}
      df_immigration  = df_immigration.append(df1, ignore_index=True)

  return df_immigration

def find_jobs_references(input_file):
    '''
    This function looks for words associated with employment issues
    in a particular State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of employment references in the speech
    '''
    readlines = input_file.readlines()
    jobs_counter = 0
    keywords = {'jobs': ['job', 'jobs', 'working familities']}
    for key, values in keywords.items():
      for line in readlines:
        for item in values:
          result = regex.findall(fr'\b{item}\b', line.lower())
          if result:
            jobs_counter += len(result)
    return jobs_counter

def number_of_jobs_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for words associated with employment.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_jobs = pd.DataFrame(columns=['president', 'year', 'jobs'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      jobs = find_jobs_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'jobs': jobs}
      df_jobs  = df_jobs.append(df1, ignore_index=True)

  return df_jobs

def find_military_references(input_file):
  '''
  This function looks for words associated with the armed forces in a
  particular State of the Union Address given by a U.S. President.

  :param input_file: sotu speech being processed
  :return: number of armed forces references in the speech
  '''
  readlines = input_file.readlines()
  military_counter = 0
  keywords = {'military': ['air force', 'american forces', 'american troops', 'american soldiers', 'armed forces', 'army', 'coast guard', 'department of defense',
                           'marines', 'military', 'nato', 'navy', 'veterans']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          military_counter += len(result)
  return military_counter

def number_of_military_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for words associated with the armed forces.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_military = pd.DataFrame(columns=['president', 'year', 'military'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      military = find_military_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'military': military }
      df_military  =  df_military.append(df1, ignore_index=True)

  return df_military

def find_nutritional_references(input_file):
  '''
  This function looks for words associated with nutritional issues in a
  particular State of the Union Address given by a U.S. President.

  :param input_file: sotu speech being processed
  :return: number of nutritional references in the speech
  '''
  readlines = input_file.readlines()
  nutrition_counter = 0
  keywords = {'nutritional': ['famine','feeding the hungry', 'food aid', 'food assistance', 'food stamp', 'food stamps', 'global hunger', 'healthy food',
                              'little food', 'needy families', 'snap', 'starvation']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          nutrition_counter += len(result)
  return nutrition_counter

def number_of_nutritional_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for words associated with nutritional issues.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_nutrition = pd.DataFrame(columns=['president', 'year', 'nutritional'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      nutritional = find_nutritional_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'nutritional': nutritional}
      df_nutrition = df_nutrition.append(df1, ignore_index=True)

  return  df_nutrition

def find_superlative_references(input_file):
  '''
  This function looks for superlative words in a particular
  State of the Union Address given by a U.S. President.

  :param input_file: sotu speech being processed
  :return: number of superlatives in the speech
  '''
  readlines = input_file.readlines()
  superlative_counter = 0
  keywords = {'superlative': ['most beautiful', 'biggest', 'bravest', 'brightest', 'glorious', 'greatest', 'happiest', 'highest', 'hottest', 'incredible', 'largest',
                              'longest', 'magnificent', 'marvelous', 'nicest', 'safest', 'smartest', 'spectacular', 'strongest', 'toughest', 'wealthiest',
                              'wonderful']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          superlative_counter += len(result)
  return superlative_counter

def number_of_superlative_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for superlative words.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_superlative = pd.DataFrame(columns=['president', 'year', 'superlative'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      superlative = find_superlative_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'superlative': superlative}
      df_superlative  = df_superlative.append(df1, ignore_index=True)

  return df_superlative

def find_religious_references(input_file):
  '''
  This function looks for religious words in a particular
  State of the Union Address given by a U.S. President.

  :param input_file: sotu speech being processed
  :return: number of religious references in the speech
  '''
  readlines = input_file.readlines()
  religious_counter = 0
  keywords = {'religious': ['bible', 'christian', 'church', 'god', 'holiness', 'holy land', 'islam', 'jerusalem', 'judaism']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          religious_counter += len(result)
  return religious_counter

def number_of_religious_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for religious words.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_religious = pd.DataFrame(columns=['president', 'year', 'religious'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      religious = find_religious_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'religious': religious}
      df_religious  = df_religious.append(df1, ignore_index=True)

  return df_religious


def find_republican_references(input_file):
  '''
	This function looks for words associated with the republican party
	in a particular State of the Union Address given by a U.S. President.

	:param input_file: sotu speech being processed
	:return: number of republican party references in the speech
	'''
  readlines = input_file.readlines()
  republican_counter = 0
  keywords = {'republican': ['republican', 'republicans', 'republican party']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          republican_counter += len(result)
  return republican_counter

def number_of_republican_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for words associated with the republican party.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_republican = pd.DataFrame(columns=['president', 'year', 'republican'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      republicans = find_republican_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'republican': republicans}
      df_republican = df_republican.append(df1, ignore_index=True)

  return df_republican

def find_retirement_references(input_file):
  '''
  This function looks for words associated with retirement in a
  particular State of the Union Address given by a U.S. President.

  :param input_file: sotu speech being processed
  :return: number of retirement references in the speech
  '''
  readlines = input_file.readlines()
  retirement_counter = 0
  keywords = {'retirement': ['401(k)', 'death tax', 'pension', 'retirement', 'savings accounts', 'social security', 'thrift savings plan']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          retirement_counter += len(result)
  return retirement_counter

def number_of_retirement_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while searching
  for words associated with retirement.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_retirement = pd.DataFrame(columns=['president', 'year', 'retirement'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      retirement = find_retirement_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'retirement': retirement}
      df_retirement  =  df_retirement.append(df1, ignore_index=True)

  return df_retirement

def find_taxes_references(input_file):
    '''
    This function looks for words associated with taxes in a particular
    State of the Union Address given by a U.S. President.

    :param input_file: sotu speech being processed
    :return: number of tax references in the speech
    '''
    readlines = input_file.readlines()
    taxes_counter = 0
    keywords = {'taxes': ['child credit', 'federal taxes', 'death tax', 'marriage penalty',' tax code', 'tax credits', 'tax cuts', 'tax increase'', tax rates',
                          'tax reductions', 'tax reform', 'taxes', 'taxpayer']}
    for key, values in keywords.items():
      for line in readlines:
        for item in values:
          result = regex.findall(fr'\b{item}\b', line.lower())
          if result:
            taxes_counter += len(result)
    return taxes_counter

def number_of_taxes_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for words associated with taxes.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_taxes = pd.DataFrame(columns=['president', 'year', 'taxes'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      taxes = find_taxes_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'taxes': taxes}
      df_taxes  = df_taxes.append(df1, ignore_index=True)

  return df_taxes

def find_terrorism_references(input_file):
  '''
  This function looks for words associated with terrorism in a
  particular State of the Union Address given by a U.S. President.

  :param input_file: sotu speech being processed
  :return: number of terrorism references in the speech
  '''
  readlines = input_file.readlines()
  terrorism_counter = 0
  keywords = {'terrorism': ['al qaeda', 'bioterrorism', 'extremism', 'extremists', 'fighting terror', 'hamas', 'hezbollah', 'isil', 'isis', 'islamic jihad',
                            'jaish-i-mohammed', 'terrorism', 'terrorist', 'terrorists', 'terror camps', 'terror cells', 'terror states', 'war against terror',
                            'war on terror', 'weapons of terror']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          terrorism_counter += len(result)
  return terrorism_counter

def number_of_terrorism_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while
  searching for words associated with terrorism.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_terrorism = pd.DataFrame(columns=['president', 'year', 'terrorism'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      terrorism = find_terrorism_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'terrorism': terrorism}
      df_terrorism  =  df_terrorism.append(df1, ignore_index=True)

  return df_terrorism

def find_trade_references(input_file):
  '''
  This function looks for words associated with trade in a particular
  State of the Union Address given by a U.S. President.

  :param input_file: sotu speech being processed
  :return: number of trade references in the speech
  '''
  readlines = input_file.readlines()
  wmd_counter = 0
  keywords = {'trade': ['made in america', 'nafta', 'trade deficit', 'trade surplus', 'tariff', 'trans-pacific partnership', 'tpp', 'transatlantic trade']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          wmd_counter += len(result)
  return wmd_counter

def number_of_trade_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while searching
  for words associated with weapons of mass destruction.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_trade = pd.DataFrame(columns=['president', 'year', 'trade'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      trade = find_trade_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'trade': trade}
      df_trade  =  df_trade.append(df1, ignore_index=True)

  return df_trade

def find_wmd_references(input_file):
  '''
  This function looks for words associated with weapons of mass destruction
  in a particular State of the Union Address given by a U.S. President.

  :param input_file: sotu speech being processed
  :return: number of weapons of mass destruction references in the speech
  '''
  readlines = input_file.readlines()
  wmd_counter = 0
  keywords = {'WMD': ['anthrax', 'biological weapons', 'botulinum toxin', 'chemical agents',' chemical attack', 'ebola', 'enrich uranium', 'germ warfare', 'nuclear materials',
                      'nuclear program', 'nuclear weapon', 'nuclear weapons', 'plague', 'sarin', 'uranium stockpile', 'weapons of mass destruction']}
  for key, values in keywords.items():
    for line in readlines:
      for item in values:
        result = regex.findall(fr'\b{item}\b', line.lower())
        if result:
          wmd_counter += len(result)
  return wmd_counter

def number_of_wmd_references(sotu_speeches):
  '''
  This function processes all the sotu speeches, while searching
  for words associated with weapons of mass destruction.

  :param sotu_speeches: a dictionary of sotu speeches filename
  :return: pandas dataframe
  '''
  df_wmd = pd.DataFrame(columns=['president', 'year', 'wmd'])

  number_of_speeches = len(sotu_speeches)
  if number_of_speeches != 0:
    for key, value in sotu_speeches.items():
      number_of_speeches -= 1
      president_name = value[0]
      speech = value[1]

      current_speech = get_sotu_speech(speech)

      wmd = find_wmd_references(current_speech)

      df1 = {'president': president_name, 'year': key, 'wmd': wmd}
      df_wmd  =  df_wmd.append(df1, ignore_index=True)

  return df_wmd

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

bipartisan_references = number_of_bipartisan_references(sotu_speeches)
democrat_references = number_of_democrat_references(sotu_speeches)
republican_references = number_of_republican_references(sotu_speeches)
df_combined = (bipartisan_references[['president','year','bipartisan']], democrat_references[['year','democrat']], republican_references[['year','republican']])
political_parties_references = reduce(lambda left,right: pd.merge(left,right, on='year'), df_combined)
political_parties_references.plot(kind='bar', x='year', legend=True)
plt.title('State of the Union Addresses 2002-2019 \n political parties references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

bipartisan_references = number_of_bipartisan_references(sotu_speeches)
bipartisan_references.plot(kind='bar', x='year', y='bipartisan', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n bipartisan references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

border_security_references = number_of_border_security_references(sotu_speeches)
border_security_references.plot(kind='bar', x='year', y='border security', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n border security references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

environmental_references = number_of_environmental_references(sotu_speeches)
environmental_references.plot(kind='bar', x='year', y='environment', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n environmental references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

healthcare_references = number_of_healthcare_references(sotu_speeches)
healthcare_references.plot(kind='bar', x='year', y='healthcare', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n healthcare references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

immigration_references = number_of_immigration_references(sotu_speeches)
immigration_references.plot(kind='bar', x='year', y='immigration', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n immigration references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

jobs_references = number_of_jobs_references(sotu_speeches)
jobs_references.plot(kind='bar', x='year', y='jobs', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n work references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

military_references = number_of_military_references(sotu_speeches)
military_references.plot(kind='bar', x='year', y='military', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n armed forces references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

nutritional_references = number_of_nutritional_references(sotu_speeches)
nutritional_references.plot(kind='bar', x='year', y='nutritional', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n nutritional references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

religious_references = number_of_religious_references(sotu_speeches)
religious_references.plot(kind='bar', x='year', y='religious', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n religious references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

retirement_references = number_of_retirement_references(sotu_speeches)
retirement_references.plot(kind='bar', x='year', y='retirement', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n retirement references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

superlative_references = number_of_superlative_references(sotu_speeches)
superlative_references.plot(kind='bar', x='year', y='superlative', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n superlative usage', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

taxes_references = number_of_taxes_references(sotu_speeches)
taxes_references.plot(kind='bar', x='year', y='taxes', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n taxes references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

terrorism_references = number_of_terrorism_references(sotu_speeches)
terrorism_references.plot(kind='bar', x='year', y='terrorism', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n terrorism references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

trade_references = number_of_trade_references(sotu_speeches)
trade_references.plot(kind='bar', x='year', y='trade', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n trade references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()

wmd_references = number_of_wmd_references(sotu_speeches)
wmd_references.plot(kind='bar', x='year', y='wmd', legend=False)
plt.title('State of the Union Addresses 2002-2019 \n weapons of mass destruction references', fontweight='demibold')
plt.tick_params(direction='out', length=5, color='orange')
plt.show()