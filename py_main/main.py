from firebase_manager import *
from file_reader import *

# set firebase login account
# currently use testing account
account = 'tsungwei50521@gmail.com'
password = '801020'

# set data resources directory
directory = '../data_resources/'
charity_org_path = 'charity_org_characters.csv'
mission_stmt = 'mission_statements_raw.csv'

m_firebase_manger = firebase_manager(account, password)
m_file_reader = file_reader(directory)

def uplaod_mission_stmt_to_firebase():
	# read data locally
	data_row_1 = m_file_reader.read_charity_csv_file(charity_org_path)
	row_params = ['id', 'mission_statement']
	# upload data to firebase
	m_firebase_manger.save_data_row_to_firebase(data_row_1, row_params)

def uplaod_charity_to_firebase():
	# read data locally
	m_file_reader = file_reader(directory)
	data_row_2 = m_file_reader.read_mission_csv_file(mission_stmt)
	row_params = ['id', 'type', 'url', 'domain']
	# upload data to firebase
	m_firebase_manger.save_data_row_to_firebase(data_row_2, row_params)