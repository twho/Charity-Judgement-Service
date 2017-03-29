# deal with all kinds of file reading in the project
import csv

specified_type = ["Homeless Services", "Community Development", "Human Services"]

class file_reader():
	data_res_path = ''

	def __init__(self, data_res_path):
		self.data_res_path = data_res_path

	def read_charity_csv_file(self, file_path):
		data_row = []

		with open(self.data_res_path + file_path, 'rb') as csvfile:
			read_csv_file = csv.reader(csvfile, delimiter=',')

			for row in read_csv_file:
				data_row.append([str(row[3]), str(row[8]), str(row[9]), str(row[10])])

		return data_row

	def read_mission_csv_file(self, file_path):
		data_row = []

		with open(self.data_res_path + file_path, 'rb') as csvfile:
			read_csv_file = csv.reader(csvfile, delimiter=',')

			for row in read_csv_file:
				data_row.append([str(row[0]), str(row[1]), str(row[2])])

		return data_row

	def read_random_sample_id(self, file_path):
		key_list = []
		with open(self.data_res_path + file_path, 'rb') as csvfile:
			read_csv_file = csv.reader(csvfile, delimiter=',')

			for index, row in enumerate(read_csv_file):
				if index > 0:
					key_list.append(str(row[0]).split(".")[0])

		return key_list

	def read_filtered_homeless_data(self, data_set):
		data_row = {}

		for key in data_set.keys():
			data_arr = data_set[key]
			print(data_arr)
			if any(charity_type in data_arr[1] for charity_type in specified_type):
				data_row[data_arr[0]] = [data_arr[0], data_arr[1], data_arr[4], data_arr[5]]

		return data_row 
