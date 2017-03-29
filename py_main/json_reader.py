import json

# json fieldnames
fieldnames = ["charities", "type", "url", "domain", "name", "mission_statement"]
options = ["homeless_related", "not_homeless_related"]
specify_type = ["Homeless Services", "Community Development", "Human Services"]

class json_reader():
	data_res_path = ''

	def __init__(self, data_res_path):
		self.data_res_path = data_res_path

	def check_json_file(self, file_name, key_list):
		except_dict = {}
		rev_except_dict = {}
		num_sum = 0
		with open(str(self.data_res_path + file_name)) as data_file:    
			data = json.load(data_file)
			for key in key_list:
				for x in data[fieldnames[0]][key]:
					for elem in data[fieldnames[0]][key][x]:
						cid = data[fieldnames[0]][key][x]["id"]
						char_type = data[fieldnames[0]][key][x]["type"]
						mission_statement = data[fieldnames[0]][key][x]["mission_statement"]
						if "MichaelHo" in data[fieldnames[0]][key][x][elem] and not data[fieldnames[0]][key][x][elem].__hash__:
							num_sum = num_sum + 1
							if data[fieldnames[0]][key][x][elem]["MichaelHo"] == options[0]:
								print(cid)
								if char_type not in except_dict.keys():
									except_dict[char_type] = 1
								else:
									except_dict[char_type] = except_dict[char_type] + 1

								# if specify_type[0] not in char_type and specify_type[1] not in char_type and specify_type[2] not in char_type:
									# print("Type: " + char_type)
									# print("Mission Statemnet: " + mission_statement)
							# else:
							# 	if char_type not in rev_except_dict.keys():
							# 		rev_except_dict[char_type] = 1
							# 	else:
							# 		rev_except_dict[char_type] = rev_except_dict[char_type] + 1
			print num_sum

			# for key in except_dict.keys():
			# 	print_str = str(key) + " / homeless: " + str(except_dict[key]) + " / non homeless: "
			# 	if key in rev_except_dict.keys():
			# 		print_str = print_str + str(rev_except_dict[key])
			# 	else:
			# 		print_str = print_str + "0"		

			# 	print print_str	

			# for key in rev_except_dict.keys():
			# 	print_str = str(key) + " / homeless: 0 / non homeless: "
			# 	if key not in except_dict.keys():
			# 		print_str = print_str + str(rev_except_dict[key])
			# 		print print_str	
