import pandas as pd
from collections import defaultdict
import itertools
from itertools import chain, combinations
import csv


def get_large_one_itemset(data, support):
    item_sets = defaultdict(int)
    counted = {}
    for i, row in enumerate(data):
        for item in list(row):
            # Iterating through every entry in dataframe
            # print(item)
            if item not in counted:
                item_sets[item] += 1
                counted[item] = [i]
            elif i not in counted[item]:
                item_sets[item] += 1
                counted[item].append(i)

        if i%10000 == 0:
            print(i)

    row_count = len(data)
    large_itemset = {}
    for item, freq in item_sets.items():
        if freq / row_count >= support and item != None:
            # print(item)
            large_itemset[(item,)] = freq / row_count

    return set(large_itemset.keys()), large_itemset


def subsets(iterable):
    # Code to generate subsets of a list in python
    # Original reference - https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
    # We have modified it to generate combinations of size k-1 only
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) - 1, len(s))))


def apriori_gen(prev_item_set):
    # Algorithm from paper
    # Join step detailed in paper
    # insert into C_k
    # select p.item_1, p.item2, .. , q.item_k-1
    # from L_k-1 p , L_k-1 q
    # where p.item_1 = q.item_1, ... , p.item_k_2 = q.item_k_2 , p.item_k-1 < q.item_k-1
    C_k = []

    for p in prev_item_set:
        for q in prev_item_set:
            if (p[:-1] == q[:-1]) and (p[-1] != q[-1]):
                if p[-1] > q[-1]:
                    C_k.append(q + (p[-1],))
                else:
                    C_k.append(p + (q[-1],))

    C_k = list(set(C_k))

    # print('C_k - ', C_k)

    # Algorithm from paper
    # prune
    # for all itemsets c in C_k
    # for all (k-1) subsets s of c do
    # if s not in l_k-1 then
    # delete c from C_k

    C_k_new = []
    for c in C_k:
        prune = False
        for subset in subsets(c):
            # print(subset)
            if subset not in prev_item_set:
                # print(subset)
                prune = True

        if prune == False:
            C_k_new.append(c)

    # print('New C_k - ', C_k_new)

    return C_k_new


def get_support(candidate, data):
    # Algorithm from paper
    # for all transactions t in D
    # C_t = subset(C_k, t)
    # for all candidates c in C_t do
    # c.count++
    count = 0
    for i, itemset in data.iterrows():
        flag = 0
        for item in candidate:
            if item not in list(itemset):
                flag = 1
                break
        if flag == 0:
            count += 1

    return count / len(data)


def get_confidence(rule, support_dict):
    # print('Rule - ',rule)
    confidence = support_dict[tuple(sorted(rule))] / support_dict[tuple(sorted(rule[:-1], ))]
    # print('Confidence - ', confidence)
    return confidence


def get_association_rules(frequent_itemsets, support_dict, min_conf):
    rules = []
    for itemset in frequent_itemsets:
        if len(itemset) > 1:
            candidate_rules = list(itertools.permutations(itemset))
            for rule in candidate_rules:
                if get_confidence(rule, support_dict) >= min_conf:
                    rules.append(rule)
    return rules


def main(data, support, confidence):
    # Algorithm 2.2.1 from the paper
    # L1 = {large 1-itemsets}
    # for (k=2; L_k-1 != inf; k++) do begin
    #     C_k = apriori-gen(Lk_1); //new candidates
    #     for all transactions t < D do begin
    #         C_t = subset(C_k,t); //Candidates contained in t
    #         forall candidates c in C_t do
    #             c.count++;
    #     end
    #     L_k = {c < C_k | c.count >= minsup}
    # end
    # answer = U_k l_K

    answer = set()
    l_k, support_dict = get_large_one_itemset(data, support)
    print('Itemsets for k = 1 - ', l_k)
    for item in l_k:
        answer.add(item)
    # print(l_k)
    l_k_plus_1 = l_k
    k = 2
    while len(l_k_plus_1) > 0:
        l_k_plus_1 = set()
        c_k = apriori_gen(l_k)
        for candidate in c_k:
            count = get_support(candidate, data)
            if count >= support:
                l_k_plus_1.add(candidate)
                support_dict[tuple(sorted(candidate))] = count
        print('Itemsets for k = {} - {}'.format(k, l_k_plus_1))
        for item in l_k_plus_1:
            answer.add(item)
        l_k = l_k_plus_1
        k += 1
    return answer, support_dict


if __name__ == '__main__':

    support = 0.7
    confidence = 0.7
    # data = pd.read_csv(r"C:\Users\nidhe\Documents\Columbia\2021_Spring\AdvanceDatabases\Project3\Association_Rules_Extractor\data\INTEGRATED_DATASET.csv", header=None)
    with open(
            r"C:\Users\nidhe\Documents\Columbia\2021_Spring\AdvanceDatabases\Project3\Association_Rules_Extractor\data\INTEGRATED_DATASET.csv",
            newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        next(datareader)

        data = []
        for row in datareader:
            data.append(row)

    answer, support_dict = main(data, support, confidence)
    print('Final large itemsets - ', answer)
    rules = get_association_rules(answer, support_dict, confidence)
    print('Association Rules - ', rules)

    support_dict_sorted = dict(sorted(support_dict.items(), key=lambda x: x[1], reverse=True))
    rules_sorted = sorted(rules, key=lambda item: get_confidence(item, support_dict), reverse=True)

    with open("output.txt", "w") as f:
        f.write("==Frequent itemsets (min_sup={})\n".format(support))
        for key, value in support_dict_sorted.items():
            f.write("{}, {}%".format(list(key), value * 100))
            f.write("\n")
        f.write("\n")
        f.write("==High-Confidence Association Rules (min_conf={})\n".format(confidence))
        for item in rules_sorted:
            f.write("{}=>{}, (Conf: {}%, Supp: {}%)".format(list(item[:-1]), [item[-1]],
                                                            get_confidence(item, support_dict) * 100,
                                                            support_dict[tuple(sorted(item))] * 100))
            f.write("\n")
        f.close()