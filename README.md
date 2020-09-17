

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

Textual analysis is a broad term for various research methodologies used to qualitatively describe, interpret and understand text data. These methodologies are mainly used in academic research to analyze content related to media and communication studies, popular culture, sociology, and philosophy. Textual analysis allows these researchers to quickly obtain relevant insights from unstructured data. All types of information can be gleaned from textual data, especially from social media posts or news articles. Some of this information includes the overall concept of the subtext, symbolism within the text, assumptions being made and potential relative value to a subject (e.g. data science). In some cases it is possible to deduce the relative historical and cultural context of a body of text using analysis techniques coupled with knowledge from different disciplines, like linguistics and semiotics.

A subset of textual analysis is content analysis. Content analysis is the study of documents and communication artifacts. These artifacts might be texts of various formats, pictures, audio or video. Social scientists use content analysis to examine patterns in communication in a replicable and systematic manner.

In short, textual analysis consists of describing the characteristics of specific text and making interpretations to answer specific questions about the text. 
</p>


## Textual analysis techniques

#### Word Frequency
<p align="justify">
Word frequency is the technique used in textual analysis to measure the frequency of a specific word or word grouping within unstructured data. Measuring the number of word occurrences in a corpus allows a researcher to garner interesting insights about the text.
</p>

#### Collocation
<p align="justify">
In corpus linguistics, a collocation is a series of words or terms that frequently co-occur within a corpus. Collocations are usually bigrams (a pair of words) and trigrams (a combination of three words). In textual analysis, identifying collocations is useful to understand the semantic structure of a corpus. And counting bigrams and trigrams as one word can improve the accuracy of the textual analysis.
</p>

#### Concordance

<p align="justify">
Human language is ambiguous: depending on the context, the same word can mean different things.  A concordance is one of the oldest of text mining tools dating back to at least the 13th century when they were used to analyze and “read” religious texts. In modern-day terms a concordance is used to identify instances in which a word or a series of words appear with a corpus and to understand these words exact meaning. Many search engines use concordance to return the query as well as the words surrounding the query. 
</p>

#### Text Classification

<p align="justify">
Text classification is the process of assigning tags or categories to unstructured data based on its content.  Text classification is  one of the most essential tasks of natural language processing, because it allows a cost-efficient way to organizing the textual data according to either topic, urgency, sentiment or intent. To accomplsh this text classifiers can use techniques, such as topic analysis, sentiment analysis, language detection or intent detection. 
  
Topic Analysis consists of assigning predefined tags to an extensive collection of text data, based on its topics or themes. Sentiment Analysis, also known as ‘opinion mining’, is the automated process of understanding the attributes of an opinion, that is, the emotions that underlie a text (e.g. positive, negative, and neutral). Language detection allows a researcher to classify a corpus based on its language. Intent detection is used to recognize the intent of a given text.
</p>

#### Text Extraction
<p align="justify">
Text extraction is a textual analysis technique which consists of extracting specific terms or expressions from a collection of text data. The most useful text extraction tasks include; named-entity recognition, keyword extraction and feature extraction.  
</p>


# State of the Union addresses analysis

## Measuring audience ovation or laugher:

<p align="justify">

The State of the Union corpus contains meta data that indicates what sections of an address garnered some form of audience response. This data allows for the basic measurement of both ovation expressions (applause) and auditory cues (laugher) during a given speech.  The meta data within these corpuses was added manually by the sources, so any metrics generated are not completely reliability, because there might be underlying biases. A more thorough analysis would require reviewing the corresponding videos for each address and linking these audience responses to the specific speech.  

Additionally, these meta-based metrics cannot determine if the audience applauded for 10 seconds or 60 seconds. For example, in President Trump's 2017 State of the Union address, the widow of Navy special operator Senior Chief William Ryan Owens, who was slain in a January 2017 raid in Yemen received a bipartisan standing ovation that lasted for one minute and 36 seconds.

The meta data showed that the average audiance applause metric was 55 within all the State of the Union addresses in the corpuses analyzed.  The highest number of applauses for a specific speech was 117 and this metric was associated with President Trump's 2018 State of the Union address. President Obama's 2010 State of the Union address received 116 applauses, which was the second highest number of ovation expressions.

Additional analysis of the corresponding videos is required to determine what topics garnered applause from the audience and if the applause was bipartisan or partisan in nature. 
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_applause_metrics.png">
</p>

<p align="justify">

The auditory cues (laugher) from the audience were also measured.  The meta data within the corpuses showed that the average audiance laugher metric was 2.8 per speech accross all the the State of the Union addresses analyzed. The highest number of audience laughs were associated with President Obama's 2010 State of the Union address, which garnered 11 laughs. Accross President Obama's 7 speeches, he received 37 laughs, which was the highest combined number of laughs. Whereas President Bush only received 8 laughs for the same number of speeches, but his speeches were given in the years following the 9/11 terrorist attacks on New York City and Washington. President Trump has received 10 laughs in his 3 speeches that were analyzed.

Additional analysis of the corresponding videos is required to determine what topics garnered laughter and if this laughter was bipartisan or partisan in nature. 
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_laughter_metrics.png">
</p>

## Topic Analysis:

<p align="justify">
  
Topic analysis was performed on the speeches with the corpus. The topics measured included economy, environment, healthcare, immigration, taxes, terrorism and weapons of mass destruction. These topics were extracted using both automated text extraction and manually.  These extraction methods identified bigrams and trigrams.  

