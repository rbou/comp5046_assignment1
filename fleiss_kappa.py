f = open('ppl-0.csv', 'rU') 
lines = f.readlines()

total_annotations = float(len(lines))

annotators = set()
category_counts = {}
person_categories = {}

for line in lines:
	person, category, annotator = line.split(',')
	annotator = annotator.strip()

	annotators.add(annotator)

	if category not in category_counts:
		category_counts[category] = 0.0
	category_counts[category] += 1.0

	if person not in person_categories:
		person_categories[person] = {}
	if category not in person_categories[person]:
		person_categories[person][category] = 0.0
	person_categories[person][category] += 1.0
	
total_subjects = float(len(person_categories))
total_annotators = float(len(annotators))

p = {}
for category, count in category_counts.items():
	p[category] = count/total_annotations

p_e_mean = 0.0
for p_e in p.values():
	p_e_mean += p_e**2

P = {}
for person in person_categories:
	sum_squares = 0.0
	for count in person_categories[person].values():
		sum_squares += count**2
	P[person] = (1.0/(total_annotators*(total_annotators-1))) * (sum_squares - total_annotators)

P_mean = 0.0
for P_i in P.values():
	P_mean += P_i/total_subjects

k = (P_mean - p_e_mean) / (1 - p_e_mean)
print k
