import csv

def getTime(row):
    #print(row[1].split(':'))
    hour = int(row[1].split(':')[0])
    if hour >= 4 and hour <= 6:
        return "early_morning"
    if hour >= 7 and hour <= 11:
        return "morning"
    if hour >= 12 and hour <= 15:
        return "afternoon"
    if hour >= 16 and hour <= 19:
        return "evening"
    if hour >= 20 and hour <= 23 or hour >= 0 and hour <= 3:
        return "night"

def getPersonInjuredOrKilled(row):
    data = []

    # if int(row[12]) > 0:
    #     data.append('pedestrain_injured')
    # if int(row[13]) > 0:
    #     data.append('pedestrain_killed')
    # if int(row[14]) > 0:
    #     data.append('cyclist_injured')
    # if int(row[15]):
    #     data.append('cyclist_killed')
    # if int(row[16]) > 0:
    #     data.append('motorist_injured')
    # if int(row[17]):
    #     data.append('motorist_killed')

    if int(row[10])>0: #or int(row[14])>0 or int(row[16])>0:
        data.append('person_injured')
    # else:
    #     data.append('no_injuries')

    if int(row[11])>0:# or int(row[15])>0 or int(row[17])>0:
        data.append('person_killed')
    # else:
    #     data.append('no_deaths')

    # if len(data) == 0:
    #     data.append('no_injuries_or_deaths')
    return data

def getReason(row):
    row[18] = row[18].strip()
    row[19] = row[19].strip()
    if row[18] != 'Unspecified' and row[18] != '':
        return row[18].strip().lower().replace(' ', '_').replace('/', '_')
    elif row[19] != 'Unspecified' and row[19] != '':
        return row[19].strip().lower().replace(' ', '_').replace('/', '_')
    else:
        return None

def getBorough(row):
    row[2] = row[2].strip()
    if row[2] != '':
        return row[2].strip().lower().replace(' ', '_').replace('/', '_')
    else:
        return None

def getZip(row):
    row[3] = row[3].strip()
    if row[3] != '':
        return row[3].strip()
    else:
        return None

def getVehicles(row):
    data = set()
    if row[24] != '':
        data.add(row[24].strip().lower().replace(' ', '_').replace('/', '_'))


    if row[25] != '':
        data.add(row[25].strip().lower().replace(' ', '_').replace('/', '_'))
        # vehicles = row[25].strip().lower().replace(' ', '_')
        # data = data.union(set(vehicles.split('/')))

    return list(data)

def isRecentData(row):
    year = int(row[0].split('/')[2])
    return year >= 2018

with open('Motor_Vehicle_Collisions_-_Crashes.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    next(datareader)
    filtered_data = []
    for row in datareader:
        if isRecentData(row):
            data = []

            data.append(getTime(row))

            b = getBorough(row)
            if b is not None:
                data.append(b)

            zip = getZip(row)
            if zip is not None:
                data.append(zip)

            data.extend(getPersonInjuredOrKilled(row))

            reason = getReason(row)
            if reason is not None:
                data.append(reason)

            data.extend(getVehicles(row))

            filtered_data.append(data)

            #print(data)


with open('INTEGRATED_DATASET.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    writer.writerows(filtered_data)

    #employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

