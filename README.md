# Overview

<p align="justify">
This repository contains Python code used for various text analysis experiments. The corpuses used for these experiments were the State of the Union Addresses for the Presidential periods below: 
  
- Donald Trump - 2017 to 2019
- Barack Obama - 2010 to 2016
- George W. Bush - 2002 to 2008
</p>

### Experiment 1:

<p align="justify">
This experiment used the Python modules matplotlib and pandas.  The objective of this experiment was to calculate the number of times the audience either clapped or laughed during a particular State of the Union Address. The corpuses used contained meta data, which indicates what parts of the speech gathered applause or laugher.  The metrics generated are only as reliable as the data being processed. The applause and laugher keywords were manually added to the speech text by an unknown entity.  This experiment did not validate these keywords, which could have been accomplished by watching the 17 State of Union Addresses.  Additionally, these metrics cannot determine if the audience applauded for 10 seconds or 60 seconds. 
</p>

<p align="justify">
The applause metrics were generated from the unverified corpuses obtained from the multiple websites, including the White House. The applause metrics indicate that President Trump's State of the Union Addresses for 2019 and 2018 received the highest levels of applause over a 17 year period. The average applause number per speech for the same 17 year period was 55.  Additional analysis is required to determine what topics garnered applause and if this applause was bipartisan or partisan in nature. 
</p>
<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_applause_metrics.png">
</p>

<p align="justify">
The laughter metrics were also generated from the same unverified corpuses. The laughter metrics indicate that President Obama's speeches obtained the most laughs. His State of the Union Address in 2010 received 9 laughs, which makes this speech the funniest over the 17 year period. The average laughs per speech was 2.8. Additional analysis is required to determine what topics garnered laughter and if this laughter was bipartisan or partisan in nature. 
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_laughter_metrics.png">
</p>

### Experiment 2:

<p align="justify">
This experiment also used the Python modules matplotlib and pandas. The objective of this experiment was to calculate the number of times a specific topic was mentioned in an individual speech.  The topics included economy, environment, healthcare, immigration, taxes, terrorism and weapons of mass destruction. Most topics had associated keywords, which were manually extracted from the speeches. This extraction method identified bigrams and trigrams that would have been potentially missed using some of natural language processing (NLP) modules that remove stopwords, such as 'of' or 'on.' 
  
Below is an example of a topic and its associated keywords:

- Topic: terrorism
- Keywords: al qaeda, bioterrorism, extremism, extremists, fighting terror, hamas, hezbollah, isis, islamic jihad, jaish-i-mohammed, terrorism, terrorist, terrorists, terror camps, terror states, war against terror, war on terror, weapons of terror
</p>

<p align="justify">
Since September 11, 2001, terrorism has been mentioned in every State of the Union Address by 3 different administrations. Of course President Bush spoke about terrorism the most in his speeches, because he was the president immediately following al-Qaeda's attacks on America.  
</p> 

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_terrorism_metrics.png">
</p>

<p align="justify">
Weapons of Mass destruction (WMD) were mentioned in 16 of the 17 State of the Union Addresses analyzed. In President Bush's 2003 speech he referenced WMD 29 times and terrorism 28 times. It is worth noting that this speech was used by President Bush to declare his intentions to launch military operations on Iraq for the purpose of locating WMDs allegedly hidden by Saddam Hussein.  Bush's 2003 State of the Union was on Jan 28, 2003 and the invasion of Iraq commenced on March 19, 2003.
</p> 

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_wmd_metrics.png">
</p>

<p align="justify">
</p>


<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_healthcare_metrics.png">
</p>

<p align="justify">
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_environmental_metrics.png">
</p>

<p align="justify">
Another topic was political parties. The frequency of the keywords, bipartisan, democrat(s), democratic party, republican(s), and republican party were measured for this topic.  President Obama a democrat mentioned the republican party more frequently in his speeches than the republican Presidents Bush and Trump.  President Obama also used all the keywords more frequently in his speeches.  President Bush used the keywords the least in his speeches.
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_political_parties_metrics.png">
</p>

<p align="justify">
Religion references were also analyzed in the State of Union Addresses corpuses used in this experiment. The keywords measured were:
bible, christian, church, god, holiness, holy land, islam, jerusalem, and judaism. President Bush and President Trump, both republicans used religious references more frequently than President Obama, a democratic president. 
</p>
  
<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_religious_metrics.png">
</p>

<p align="justify">
This experiment also looked at the usage of superlatives by a President. A superlative is an exaggerated or hyperbolical expression.  These words can be used to describe an object at the highest (e.g., wealthiest) or lowest limit (e.g., poorest).  Some of the superlative used by Presidents included most beautiful, bravest, hottest, safest, smartest and toughest.  President Trump used the highest number of superlatives in his 2019 address.  President Bush used the least number of superlatives in his speeches.  
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_superlative_metrics.png">
</p>

### Notes:

_The code within this repository is **not** production ready. It was **strictly** designed for experimental testing purposes only._


