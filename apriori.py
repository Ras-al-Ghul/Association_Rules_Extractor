
def select_rules(frequent_itemsets, supports, min_conf):
	assoc_rules = []
	for i in frequent_itemsets:
		# atleast two items
		if len(i) >= 2:
			# create rules by excluding one element and creating subsets
			subs = [(i.difference([ii]), set([ii])) for ii in i]
			for (left, right) in subs:
				support = supports[i]
				# supports[left] will necessarily be present
				confidence = support/supports[left]
				if confidence >= min_conf:
					assoc_rules.append((left, right, confidence, support))
	return assoc_rules


def get_candidates(itemset, L_k):
	# frozensets can be used as keys as they're immutable
	# hence return list of frozensets
	
	if L_k == [frozenset()]:
		# length one candidates
		return [frozenset([item]) for item in itemset]

	# join step of the apriori algorithm
	candidates = set()
	for a in L_k:
		for b in L_k:
			for elem in b:
				new_b = b.difference(set([elem]))
				if new_b.issubset(a):
					temp = frozenset(a.union(set([elem])))
					if temp not in candidates:
						candidates.add(temp)

	dup_candidates = set(candidates)
	# prune step of the apriori algorithm
	for c in dup_candidates:
		subsets = [c.difference([elem]) for elem in c]
		for s in subsets:
			if s not in L_k:
				candidates.remove(c)
				break

	return list(candidates)


def get_supports(data, candidates):
	# get the counts of occurrence of candidates in data
	candidates_freqs = {k:0 for k in candidates}
	for item in data:
		for idx, c in enumerate(candidates):
			if c.issubset(item):
				candidates_freqs[c] += 1

	# divide by total number of items to get supports
	supports = {c:(candidates_freqs[c]/len(data)) for c in candidates}
	return supports


def get_itemsets(data, min_sup):
	# Apriori algorithm from the paper 
	# "Fast Algorithms for Mining Association Rules, Agrawal and Srikant VLDB '94"

	itemset = set().union(*data)
	# initialize
	frequent_itemsets = set()
	# keys are candidate sets, values are supports
	supports = dict()
	L_k = [frozenset()]

	# until it is impossible to generate any more candidates of len(candidates)+1
	while len(L_k) != 0:

		candidates = get_candidates(itemset, L_k)

		candidates_support = get_supports(data, candidates)

		L_k = [c for c in candidates if candidates_support[c] >= min_sup]
		# update frequent_itemsets
		frequent_itemsets = frequent_itemsets.union(L_k)

		set_L_k = set(L_k)
		# update supports dict
		supports.update({k:v for k, v in candidates_support.items() if k in set_L_k})

	return frequent_itemsets, supports


