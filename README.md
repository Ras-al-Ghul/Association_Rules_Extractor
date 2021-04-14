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
<li>example-run.txt</li>
</ol>

## Steps to install and run

<p>There are no external modules required for this program. Run the program using the following command (from just outside the module directory). INTEGRATED_DATASET.csv could be replaced with any other data file placed in the "data/" dir.</p>

```
python3 -m Association_Rules_Extractor INTEGRATED_DATASET.csv <min_sup> <min_conf>
```
If you want to generate the INTEGRATED_DATASET.csv using script.py, please download the dataset below as a csv file, place it in "data/" directory and run the script.py

## Dataset used:
NYPD Motor Vehicle Collisions Summary:
https://data.cityofnewyork.us/NYC-BigApps/NYPD-Motor-Vehicle-Collisions-Summary/m666-sf2m

## Why is this dataset interesting?:
<p>This dataset has more than a million rows with NYC's motor vehicle collision data over the years (up until the current day). The dataset has the following columns (relevant columns are listed together):
</p>  
<ol>
<li> Crash Date and Time of the day</li>
<li> Borough and Zip Code</li>
<li> Latitude, Longitude, Location</li>
<li> On street name, Off street name, Cross street name</li>
<li> Number of persons injured, N persons killed, N {pedestrians, cyclist, motorist} {injured, killed} </li>
<li> Contributing factor vehicle {1,2,3,4,5} - Turning improperly, Following too closely, etc. </li>
<li> Collision ID </li>
<li> Vehicle type code {1,2,3,4,5} - ATV, bicycle, sedan, SUV, etc. </li>
</ol>
<p>It would be interesting to mine information about the frequent types of collisions, where they occur, at what time of the day they occur, common number of injuries/fatalities, the most frequent contributing factors, and the most common vehicle types involved in accidents.</p>

## Initial processing of data to generate INTEGRATED_DATASET.csv:
Some columns are too granular and would not yield meaningful information in this setting. Hence columns like Street names, number of cyclists, pedestrians, motorists who are injured, killed are omitted. Columns chosen along with the processing done are as follows:
- The data of <b>year>=2018</b> is considered to restrict the data to ~500k samples.
- <b>Time at which the crash occured:</b> We bin the CRASH TIME column into early-morning (4<=hour<=6), morning (7<=hour<=11), afternoon(12<=hour<=15) and night(19<=hour<=3), where hour is the hour in which accident occured. hour is the hour picked as integer after splitting the CRASH TIME with ':'
- <b>Borough:</b> Picked from BOROUGH column. the string is stripped, converted to lower characters, all ' ','/' are replaced with '_'. if column is empty nothing is added to the row.
- <b>Zipcode:</b> Picked from ZIP CODE column. If column is empty nothing is added to the row.
- <b>Injured:</b> Picked up from NUMBER OF PERSONS INJURED column. 'person_injured' is added to the row if the columns value is > 0.
- <b>Killed:</b> Picked up from NUMBER OF PERSONS KILLED column. 'person_killed' is added to the row if the column value is > 0.
- <b>Reason:</b> Picked up from CONTRIBUTING FACTOR VEHICLE 1 column. If CONTRIBUTING FACTOR VEHICLE 1 is 'Unspecified' or empty, value is picked up from CONTRIBUTING FACTOR VEHICLE 2. If CONTRIBUTING FACTOR VEHICLE 2 is also 'Unspecified' or empty, nothing is added to the row. The string value added to the row is stripped and the ' ' and '/' characters are replaced with '_'
- <b>Type of vehicles:</b> Picked up from VEHICLE TYPE CODE 1 and VEHICLE TYPE CODE 2. If both the columns are empty nothing is added to the row. The string values added to the row are stripped and ' ' and '/' are replaced with '_'. If vehicle names are 'station_wagon' or 'sport_utility_vehicle' or 'suv', the values are all set as 'suv' in the row.


## Algorithm
We use the Apriori algorithm mentioned in section 2.1 of the Agrawal et. al VLDB '94 paper. The candidate generation follows the algorithm mentioned in section 2.1.1. with the join and prune steps. We make use of Python frozensets as keys to store candidates and supports. The entire program and dataset fits into main memory and completes execution in around ~30 seconds of time for values of min_sup and min_conf that are not too small.

To scale it even further, one could use a sqlite database so that the entire dataset need not be stored in the main memory at once. However this comes at the cost of greater runtime. Another idea would be to use SHA hash representations of frozensets to further limit memory needs, however hashes are one way functions.  

One of the important parts of this project is to split the columns into reasonably sized granularity in order to extract meaningful associations. We tried and tested various splits for Time of the day, Injured and Killed person data, Street names and have chosen to stick with ones that seem to provide meaningful relations.

## Command line specification of a compelling run:

```
python3 -m Association_Rules_Extractor INTEGRATED_DATASET.csv 0.05 0.1
```
This would give a lot of data from which we could make conclusions.

## Conclusions from the above run:

## Conclusions from the above run:

Some interesting mined associations are:
<ol>
<li> ['following_too_closely'] => ['sedan'] (Conf: 67.42%, Supp: 6.08%) </li>
<li> ['night'] => ['sedan'] (Conf: 67.29%, Supp: 14.2%) </li>
<li> ['queens'] => ['sedan'] (Conf: 64.8%, Supp: 11.57%) </li>
<li> ['driver_inattention_distraction'] => ['sedan'] (Conf: 64.44%, Supp: 15.97%) </li>
<li> ['person_injured'] => ['sedan'] (Conf: 59.93%, Supp: 12.99%)</li>
<li> ['following_too_closely'] => ['suv'] (Conf: 59.41%, Supp: 5.35%)</li>
<li> ['queens'] => ['suv'] (Conf: 56.79%, Supp: 10.14%) </li>
<li> ['driver_inattention_distraction'] => ['suv'] (Conf: 53.34%, Supp: 13.22%) </li>
<li> ['evening'] => ['suv'] (Conf: 53.19%, Supp: 13.5%)</li>
<li> ['person_injured'] => ['suv'] (Conf: 46.89%, Supp: 10.17%) </li>
<li> ['sedan', 'driver_inattention_distraction'] => ['suv'] (Conf: 38.88%, Supp: 6.21%) </li>
</ol>

Overall, following too closely and driver inattention distraction are the most common reasons for crashes, while suvs and sedans are the most common vehicle types involved in crashes. Persons are more often injured than killed. Queens seems to be the borough with most accidents. And evenings and night times are the most common time of the day for accidents with motor vehicles.