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

all_categories = list(all_categories)
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
		

dimensions = len(all_categories)

matrix = [[0 for _ in range(dimensions)] for _ in range(dimensions)]

matrix = []
for _ in range(dimensions):
	row = []
	for _ in range(dimensions):
		row.append(0)
	matrix.append(row)

for person in my_choice:
	row = all_categories.index(actual[person])
	col = all_categories.index(my_choice[person])
	matrix[row][col] += 1

print ',',
for category in all_categories:
	print category + ',',
print

for i, row in enumerate(matrix):
	print all_categories[i] + ',',
	for column in row:
		print str(column) + ',',
	print 
	
