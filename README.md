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
1. Columns chosen along with the processing done: 
- Time at which the crash occured: bin the CRASH TIME column into early-morning (4<=hour<=6), morning (7<=hour<=11), afternoon(12<=hour<=15) and night(19<=hour<=3), where hour is the hour in which accident occured. hour is the hour picked as interger after splitting the CRASH TIME with ':'
- Borough: Picked from BOROUGH column. the string is stripped, converted to lower characters, all ' ','/' are replaced with '_'. if column is empty nothing is added to the row.
- Zipcode: Picked from ZIP CODE column. If column is empty nothing is added to the row.
- pedestrains injured: Picked up from NUMBER OF PEDESTRIANS INJURED column. 'pedestrain_injured' is added to the row if the column value is > 0.
- pedestrains killed
- cyclist injured
- cyclist killed
- motorcyclist injured
- motorcyclist killed
- reason
- kind of vehicles


## Algorithm


