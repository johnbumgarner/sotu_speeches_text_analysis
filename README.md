

<p align="center">
  <img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/graphic/text-analysis.png" width="300" height="300"/>
</p>

# Overview

<p align="justify">

The primary purpose of this repository is to analyze the textual data contained within the State of the Union addresses given in the years shown below: 
  
- Donald Trump - 2017 to 2019
- Barack Obama - 2010 to 2016
- George W. Bush - 2002 to 2008

These speeches (corpuses) were obtained from 3 primary sources. The White House website and President Bush's and President Obama's offical websites. None of these corpuses were cross-referenced with their corresponding videos. The latter would allow a researcher to more precisely measure audience reaction to a particular section of a Presidential speech.  

<b>Special note:</b> <i>The only text cleaning performed within the corpuses was associated with removing specific meta data, such as "White House photographer <name> took this photo."</i>
</p>

## Concept of textual analysis

<p align="justify">

Textual analysis is a broad term for various research methodologies used to qualitatively describe, interpret and understand text data.  These methodologies are mainly used in academic research to analyze content related to media and communication studies, popular culture, sociology, and philosophy. Textual analysis allows these researchers to quickly obtain relevant insights from unstructured data. All types of information can be gleaned from textual data, especially from social media posts or news articles. Some of this information includes the overall concept of the subtext, symbolism within the text, assumptions being made and potential relative value to a subject (e.g. data science). In some cases it is possible to deduce the relative historical and cultural context of a body of text using analysis techniques coupled with knowledge from different disciplines, like linguistics and semiotics.

A subset of textual analysis is content analysis. Content analysis is the study of documents and communication artifacts. These artifacts might be texts of various formats, pictures, audio or video. Social scientists use content analysis to examine patterns in communication in a replicable and systematic manner.

In short, textual analysis consists of describing the characteristics of specific text and making interpretations to answer specific questions about the text. 
</p>


## Textual analysis techniques
<p align="justify">
  
<b>Word Frequency</b>

test

<b>Collocation</b>

<b>Concordance</b>

<b>Text Classification</b>

<b>Text Extraction</b>
</p>

# State of the Union addresses analysis

### Experiment 1:

<p align="justify">
This experiment used the Python modules matplotlib and pandas. The objective of this experiment was to calculate the number of times the audience either clapped or laughed during a particular State of the Union address. The corpus used contained meta data, which indicates what parts of the speech gathered applause or laugher. The metrics generated are only as reliable as the data being processed, because the applause and laugher keywords were manually added to the speech text by an unknown entity. This experiment did not validate these keywords, which could have been accomplished by watching the videos associated with each of the State of Union addresses within the corpus.
</p>

<p align="justify">
Additionally, the keyword-based metrics cannot determine if the audience applauded for 10 seconds or 60 seconds. For example, in President Trump's 2017 State of the Union address, the widow of Navy special operator Senior Chief William Ryan Owens, who was slain in a January 2017 raid in Yemen received a bipartisan standing ovation that lasted for one minute and 36 seconds.
</p>

<p align="justify">
The average audiance applause metric across all the State of the Union addresses in the corpus was 55 per speech. The highest number of applauses for the speeches in the corpus were associated with President Trump's State of the Union address for 2018. This speech garnered 117 applauses. President Obama's 2010 State of the Union address received 116 applauses.
</p>

<p align="justify">
Additional analysis is required to determine what topics garnered applause from the audience and if the applause was bipartisan or partisan in nature. 
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_applause_metrics.png">
</p>

<p align="justify">
The laughter metrics were also generated from the same unverified corpus. The average audiance laughter metric across all the State of the Union addresses in the corpus was 2.8 per speech. The highest number of laughs for the speeches in the corpus were associated with President Obama's State of the Union address for 2010. This speech garnered 11 laughs. The laughter metrics indicate that President Obama's speeches received 37 laughs accross his 7 speeches.  President Bush only received 8 laughs for the same number of speeches. And President Trump received 10 laughs in only 3 speeches.
</p>

<p align="justify">
Additional analysis is required to determine what topics garnered laughter and if this laughter was bipartisan or partisan in nature. 
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_laughter_metrics.png">
</p>

### Experiment 2:

<p align="justify">
This experiment also used the Python modules matplotlib and pandas. The objective of this experiment was to calculate the number of times a specific topic was mentioned in an individual speech.  The topics included economy, environment, healthcare, immigration, taxes, terrorism and weapons of mass destruction. Most topics had associated keywords, which were manually extracted from the speeches. This extraction method identified bigrams and trigrams that would have been potentially missed using some of the natural language processing (NLP) modules that commonly remove stopwords, such as 'of' or 'on.' 
  
Below is an example of a topic and its associated keywords:

- Topic: terrorism
- Keywords: al qaeda, bioterrorism, extremism, extremists, fighting terror, hamas, hezbollah, isis, islamic jihad, jaish-i-mohammed, terrorism, terrorist, terrorists, terror camps, terror states, war against terror, war on terror, weapons of terror
</p>

