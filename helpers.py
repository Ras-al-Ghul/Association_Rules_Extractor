
import csv

def load_csv():
	with open(r"C:\Users\nidhe\Documents\Columbia\2021_Spring\AdvanceDatabases\Project3\Association_Rules_Extractor\data\INTEGRATED_DATASET.csv", newline='') as csvfile:
		datareader = csv.reader(csvfile, delimiter=',')
		next(datareader)

		data = []
		for row in datareader:
			data.append(set(row))
		return data

def print_itemsets(frequent_itemsets, support):
	pass


def print_rules(rules):
	pass


#load_csv()