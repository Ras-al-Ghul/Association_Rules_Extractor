
import csv, os

def load_csv():
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/INTEGRATED_DATASET_SMALL.csv'), newline='') as csvfile:
		datareader = csv.reader(csvfile, delimiter=',')
		next(datareader)

		data = []
		for row in datareader:
			data.append(set(row))
		return data


def print_itemsets(frequent_itemsets, support):
	pass


def print_rules(rules):
	rules = sorted(rules, key=lambda x: x[2], reverse=True)
	print('ASSOCIATION RULES')
	for idx, rule in enumerate(rules):
		print("{}. {} => {} confidence: {} support: {}".format(
			idx, rule[0], rule[1], str(round(rule[2], 2)), str(round(rule[3], 2))))


#load_csv()