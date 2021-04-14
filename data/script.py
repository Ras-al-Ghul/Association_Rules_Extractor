import csv

def getTime(row):
    #print(row[1].split(':'))
    hour = int(row[1].split(':')[0])
    if hour > 0 and hour <= 6:
        return "early_morning"
    if hour > 6 and hour <= 12:
        return "morning"
    if hour > 12 and hour <= 16:
        return "afternoon"
    if hour > 16 and hour <= 19:
        return "evening"
    if hour > 18 and hour <= 24:
        return "night"

def getPersonInjuredOrKilled(row):
    data = []

    if int(row[12]) > 0:
        data.append('pedestrain_injured')
    if int(row[13]) > 0:
        data.append('pedestrain_killed')
    if int(row[14]) > 0:
        data.append('cyclist_injured')
    if int(row[15]):
        data.append('cyclist_killed')
    if int(row[16]) > 0:
        data.append('motorist_injured')
    if int(row[17]):
        data.append('motorist_killed')

    if len(data) == 0:
        data.append('no_injuries_or_deaths')
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

def getVehicles(row):
    data = set()
    if row[24] != '':
        vehicles = row[24].strip().lower().replace(' ', '_')
        data = data.union(set(vehicles.split('/')))

    if row[25] != '':
        vehicles = row[25].strip().lower().replace(' ', '_')
        data = data.union(set(vehicles.split('/')))

    return list(data)

with open('Motor_Vehicle_Collisions_-_Crashes.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    next(datareader)
    filtered_data = []
    for row in datareader:
        data = []

        data.append(getTime(row))

        data.extend(getPersonInjuredOrKilled(row))

        reason = getReason(row)
        if reason is not None:
            data.append(reason)

        data.extend(getVehicles(row))

        filtered_data.append(data)

        #print(data)


with open('INTEGRATED_DATASET.csv',  mode='w') as csvfile:
    employee_writer = csv.writer(csvfile, delimiter=',')

    for row in filtered_data:
        employee_writer.writerow(row)

    #employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

