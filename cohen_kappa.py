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
for category in all_categories:
	if category not in my_flipped:
		my_flipped[category] = []
	if category not in actual_flipped:
		actual_flipped[category] = []

agreed_count = 0.0
total_count = 0.0
for person in actual:
	total_count += 1
	if actual[person] == my_choice[person]:
		agreed_count += 1

pr_a = agreed_count/total_count

num_annotations = float(len(actual))
pr_e = 0.0
for category in all_categories:
	my_random = float(len(my_flipped[category]))/num_annotations
	actual_random = float(len(actual_flipped[category]))/num_annotations
	pr_e += my_random*actual_random

k = (pr_a-pr_e)/(1-pr_e)
print k
