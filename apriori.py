
def select_rules(frequent_itemsets, supports, min_conf):
	assoc_rules = []
	for i in frequent_itemsets:
		if len(i) > 1:
			subs = [(i.difference([ii]), set([ii])) for ii in i]
			for (left, right) in subs:
				support = supports[i]
				confidence = support/supports[left]
				if confidence >= min_conf:
					assoc_rules.append((left, right, confidence, support))


def get_candidates(itemset, L_k):
	if L_k == [set()]:
		return [set([item]) for item in itemset]

	candidates = []
	for a in L_k:
		for b in L_k:
			for elem in b:
				if not set(b).issubset(a):
					temp = set(b).union(a)
					if not temp in candidates:
						candidates.append(temp)

	for c in candidates:
		subsets = [c.difference([elem]) for elem in c]
		for s in subsets:
			if s not in L_k:
				candidates.remove(c)

	return candidates


def get_supports(data, candidates):
	keys = [frozenset(c) for c in candidates]
	candidates_support = {k:0 for k in keys}
	for idx, item in enumerate(data):
		for idx1, c in candidates:
			if c.issubset(item):
				candidates_support[keys[idx1]] += 1

	return {k:(candidates_support[k]/len(data)) for k in keys}


def get_itemsets(data, min_sup):

	itemset = set().union(*data)
	frequent_itemsets = set()
	supports = dict()
	L_k = [set()]

	sz = 0
	while len(L_k) != 0:
		sz += 1

		candidates = get_candidates(itemset, L_k)
		candidates = [frozenset(c) for c in candidates]

		candidates_support = get_supports(data, candidates)

		L_k = [c for c in candidates if candidates_support[c] >= min_sup]
		frequent_itemsets = frequent_itemsets.union(L_k)
		supports.update(candidates_support)

	return frequent_itemsets, supports


