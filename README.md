# Project done by
Dipankar Niranjan dn2502, Nidheesha Amedapu nra2125
# Association_Rules_Extractor
Code to extract Association Rules from a dataset using the Apriori algorithm

## Files
<ol>
<li>data
  <ul>
    <li>INTEGRATED_DATASET.csv</li>
    <li>script.py</li>
  </ul>
</li>
<li>__init__.py</li>
<li>__main__.py</li>
<li>apriori.py</li>
<li>helper.py</li>
<li>README.md</li>
<li>requirements.txt</li>
</ol>

## Steps to install and run

<p>Install the rquirements from requirements.txt using the below command.</p>

```
 pip3 install -r requirements.txt
```

<p>Run the program using the following command.</p>

```
python3 -m Association_Rules_Extractor <support> <confidence>
```
<p>Where query is a string of words that you want to search and precision is a decimal value. For example,</p>

```
python3 -m Association_Rules_Extractor 0.6 0.6
```

## Dataset used:
NYPD Motor Vehicle Collisions Summary:
https://data.cityofnewyork.us/NYC-BigApps/NYPD-Motor-Vehicle-Collisions-Summary/m666-sf2m

## Design

<ol>
<li>search_scrape.py :
   <ul>
    <li>Sends a google query.</li> 
    <li>Extracts the summary, title and contents of the query results.</li>
    <li>Gets user feed back on the document relevance.</li>
    <li>Helpers to process text - lower case, eliminate punctuations, etc. </li>
   </ul>
</li>
<li>indexer.py
  <ul>
    <li>Extracts the vocabulary</li>
    <li>Gets list of stop words from stop_words.txt</li>
    <li>Builds tfidf of the summary, title and content using TfidfVectorizer from scikit-learn.</li>
  </ul>
</li>
<li>rocchio.py
  <ul>
    <li>Uses the tfidf and bigram data and suggests the best words for query expansion</li>
  </ul>
</li>
</ol>

## Algorithm


