# deal with all kinds of file reading in the project
import csv

class file_reader():
	data_res_path = ''

	def __init__(self, data_res_path):
		self.data_res_path = data_res_path

	def read_charity_csv_file(self, file_path):
		data_row = []

		with open(self.data_res_path + file_path, 'rb') as csvfile:
			read_csv_file = csv.reader(csvfile, delimiter=',')

			for row in read_csv_file:
				data_row.append([row[3], row[8], row[9], row[10]])

		return data_row

	def read_mission_csv_file(self, file_path):
		data_row = []

		with open(self.data_res_path + file_path, 'rb') as csvfile:
			read_csv_file = csv.reader(csvfile, delimiter=',')

			for row in read_csv_file:
				data_row.append([row[0], row[2]])

		return data_row
