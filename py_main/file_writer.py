import csv
from random import randint
from itertools import repeat

class file_writer():
	data_res_path = ''
	fieldnames = []

	def __init__(self, data_res_path, fieldnames):
		self.data_res_path = data_res_path
		self.fieldnames = fieldnames

	# row_params of data_set_1: ['id', 'type', 'url', 'domain']
	# row_params of data_set_2: ['id', 'name', 'mission_statement']
	def combine_data_set(self, data_set_1, data_set_2):
		combined_set = {}
		for row in data_set_1:
			combined_set[row[0]] = [row[0], row[1], row[2], row[3]]

		for row in data_set_2:
			if row[0] in combined_set.keys():
				combined_set[row[0]].append(row[1])
				combined_set[row[0]].append(row[2])

		for key in combined_set.keys():
			if len(combined_set[key]) < 6:
				combined_set.pop(key, None)
				
		return combined_set

	# column: ['id', 'type', 'url', 'domain', 'name', 'mission_statement']
	def write_data_to_csv(self, data_set):
		 with open(self.data_res_path + 'combined_charity_data_set.csv', 'w') as csvfile:
		 	writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
		 	writer.writeheader()
		 	for row in data_set.values():
		 		if len(row) >= 6:
		 			writer.writerow({self.fieldnames[0]: str(row[0]), self.fieldnames[1]: str(row[1]), self.fieldnames[2]: str(row[2]), self.fieldnames[3]: str(row[3]), self.fieldnames[4]: str(row[4]), self.fieldnames[5]: str(row[5])})

	def get_random_n_data_as_csv(self, n, data_set):
		with open(self.data_res_path + 'mt_charity_random_' + str(n) + ' _data_set.csv', 'w') as csvfile:
		 	writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
		 	writer.writeheader()
		 	random_set = []
		 	for time in repeat(None, n):
		 		row = data_set.values()[randint(0, len(data_set.keys()))]
		 		# row.extend(str("n"))
		 		# random_set.append(row)
		 		# writer.writerow({self.fieldnames[0]: str(row[0]), self.fieldnames[1]: str(row[1]), self.fieldnames[2]: str(row[2]), self.fieldnames[3]: str(row[3]), self.fieldnames[4]: str(row[4]), self.fieldnames[5]: str(row[5]), self.fieldnames[6]: str("n")})
		 		writer.writerow({self.fieldnames[0]: str(row[0]), self.fieldnames[1]: str(row[1]), self.fieldnames[2]: str(row[2]), self.fieldnames[3]: str(row[3])})
		 		data_set.pop(row[0])

		 	return random_set
