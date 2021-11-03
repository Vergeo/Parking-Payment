import json

class Settings :
	def __init__(self) :

		# Window Config
		self.title = "Good Parking"
		base = 60
		ratio = (16,9)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width+10}x{self.height+20}+{(1366-self.width-10)//2}+{(768-self.height-20)//2}"

		# Path
		self.logo_path = "image/logo.png"
		self.small_logo_path = "image/logo_small.png"
		self.i_username_path = "image/i_username.png"
		self.i_password_path = "image/i_password.png"
		self.i_quit_path = "image/i_quit.png"
		self.i_search_path = "image/i_search2.png"

		self.user_path = "data/users.json"
		self.vehicle_path = "data/vehicles.json"

	def load_data(self, path) :
		with open(path, "r") as json_data :
			data = json.load(json_data)
		return data

	def login(self, username, password) :
		users = self.load_data(self.user_path)
		if username in  users :
			if password == users[username]["password"] :
				return True
		else :
			return False

	def save_data(self, item, path) :
		with open(path, "w") as json_data :
			json.dump(item, json_data)


# [{
# 	"BG 1 A" : {
# 		"vehicle_type" : "Car",
# 		"vehicle_brand" : "Toyota",
# 		"time_enter" : "16:38:18 Wed 19 May 2021",
# 		"time_leave" : "17:40:53 Wed 19 May 2021",
# 		"duration" : "1 hour(s) 12 minute(s) 35 second(s)",
# 		"price" : "Rp 5.000,-"
# 		}
# 	},
# 	{
# 	"BG 2 B" : {
# 		"vehicle_type" : "11",
# 		"vehicle_brand" : "11",
# 		"time_enter" : "11",
# 		"time_leave" : "11",
# 		"duration" : "11",
# 		"price" : "11"
# 		}
# 	},
# 	{"BG 3 C" : {
# 		"vehicle_type" : "22",
# 		"vehicle_brand" : "22",
# 		"time_enter" : "22",
# 		"time_leave" : "22",
# 		"duration" : "22",
# 		"price" : "22"
# 		}
# 	},
# 	{"BG 4 D" : {
# 		"vehicle_type" : "33",
# 		"vehicle_brand" : "33",
# 		"time_enter" : "33",
# 		"time_leave" : "33",
# 		"duration" : "33",
# 		"price" : "33"
# 		}
# 	},
# 	{"BG 5 E" : {
# 		"vehicle_type" : "44",
# 		"vehicle_brand" : "44",
# 		"time_enter" : "44",
# 		"time_leave" : "44",
# 		"duration" : "44",
# 		"price" : "44"
# 		}
# 	},
# 	{
# 	"BG 2 B" : {
# 		"vehicle_type" : "11",
# 		"vehicle_brand" : "11",
# 		"time_enter" : "11",
# 		"time_leave" : "11",
# 		"duration" : "11",
# 		"price" : "11"
# 		}
# 	},
# 	{"BG 3 C" : {
# 		"vehicle_type" : "22",
# 		"vehicle_brand" : "22",
# 		"time_enter" : "22",
# 		"time_leave" : "22",
# 		"duration" : "22",
# 		"price" : "22"
# 		}
# 	},
# 	{"BG 4 D" : {
# 		"vehicle_type" : "33",
# 		"vehicle_brand" : "33",
# 		"time_enter" : "33",
# 		"time_leave" : "33",
# 		"duration" : "33",
# 		"price" : "33"
# 		}
# 	},
# 	{"BG 5 E" : {
# 		"vehicle_type" : "44",
# 		"vehicle_brand" : "44",
# 		"time_enter" : "44",
# 		"time_leave" : "44",
# 		"duration" : "44",
# 		"price" : "44"
# 		}
# 	},
# 	{
# 	"BG 2 B" : {
# 		"vehicle_type" : "11",
# 		"vehicle_brand" : "11",
# 		"time_enter" : "11",
# 		"time_leave" : "11",
# 		"duration" : "11",
# 		"price" : "11"
# 		}
# 	},
# 	{"BG 3 C" : {
# 		"vehicle_type" : "22",
# 		"vehicle_brand" : "22",
# 		"time_enter" : "22",
# 		"time_leave" : "22",
# 		"duration" : "22",
# 		"price" : "22"
# 		}
# 	},
# 	{"BG 4 D" : {
# 		"vehicle_type" : "33",
# 		"vehicle_brand" : "33",
# 		"time_enter" : "33",
# 		"time_leave" : "33",
# 		"duration" : "33",
# 		"price" : "33"
# 		}
# 	},
# 	{"BG 5 E" : {
# 		"vehicle_type" : "44",
# 		"vehicle_brand" : "44",
# 		"time_enter" : "44",
# 		"time_leave" : "44",
# 		"duration" : "44",
# 		"price" : "44"
# 		}
# 	},
# 	{
# 	"BG 2 B" : {
# 		"vehicle_type" : "11",
# 		"vehicle_brand" : "11",
# 		"time_enter" : "11",
# 		"time_leave" : "11",
# 		"duration" : "11",
# 		"price" : "11"
# 		}
# 	},
# 	{"BG 3 C" : {
# 		"vehicle_type" : "22",
# 		"vehicle_brand" : "22",
# 		"time_enter" : "22",
# 		"time_leave" : "22",
# 		"duration" : "22",
# 		"price" : "22"
# 		}
# 	},
# 	{"BG 4 D" : {
# 		"vehicle_type" : "33",
# 		"vehicle_brand" : "33",
# 		"time_enter" : "33",
# 		"time_leave" : "33",
# 		"duration" : "33",
# 		"price" : "33"
# 		}
# 	},
# 	{"BG 5 E" : {
# 		"vehicle_type" : "44",
# 		"vehicle_brand" : "44",
# 		"time_enter" : "44",
# 		"time_leave" : "44",
# 		"duration" : "44",
# 		"price" : "44"
# 		}
# 	}

# ]