Below is an example of a topic and its associated keywords(unigrams, bigrams and trigrams):

<b>Topic:</b> <i>terrorism</i>

<b>Keywords:</b> <i>al qaeda, bioterrorism, extremism, extremists, fighting terror, hamas, hezbollah, isis, islamic jihad, jaish-i-mohammed, terrorism, terrorist, terrorists, terror camps, terror states, war against terror, war on terror, weapons of terror</i>

Since September 11, 2001, terrorism has been mentioned in every State of the Union address across 3 different Presidential administrations. The analysis revealed
that President Bush spoke about terrorism the greatest number of times in his speeches. In terms of a historical context he was the President immediately following the horrific al-Qaeda attacks on America.  

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_terrorism_metrics.png">
</p>

The topic <i>Weapons of Mass destruction (WMD)</i> was mentioned in 16 of the 17 State of the Union addresses analyzed. President Bush's 2003 speech 
referenced WMD 29 times and terrorism 28 times. It is worth noting that this speech was used by President Bush to declare his intentions to launch offensive military operations on Iraq for the express purpose of locating the WMDs allegedly being hidden by Saddam Hussein. Bush's 2003 State of the Union address was on January 28, 2003 and the invasion of Iraq commenced on March 19, 2003.


<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_wmd_metrics.png">
</p>

<p align="justify">

Healthcare issues was a talking point in every State of the Union address within the corpus, which covers 17 years and 3 different administrations. Some of the healthcare keywords measured included <i>affordable care act, cancer research, generic drugs, health insurance, high drug prices, Medicaid, Medicare and terminal illnesses</i>. 

President Bush mentioned healthcare issues an average of 12.6 times accross his 7 State of the Union addresses. President Obama's average was 10 mentions in his 7 addresses and President Trump's average was almost 10 times per his 3 speeches. 

President Bush mentioned healthcare issues a total of 88 times across his 7 speeches. His 2004 address mentioned healthcare 23 times, which was the highest number any address accross the 3 Presidential administrations analyzed. His 2007 State of the Union address mentioned healthcare 21 times, which was the second highest for the same period.

President Obama mentioned healthcare issues 70 times in his 7 speeches. He mentioned healthcare issues 15 times in his 2010 address, which was the highest within his corpus. It is worth noting that Congress passed the Patient Protection and Affordable Care Act (also know as Obamacare) in March 2010. 
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_healthcare_metrics.png">
</p>

<p align="justify">
Global environmental issues have also been a major talking point in State of the Union addresses within the corpus. Some of the environmental keywords measured included <i>clean water, climate change, energy efficient, fossil fuels, hybrid vehicles, ocean temperatures and wind energy.</i>. The environmental buzzword that occurred the most was climate change. This keyword was only mentioned 17 times accross 3 Presidential administrations with President Obama mentioning this phrase 15 times.

All of President Obama's State of the Union addresses mentioned the bigram <i>climate change</i>. His 2013 speech mentioned environmental issues 18 times, which was the highest number of references spanning 3 Presidential administrations and 17 State of the Union addresses.  President Obama's 2013 address came on the heels of the 2012 United Nations Climate Change Conference. His 2010 speech contained the second highest number of environmental keywords. This speech came weeks after the 2010 United Nations Climate Change Conference. Additional research would be required to determine if these Climate Change Conferences influenced President Obama's addresses in 2010 and 2013. President Obama mentioned environmental issues 80 times across 7 speeches.

President Bush's 2007 State of the Union address mentioned that new technologies would be needed to diversify America's energy supply. The context around this section of his speech was related to high gas prices and America's reliance on foreign oil from the Middle East. He also talked about diversify America's energy supply in his 2008 speech.  President Bush briefly touched on climate change in both speeches, but context of these references were linked to diversifying America's energy supply for national security reasons and not for the health of the world.
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_environmental_metrics.png">
</p>

<p align="justify">
Religion references were also analyzed in the State of the Union addresses with the corpus. The keywords measured included <i>bible, christian, church, god, holiness, holy land, islam, jerusalem, and judaism</>. The Republican Presidents Bush and Trump used religious references more frequently than President Obama, a Democratic president. 
</p>
  
<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_religious_metrics.png">
</p>

<p align="justify">
Another topic analyzed within the corpuses was political parties. The keywords measured included <i>bipartisan, democrat(s), democratic party, republican(s), and republican party</i>. President Obama a democrat mentioned the republican party more frequently in his speeches than his republican counterparts Presidents Bush and Trump.  President Obama also used all these political keywords more frequently in his speeches. President Bush used these keywords the least frequently in his speeches.
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_political_parties_metrics.png">
</p>

<p align="justify">
The frequency of superlatives usage by a President was also measured. A superlative is an exaggerated or hyperbolical expression.  These words can be used to describe an object at the highest (e.g., wealthiest) or lowest limit (e.g., poorest).  Some of the superlative used by Presidents included <i>most beautiful, bravest, hottest, safest, smartest and toughest</i>. President Trump used superlatives the most and President Bush them the least. President Trump's 2019 address used superlatives nearly 20 times. 
</p>

<p align="center"><br>
<img src="https://github.com/johnbumgarner/sotu_nlp_experiments/blob/master/sotu_charts/sotu_superlative_metrics.png">
</p>

### Notes:

_The code within this repository is **not** production ready. It was **strictly** designed for experimental testing purposes only._