<p align="justify">
Since September 11, 2001, terrorism has been mentioned in every State of the Union address across 3 different administrations. Of course President Bush spoke about terrorism the greatest number of times in his speeches, because he was the president immediately following al-Qaeda's attacks on America.  
</p> 

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_terrorism_metrics.png">
</p>

<p align="justify">
Weapons of Mass destruction (WMD) were mentioned in 16 of the 17 State of the Union addresses analyzed. In President Bush's 2003 speech he referenced WMD 29 times and terrorism 28 times. It is worth noting that this speech was used by President Bush to declare his intentions to launch offensive military operations on Iraq for the express purpose of locating the WMDs allegedly being hidden by Saddam Hussein.  Bush's 2003 State of the Union was on Jan 28, 2003 and the invasion of Iraq commenced on March 19, 2003.
</p> 

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_wmd_metrics.png">
</p>

<p align="justify">
Healthcare issues in America was a talking point in every State of the Union address within the corpus, which covers 17 years and 3 different administrations.  Some of the keywords measured included affordable care act, cancer research, generic drugs, health insurance, high drug prices, Medicaid, Medicare and terminal illnesses. 
</p>

<p align="justify">
On average President Bush mentioned healthcare issues 12.6 times in his 7 State of the Union addresses. President Obama's average was 10 mentions in his 7 addresses and President Trump's average is almost 10 times per his 3 speeches within the corpus. 
</p>

<p align="justify">
President Bush mentioned healthcare issues 88 times over 7 speeches. President Bush's 2004 address mentioned healthcare 23 times, which is the highest number of mentions in a 17 year period. His 2007 State of the Union address mentioned healthcare 21 times, which is the second highest for the same period.
</p>

<p align="justify">
President Obama mentioned healthcare issues 70 times in his 7 speeches. His January 2010 address mentioned healthcare issues 15 times, which was the highest number of mentions across all of his State of the Union addresses. It is worth noting that Congress passed the Patient Protection and Affordable Care Act on March 23, 2010. Most Americans known this Act as either the Affordable Care Act or Obamacare.  
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_healthcare_metrics.png">
</p>

<p align="justify">
Global environmental issues have been a major topic for years. Currently, one of the main environmental buzzwords is climate change. Over the last 17 State of the Union addresses in the corpus this phrase was only mentioned 17 times and President Obama mentioned 15 of these. Some of the other environmental keywords measured include clean water, energy efficient, fossil fuels, hybrid vehicles, ocean temperatures and wind energy. </p>

<p align="justify">
President Obama spoke about climate change in all of his State of the Union addresses.  His 2013 speech mentioned environmental issues 18 times, which was the highest number of references spanning 3 Presidential administrations and 17 State of the Union addresses.  President Obama's 2013 address came on the heels of the 2012 United Nations Climate Change Conference. His 2010 speech contained the second highest mention and it also came on the 2010 United Nations Climate Change Conference. Additional research would be required to determine if these Climate Change Conferences influenced President Obama's addresses for the years specified. He mentioned environmental issues 80 times across 7 speeches.
</p>

<p align="justify">
President Bush's 2007 State of the Union address mentioned that new technologies would be needed to diversify America's energy supply. The context around this section of his speech was related to high gas prices and America's reliance on foreign oil from the Middle East. 
He also talked about diversify America's energy supply in his 2008 speech.  President Bush briefly touched on climate change in both speeches, but again these references were linked to diversifying America's energy supply for national security reasons and not the health of the world.
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_environmental_metrics.png">
</p>

<p align="justify">
PLACE HOLDER FOR TEXT
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_immigration_metrics.png">
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_border_security_immigration_metrics.png">
</p>



<p align="justify">
Religion references were also analyzed in the State of Union addresses used in this experiment. The keywords measured included
bible, christian, church, god, holiness, holy land, islam, jerusalem, and judaism. President Bush and President Trump, both republicans used religious references more frequently than President Obama, a democratic president. 
</p>
  
<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_religious_metrics.png">
</p>

<p align="justify">
Another topic analyzed was political parties. The frequency of the keywords, bipartisan, democrat(s), democratic party, republican(s), and republican party were measured for this topic.  President Obama a democrat mentioned the republican party more frequently in his speeches than his republican counterparts Presidents Bush and Trump.  President Obama also used all these political keywords more frequently in his speeches. President Bush used these keywords the least in his speeches.
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_political_parties_metrics.png">
</p>

<p align="justify">
This experiment also looked at the usage of superlatives by a President. A superlative is an exaggerated or hyperbolical expression.  These words can be used to describe an object at the highest (e.g., wealthiest) or lowest limit (e.g., poorest).  Some of the superlative used by Presidents included most beautiful, bravest, hottest, safest, smartest and toughest.  President Trump used the highest number of superlatives in his 2019 address. President Bush used the least number of superlatives in his speeches.  
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_superlative_metrics.png">
</p>

### Notes:

_The code within this repository is **not** production ready. It was **strictly** designed for experimental testing purposes only._
