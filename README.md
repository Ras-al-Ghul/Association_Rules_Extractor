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

## Initial processing of data to generate INTEGRATED_DATASET.csv:
1. Columns chosen: 
- Time at which the crash occured
- Borough
- Zipcode
- pedestrains injured
- pedestrains killed
- cyclist injured
- cyclist killed
- motorcyclist injured
- motorcyclist killed
- reason
- kind of vehicles


## Algorithm


