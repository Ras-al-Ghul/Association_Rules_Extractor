
import csv, os

def load_csv():
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/INTEGRATED_DATASET2.csv'), newline='') as csvfile:
		datareader = csv.reader(csvfile, delimiter=',')
		next(datareader)

		data = []
		for row in datareader:
			data.append(set(row))
		return data


def print_itemsets(frequent_itemsets, support, min_sup):
	frequent_itemsets = sorted(frequent_itemsets, key=lambda x: support[x], reverse=True)
	print("==Frequent itemsets (min_sup={}%)".format(str(round(min_sup*100, 2))))
	for item in frequent_itemsets:
		print("{}, {}%".format(list(item), str(round(support[item]*100, 2))))


def print_rules(rules, min_conf):
	rules = sorted(rules, key=lambda x: x[2], reverse=True)
	print("==High-confidence association rules (min_conf={}%)".format(str(round(min_conf*100, 2))))
	for rule in rules:
		print("{} => {} (Conf: {}%, Supp: {}%)".format(
			list(rule[0]), list(rule[1]), str(round(rule[2]*100, 2)), str(round(rule[3]*100, 2))))
