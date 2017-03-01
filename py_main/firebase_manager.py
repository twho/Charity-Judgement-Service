# Charity Information RA on Firebase
import pyrebase

config = {
	"apiKey": "AIzaSyDGFBbjnXFZ7WS9XWctDdVr8p0U9BuPsoU",
    "authDomain": "charity-sample-database.firebaseapp.com",
    "databaseURL": "https://charity-sample-database.firebaseio.com",
    "storageBucket": "charity-sample-database.appspot.com",
    "messagingSenderId": "347624664460"
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

	def save_data_row_to_firebase(self, dataset, row_params):
		# Pass the user's idToken to the push method
		db = self.firebase.database()
		self.refresh_user_id_token()

		for data in dataset:
			org_id = data[0].split('.')[0]
			data_collection = {}
			for index, data_node in enumerate(data):
				if index > 5:
					data_collection[row_params[index]] = "n"
				else:
					data_collection[row_params[index]] = data_node
			results = db.child('charities').child(org_id).push(data_collection, self.user['idToken'])
			