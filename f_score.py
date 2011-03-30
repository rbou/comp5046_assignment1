f = open('ppl-0.csv', 'rU') 

person_categories = {}
my_choice = {}
all_categories = set()

for line in f.readlines():
	person, category, annotator = line.split(',')
	if category not in all_categories:
		all_categories.add(category)
	annotator = annotator.strip()
	if annotator == 'rima.B':
		my_choice[person] = category
	if person not in person_categories:
		person_categories[person] = []
	person_categories[person].append(category)

actual = {}

for person, votes in person_categories.items():
	vote_counts = {}

	for key in votes:
		if key not in vote_counts:
			vote_counts[key] = 0
		vote_counts[key] += 1

	max_value = 0
	for k,v in vote_counts.items():
		if v > max_value:
			max_value = v
			max_key = k

	actual[person] = max_key
	
actual_flipped = {}
for person, category in actual.items():
	if category not in actual_flipped:
		actual_flipped[category] = []
	actual_flipped[category].append(person)


my_flipped = {}
for person, category in my_choice.items():
	if category not in my_flipped:
		my_flipped[category] = []
	my_flipped[category].append(person)

f_score = {}
weight = {}

for category in all_categories:
	if category not in actual_flipped and category not in my_flipped:
		f_score[category] = 1
		weight[category] = 0
		continue
	if category not in actual_flipped or category not in my_flipped:
		f_score[category] = 0
		if category not in actual_flipped:
			weight[category] = 0
		else:
			weight[category] = float(len(actual_flipped[category]))
		continue

	actual = float(len(actual_flipped[category]))
	weight[category] = float(len(actual_flipped[category]))

	correct = float(0)
	for person in my_flipped[category]:
		if person in actual_flipped[category]:
			correct += 1
	total_returned = float(len(my_flipped[category])) 

	precision = correct/total_returned
	recall = correct/actual
	f_score[category] = 2.0*((precision * recall)/(precision + recall))

print f_score 

num = 0.0
for category, f in f_score.items():
	w = weight[category]
	num += w*f

den = 0.0
for w in weight.values():
	den += w

weighted_mean = num/den

print weighted_mean
