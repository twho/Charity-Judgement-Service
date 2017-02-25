# Charity Information RA on Firebase
import pyrebase

config = {
	"apiKey": "AIzaSyCwHSRlrPwTh_fcUxen681wRAIAjfh5Xmc",
    "authDomain": "charity-database-4520a.firebaseapp.com",
    "databaseURL": "https://charity-database-4520a.firebaseio.com",
    "storageBucket": "charity-database-4520a.appspot.com",
    "messagingSenderId": "637988160509"
}

class firebase_manager():
	user = []
	auth = None
	firebase = None
	email = ''
	password = ''

	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.firebase = pyrebase.initialize_app(config)
		# Get a reference to the auth service
		self.auth = self.firebase.auth()
		# Log the user in
		self.user = self.auth.sign_in_with_email_and_password(self.email, self.password)

	def refresh_user_id_token(self):
		self.user = self.auth.refresh(self.user['refreshToken'])

	def save_data_row_to_firebase(self, dataset):
		# Pass the user's idToken to the push method
		db = self.firebase.database()
		self.refresh_user_id_token()

		# params for charity characters
		# row_params = ['id', 'type', 'url', 'domain']
		row_params = ['id', 'mission_statement']

		for data in dataset:
			org_id = data[0].split('.')[0]
			data_collection = {}
			for index, data_node in enumerate(data):
				data_collection[row_params[index]] = data_node
			results = db.child('charities').child(org_id).push(data_collection, self.user['idToken'])
