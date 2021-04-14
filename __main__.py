import sys
import time

from . import helpers
from . import apriori

def main():
    
    if len(sys.argv) < 4:
        print('Usage: python3 -m Association_Rules_Extractor <dataset> <min_sup> <min_conf>')
        return

    dataset = sys.argv[1]
    min_sup, min_conf = float(sys.argv[2]), float(sys.argv[3])
    
    if min_sup < 0 or min_sup > 1 or min_conf < 0 or min_conf > 1:
        print('min_sup and min_conf must be floats in [0,1]')
        return

    # data = helpers.load_csv()
    # data is a list of sets

    frequent_itemsets, supports = apriori.get_itemsets(data, min_sup)
    helpers.print_itemsets(frequent_itemsets, supports)

    rules = apriori.select_rules(frequent_itemsets, supports, min_conf)
    helpers.print_rules(rules)


if __name__ == '__main__':
    main()