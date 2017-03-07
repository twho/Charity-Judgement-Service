from firebase_manager import *
from file_reader import *
from file_writer import *

# set firebase login account
# currently use testing account
account = 'tsungwei50521@gmail.com'
password = '801020'

# set data resources directory
directory = '../data_resources/'
charity_org_path = 'charity_org_characters.csv'
mission_stmt = 'mission_statements_raw.csv'

# fieldnames
fieldnames = ["id", "type", "url", "domain", "name", "mission_statement"]

# init
m_firebase_manger = firebase_manager(account, password)
m_file_reader = file_reader(directory)
m_file_writer = file_writer(directory, fieldnames)

# all available data set
data_row_2 = m_file_reader.read_mission_csv_file(mission_stmt)
data_row_1 = m_file_reader.read_charity_csv_file(charity_org_path)
combined_set = m_file_writer.combine_data_set(data_row_1, data_row_2)

# write data to csv
# m_file_writer.write_data_to_csv(combined_set)

fieldnames_include_rater = fieldnames
fieldnames_include_rater.append('rater')
m_file_writer = file_writer(directory, fieldnames_include_rater)
random_data_set = m_file_writer.get_random_n_data_as_csv(200, combined_set)
m_firebase_manger.save_data_row_to_firebase(random_data_set, fieldnames_include_rater)