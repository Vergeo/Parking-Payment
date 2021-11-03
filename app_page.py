import tkinter as tk
from time import ctime
import math
from tkinter import messagebox

class App_page(tk.Frame) :
	def __init__(self, parent, app) :
		self.app = app
		self.settings = app.settings

		super().__init__(parent)
		self.grid(column=0, row=0, sticky="nsew")

		self.bg_color = "#02B0AC"
		self.mainframe = tk.Frame(self, bg= self.bg_color)
		self.mainframe.pack(fill="both", expand=True)

		self.mainframe.grid_columnconfigure(0, weight=self.settings.width//3)
		self.mainframe.grid_columnconfigure(1, weight=2*self.settings.width//3)
		self.mainframe.grid_rowconfigure(0, weight=1)

		self.pixel = tk.PhotoImage(width=0, height=0)

		# Method
		self.get_data()

		self.current_vehicle = self.vehicles[0]
		self.current_index = 0
		self.edit_mode = False
		self.vehicles_index = []

		self.create_left_content()
		self.create_right_content()

	def get_data(self) :
		self.vehicles = self.settings.load_data(self.settings.vehicle_path)

	def create_vehicles_list_box(self, full=False) :
		self.LB_left_content.delete(0, "end")
		if full :
			self.vehicles_index = []
			counter = 0
			self.get_data()
			vehicles = self.vehicles
			for vehicle in vehicles:
				self.vehicles_index.append(counter)
				counter += 1
		self.get_data()
		for index in self.vehicles_index :
			vehicle = self.vehicles[index]
			for numberPlate, vehivleDetails in vehicle.items() :
				self.LB_left_content.insert("end", numberPlate)

	def create_left_content(self) :
		self.F_left = tk.Frame(self.mainframe, bg="white", width=self.settings.width//3, height=self.settings.height)
		self.F_left.grid(column=0, row=0, sticky="nsew")

		# self.F_left.grid_rowconfigure(0, weight=self.settings.height//4)
		# self.F_left.grid_rowconfigure(1, weight=3*self.settings.height//4)

		self.F_left_header = tk.Frame(self.F_left, bg="#009694", width=self.settings.width//3, height=self.settings.height//4)
		self.F_left_header.pack(fill="both")

		self.logo = self.app.create_image(self.settings.small_logo_path)
		self.L_logo = tk.Label(self.F_left_header, image=self.logo, bg="#009694")
		self.L_logo.pack(fill="both")

		self.F_welcome = tk.Frame(self.F_left, bg="white", width=self.settings.width//3, height=27)
		self.F_welcome.pack(fill="both")

		self.L_welcome = tk.Label(self.F_welcome, text=f"Welcome, {self.app.user}", font=("Consolas", 16, "bold"), image=self.pixel, height=27, compound="c", fg=self.bg_color, bg="white")
		self.L_welcome.grid(sticky="w")

		self.F_search = tk.Frame(self.F_left, bg="blue", width=self.settings.width//3, height = 26)
		self.F_search.pack(fill="both")

		self.search_var = tk.StringVar()
		self.E_search = tk.Entry(self.F_search, font=("calibri",16), width=25, textvariable=self.search_var)
		self.E_search.pack(side="left", fill="both")

		self.i_search = self.app.create_image(self.settings.i_search_path)
		self.B_search = tk.Button(self.F_search, image=self.i_search, width=35, height=26, bd=1, bg=self.bg_color,command = self.search)
		self.B_search.pack(side="right", fill="both")

		self.F_left_content = tk.Frame(self.F_left, bg="white", width=self.settings.width//3, height=3*self.settings.height//4-56)
		self.F_left_content.pack(fill="both", expand=True)

		self.LB_left_content = tk.Listbox(self.F_left_content,width=20, height=10, font=("Arial",16), selectmode="single", bd=0)
		self.LB_left_content.pack(side="left", fill="both", expand=True)

		self.create_vehicles_list_box(True)

		self.vehicles_scroll = tk.Scrollbar(self.F_left_content)
		self.vehicles_scroll.pack(side="right", fill="y")

		self.LB_left_content.configure(yscrollcommand=self.vehicles_scroll.set)
		self.vehicles_scroll.configure(command=self.LB_left_content.yview)

		self.LB_left_content.bind("<<ListboxSelect>>", self.Lb_item_clicked)

	def create_right_content(self) :
		self.F_right = tk.Frame(self.mainframe, bg=self.bg_color, width=2*self.settings.width//3, height=self.settings.height)
		self.F_right.grid(column=1, row=0, sticky="nsew")

		self.F_right_header = tk.Frame(self.F_right, width=2*self.settings.width//3, height=self.settings.height//6, bg="#009694")
		self.F_right_header.pack(fill="both")

		plate_number = list(self.current_vehicle.keys())[0]
		self.L_vehicle_plate_number = tk.Label(self.F_right_header, width=2*self.settings.width//3, height=self.settings.height//6, bg="#009694", image=self.pixel, compound="c", text=plate_number, font=("Consolas",40,"bold"), fg="white")
		self.L_vehicle_plate_number.grid(column=0, row=0, sticky="nsew")

		for plate_number, detail in self.current_vehicle.items() :
			info = ['Type',detail["vehicle_type"],'Brand',detail["vehicle_brand"],'Time Enter',detail["time_enter"],'Time Leave',detail["time_leave"],'Duration',detail["duration"],'Price',detail["price"]]

		self.F_right_content = tk.Frame(self.F_right, width=2*self.settings.width//3, height=11*self.settings.height//15, bg=self.bg_color)
		self.F_right_content.pack(fill="both",expand=True)

		# self.F_right_content.grid_columnconfigure(0, weight=1)

		for i in range(14) :
			self.F_right_content.grid_rowconfigure(i, weight=1)

		placeholder1 = label = tk.Label(self.F_right_content, font=("Consolas",10), bg="#02B0AC")
		placeholder1.grid(column=0, row=0, sticky="w")

		placeholder2 = label = tk.Label(self.F_right_content, font=("Consolas",10), bg="#02B0AC")
		placeholder2.grid(column=0, row=13, sticky="w")

		self.tabel_info = []

		for i in range(12) :
			if i%2==0 :
				label = tk.Label(self.F_right_content, text=info[i], font=("Consolas",14,"bold"), bg="#02B0AC", fg="white")
				label.grid(column=0, row=i+1, sticky="w", padx=60)
			else :
				label = tk.Label(self.F_right_content, text=info[i], font=("Consolas",14), bg="#02B0AC", fg="white")
				label.grid(column=0, row=i+1, sticky="w", padx=60)
			self.tabel_info.append(label)

		self.F_right_footer = tk.Frame(self.F_right, width=2*self.settings.width//3, height=self.settings.height//10, bg="#02BFBC")
		self.F_right_footer.pack(fill="both")

		features = ['Add New Vehicle', 'Exit Vehicle', 'Edit Vehicle', 'Delete Vehicle']
		commands = [self.add_new_car, self.exit_car, self.edit_car_info, self.delete_car]
		self.feature_buttons = []

		for feature in features :
			button = tk.Button(self.F_right_footer, width=self.settings.width//6, height=self.settings.height//10,bg="#02BFBC", borderwidth=1, image=self.pixel, compound="c", text=feature, font=("Arial",12, "bold"), fg="white", command=commands[features.index(feature)])
			button.grid(column=features.index(feature), row=0, sticky="w")
			if feature == "Delete Vehicle" :
				button.configure(bg="#F00000")
			self.feature_buttons.append(button)

		# self.B_add_new_car = tk.Button(self.F_right_footer, width=self.settings.width//6, height=self.settings.height//10,bg="#02BFBC", borderwidth=1, image=self.pixel, compound="c", text="Add New Car", font=("Arial",14, "bold"), fg="white")
		# self.B_add_new_car.grid(column=0, row=0, sticky="w")

		# self.B_exit_car = tk.Button(self.F_right_footer, width=self.settings.width//6, height=self.settings.height//10,bg="#02BFBC", borderwidth=1, image=self.pixel, compound="c", text="Exit Car", font=("Arial",14, "bold"), fg="white")
		# self.B_exit_car.grid(column=1, row=0, sticky="w")

		# self.B_edit_car = tk.Button(self.F_right_footer, width=self.settings.width//6, height=self.settings.height//10,bg="#02BFBC", borderwidth=1, image=self.pixel, compound="c", text="Edit Car", font=("Arial",14, "bold"), fg="white", command=self.edit_car_info)
		# self.B_edit_car.grid(column=2, row=0, sticky="w")

		# self.B_delete_car = tk.Button(self.F_right_footer, width=self.settings.width//6, height=self.settings.height//10,bg="#F00000", borderwidth=1, image=self.pixel, compound="c", text="Delete Car", font=("Arial",14, "bold"), fg="white")
		# self.B_delete_car.grid(column=3, row=0, sticky="w")



	def Lb_item_clicked(self, event) :
		if not self.edit_mode :
			selection = event.widget.curselection()
			try :
				LB_index = selection[0]
			except IndexError :
				LB_index = self.current_index
			index = self.vehicles_index[LB_index]
			self.current_index = index
			self.current_vehicle = self.vehicles[index]
			for plate_number, detail in self.current_vehicle.items() :
				types = detail["vehicle_type"]
				brand = detail["vehicle_brand"]
				time_enter = detail["time_enter"]
				time_leave = detail["time_leave"]
				duration = detail["duration"]
				price = detail["price"]

			self.tabel_info[1].configure(text=types)
			self.tabel_info[3].configure(text=brand)
			self.tabel_info[5].configure(text=time_enter)
			self.tabel_info[7].configure(text=time_leave)
			self.tabel_info[9].configure(text=duration)
			self.tabel_info[11].configure(text=price)
			self.L_vehicle_plate_number.configure(text=plate_number)

	def update_page(self) :
		self.F_right.destroy()
		self.get_data()
		self.create_right_content()

		self.create_vehicles_list_box(True)

	def get_current_time(self) :
		now = ctime()
		time = ""
		day = ""
		date = ""
		month = ""
		year = ""
		for i in range(8) :
			time += now[i+11]
			if i <= 3 :
				year += now[i+20]
				if i <= 2 :
					day += now[i]
					month += now[i+4]
					if i <= 1 :
						date += now[i+8]
		current_time = time + " " + day + " " + date + " " + month + " " + year
		return current_time

	def month_to_int(self, month) :
		month = month.lower()
		if month == "jan" :
			return 1
		elif month == "feb" :
			return 2
		elif month == "mar" :
			return 3
		elif month == "apr" :
			return 4
		elif month == "may" :
			return 5
		elif month == "jun" :
			return 6
		elif month == "jul" :
			return 7
		elif month == "aug" :
			return 8
		elif month == "sep" :
			return 9
		elif month == "oct" :
			return 10
		elif month == "nov" :
			return 11
		elif month == "dec" :
			return 12

	def count_duration(self, start, end) :
		start = start
		end = end

		year1 = int(start[20]+start[21]+start[22]+start[23])
		month1 = self.month_to_int(start[16] + start[17] + start[18])
		date1 = int(start[13]+start[14])
		hour1 = int(start[0] + start[1])
		min1 = int(start[3] + start[4])
		sec1 = int(start[6] + start[7])

		year2 = int(end[20]+end[21]+end[22]+end[23])
		month2 = self.month_to_int(end[16] + end[17] + end[18])
		date2 = int(end[13]+end[14])
		hour2 = int(end[0] + end[1])
		min2 = int(end[3] + end[4])
		sec2 = int(end[6] + end[7])

		if (month1 != month2) or (year1 != year2):
			return "Error", "Error", "Error"
		else :
			year_difference = year2 - year1
			start_time = sec1 + 60*min1 + 3600*hour1 + 86400*date1
			end_time = sec2 + 60*min2 + 3600*hour2 + 86400*date2
			duration = end_time - start_time
			hour = duration//3600
			minute = (duration - hour*3600)//60
			second = duration - hour*3600 - minute*60
			return hour, minute,second

		# day = duration//86400
		# hour = (duration-day*86400)//3600
		# minute = (duration - day*86400 - hour*3600)//60
		# second = duration - day*86400 - hour*3600 - minute*60
		# return hour, minute,second, day

	def count_price(self, types, hour, minute, second) :
		duration = second + 60*minute + 3600*hour
		hours = math.ceil(duration/3600)
		price = 0
		if types == "Car" :
			if hours == 1 :
				price = 3
			elif hours > 1 :
				price = 3 + (hours-1)*2
		elif types == "Motorcycle" :
			if hours == 1 :
				price = 2
			elif hours > 1 :
				price = 2 + (hours-1)*1
		return price

	def add_new_car(self) :
		self.edit_mode = True
		self.entry_vars = []

		self.F_right = tk.Frame(self.mainframe, bg=self.bg_color, width=2*self.settings.width//3, height=self.settings.height)
		self.F_right.grid(column=1, row=0, sticky="nsew")

		self.F_right_header = tk.Frame(self.F_right, width=2*self.settings.width//3, height=self.settings.height//6, bg="#009694")
		self.F_right_header.pack(fill="both")
		self.F_right_header.grid_rowconfigure(0, weight=1)
		self.F_right_header.grid_columnconfigure(0, weight=1)

		var = tk.StringVar()
		self.E_vehicle_plate_number = tk.Entry(self.F_right_header, bg="#009694", font=("Consolas",40,"bold"), fg="white", textvariable=var)
		self.E_vehicle_plate_number.grid(column=0, row=0, sticky="nsew")
		self.entry_vars.append(var)

		for plate_number, detail in self.current_vehicle.items() :
			info = ['Type',detail["vehicle_type"],'Brand',detail["vehicle_brand"],'Time Enter',detail["time_enter"],'Time Leave',detail["time_leave"],'Duration',detail["duration"],'Price',detail["price"]]

		self.F_right_content = tk.Frame(self.F_right, width=2*self.settings.width//3, height=11*self.settings.height//15, bg=self.bg_color)
		self.F_right_content.pack(fill="both",expand=True)
		for i in range(14) :
			self.F_right_content.grid_rowconfigure(i, weight=1)

		self.F_right_content.grid_columnconfigure(0, weight=1)
		self.F_right_content.grid_columnconfigure(1, weight=100)

		placeholder1 = label = tk.Label(self.F_right_content, font=("Consolas",10), bg="#02B0AC")
		placeholder1.grid(column=0, row=0, sticky="w")

		placeholder2 = label = tk.Label(self.F_right_content, font=("Consolas",10), bg="#02B0AC")
		placeholder2.grid(column=0, row=13, sticky="w")

		self.tabel_info = []
		self.var = tk.StringVar()

		for i in range(12) :
			if i == 1 :
				var = tk.StringVar()
				radiobtn1 = tk.Radiobutton(self.F_right_content, text="Car", font=("Consolas",14,"bold"), background=self.bg_color, fg="gray90",indicatoron=0, compound="c", value="Car", variable=var, image=self.pixel, width=60, height=18)
				radiobtn1.grid(column=0, row=i+1, sticky="w", padx=60)
				radiobtn2 = tk.Radiobutton(self.F_right_content, text="Motorcycle", font=("Consolas",14,"bold"), background=self.bg_color, fg="gray90",indicatoron=0, compound="c", value="Motorcycle", variable=var, image=self.pixel, width=120, height=18)
				radiobtn2.grid(column=1, row=i+1, sticky="w")
				radiobtn1.select()
				self.tabel_info.append([radiobtn1, radiobtn2])
				self.entry_vars.append(var)
			else :
				if i%2==0 :
					label = tk.Label(self.F_right_content, text=info[i], font=("Consolas",14,"bold"), bg="#02B0AC", fg="white")
					label.grid(column=0, row=i+1, sticky="w", padx=60, columnspan=2)
					self.tabel_info.append(label)
				else :
					var = tk.StringVar()
					entry = tk.Entry(self.F_right_content, text=info[i], font=("Consolas",14), bg="#02B0AC", fg="white", width=50, textvariable=var)
					if i == 5 :
						entry.insert(0, self.get_current_time())
					entry.grid(column=0, row=i+1, sticky="w", padx=60, columnspan=2)
					self.tabel_info.append(entry)
					self.entry_vars.append(var)

		self.F_right_footer = tk.Frame(self.F_right, width=2*self.settings.width//3, height=self.settings.height//10, bg="#02BFBC")
		self.F_right_footer.pack(fill="both")

		features = ['Save', 'Cancel']
		commands= [self.save_add_new, self.cancel_edit]
		self.feature_buttons = []

		for feature in features :
			button = tk.Button(self.F_right_footer, width=self.settings.width//3, height=self.settings.height//10,bg="#02BFBC", borderwidth=1, image=self.pixel, compound="c", text=feature, font=("Arial",14, "bold"), fg="white", command=commands[features.index(feature)])
			button.grid(column=features.index(feature), row=0, sticky="w")
			if feature == "Cancel" :
				button.configure(bg="#F00000")
			self.feature_buttons.append(button)

	def save_add_new(self) :
		confirm = messagebox.askyesnocancel("Save Confirmation", "Are you sure to add this vehicle?")

		if confirm:
			self.edit_mode = False
			vehicle_plate_number = self.entry_vars[0].get()
			vehicle_type = self.entry_vars[1].get()
			vehicle_brand = self.entry_vars[2].get()
			time_enter = self.entry_vars[3].get()
			time_leave = self.entry_vars[4].get()
			duration = self.entry_vars[5].get()
			price = self.entry_vars[6].get()
			new_vehicle = {
				vehicle_plate_number : {
					"vehicle_type" : vehicle_type,
					"vehicle_brand" : vehicle_brand,
					"time_enter" : time_enter,
					"time_leave" : time_leave,
					"duration" : duration,
					"price" : price
				}
			}
			self.vehicles.append(new_vehicle)

			self.current_vehicle = self.vehicles[self.current_index]

			self.settings.save_data(self.vehicles, self.settings.vehicle_path)
			self.update_page()

	def exit_car(self) :
		plate_number = list(self.current_vehicle.keys())[0]
		for plate_number, detail in self.current_vehicle.items() :
			time_enter = detail["time_enter"]
			vehicle_type = detail["vehicle_type"]
		
		time_leave = self.get_current_time()
		hour, minute, second = self.count_duration(time_enter, time_leave)
		if hour == "Error" or minute == "Error" or second == "Error" :
			duration = "Automation error, please count manually"
			price2 = "Automation error, please count manually"
		else :
			duration = f"{hour} hour(s) {minute} minute(s) {second} second(s)"
			price2 = f"Rp {self.count_price(vehicle_type, hour, minute, second)}.000,-"

		self.vehicles[self.current_index][plate_number]["time_leave"] = time_leave
		self.vehicles[self.current_index][plate_number]["duration"] = duration
		self.vehicles[self.current_index][plate_number]["price"] = price2
		self.settings.save_data(self.vehicles, self.settings.vehicle_path)
		self.update_page()

	def edit_car_info(self) :
		self.edit_mode = True
		self.entry_vars = []

		self.F_right = tk.Frame(self.mainframe, bg=self.bg_color, width=2*self.settings.width//3, height=self.settings.height)
		self.F_right.grid(column=1, row=0, sticky="nsew")

		self.F_right_header = tk.Frame(self.F_right, width=2*self.settings.width//3, height=self.settings.height//6, bg="#009694")
		self.F_right_header.pack(fill="both")
		self.F_right_header.grid_rowconfigure(0, weight=1)
		self.F_right_header.grid_columnconfigure(0, weight=1)

		var = tk.StringVar()
		plate_number = list(self.current_vehicle.keys())[0]
		self.E_vehicle_plate_number = tk.Entry(self.F_right_header, bg="#009694", text=plate_number, font=("Consolas",40,"bold"), fg="white", textvariable=var)
		self.E_vehicle_plate_number.grid(column=0, row=0, sticky="nsew")
		self.E_vehicle_plate_number.insert("end", plate_number)
		self.entry_vars.append(var)

		for plate_number, detail in self.current_vehicle.items() :
			info = ['Type',detail["vehicle_type"],'Brand',detail["vehicle_brand"],'Time Enter',detail["time_enter"],'Time Leave',detail["time_leave"],'Duration',detail["duration"],'Price',detail["price"]]

		self.F_right_content = tk.Frame(self.F_right, width=2*self.settings.width//3, height=11*self.settings.height//15, bg=self.bg_color)
		self.F_right_content.pack(fill="both",expand=True)
		for i in range(14) :
			self.F_right_content.grid_rowconfigure(i, weight=1)

		self.F_right_content.grid_columnconfigure(0, weight=1)
		self.F_right_content.grid_columnconfigure(1, weight=100)

		placeholder1 = label = tk.Label(self.F_right_content, font=("Consolas",10), bg="#02B0AC")
		placeholder1.grid(column=0, row=0, sticky="w")

		placeholder2 = label = tk.Label(self.F_right_content, font=("Consolas",10), bg="#02B0AC")
		placeholder2.grid(column=0, row=13, sticky="w")

		self.tabel_info = []
		self.var = tk.StringVar()

		for i in range(12) :
			if i == 1 :
				var = tk.StringVar()
				radiobtn1 = tk.Radiobutton(self.F_right_content, text="Car", font=("Consolas",14,"bold"), background=self.bg_color, fg="gray90",indicatoron=0, compound="c", value="Car", variable=var, image=self.pixel, width=60, height=18)
				radiobtn1.grid(column=0, row=i+1, sticky="w", padx=60)
				radiobtn2 = tk.Radiobutton(self.F_right_content, text="Motorcycle", font=("Consolas",14,"bold"), background=self.bg_color, fg="gray90",indicatoron=0, compound="c", value="Motorcycle", variable=var, image=self.pixel, width=120, height=18)
				radiobtn2.grid(column=1, row=i+1, sticky="w")
				if info[i] == "Motorcycle" :
					radiobtn2.select()
				else :
					radiobtn1.select()
				self.tabel_info.append([radiobtn1, radiobtn2])
				self.entry_vars.append(var)
			else :
				if i%2==0 :
					label = tk.Label(self.F_right_content, text=info[i], font=("Consolas",14,"bold"), bg="#02B0AC", fg="white")
					label.grid(column=0, row=i+1, sticky="w", padx=60, columnspan=2)
					self.tabel_info.append(label)
				else :
					var = tk.StringVar()
					entry = tk.Entry(self.F_right_content, text=info[i], font=("Consolas",14), bg="#02B0AC", fg="white", width=50, textvariable=var)
					entry.insert(0, info[i])
					entry.grid(column=0, row=i+1, sticky="w", padx=60, columnspan=2)
					self.tabel_info.append(entry)
					self.entry_vars.append(var)

		self.F_right_footer = tk.Frame(self.F_right, width=2*self.settings.width//3, height=self.settings.height//10, bg="#02BFBC")
		self.F_right_footer.pack(fill="both")

		features = ['Save', 'Cancel']
		commands= [self.save_edit, self.cancel_edit]
		self.feature_buttons = []

		for feature in features :
			button = tk.Button(self.F_right_footer, width=self.settings.width//3, height=self.settings.height//10,bg="#02BFBC", borderwidth=1, image=self.pixel, compound="c", text=feature, font=("Arial",14, "bold"), fg="white", command=commands[features.index(feature)])
			button.grid(column=features.index(feature), row=0, sticky="w")
			if feature == "Cancel" :
				button.configure(bg="#F00000")
			self.feature_buttons.append(button)

	def save_edit(self) :
		confirm = messagebox.askyesnocancel("Save Confirmation", "Are you sure to save this edited vehicle?")

		if confirm:
			self.edit_mode = False
			vehicle_plate_number = self.entry_vars[0].get()
			vehicle_type = self.entry_vars[1].get()
			vehicle_brand = self.entry_vars[2].get()
			time_enter = self.entry_vars[3].get()
			time_leave = self.entry_vars[4].get()
			duration = self.entry_vars[5].get()
			price = self.entry_vars[6].get()
			self.vehicles[self.current_index] = {
				vehicle_plate_number : {
					"vehicle_type" : vehicle_type,
					"vehicle_brand" : vehicle_brand,
					"time_enter" : time_enter,
					"time_leave" : time_leave,
					"duration" : duration,
					"price" : price
				}
			}

			self.current_vehicle = self.vehicles[self.current_index]

			self.settings.save_data(self.vehicles, self.settings.vehicle_path)
			self.update_page()

	def cancel_edit(self) :
		self.edit_mode = False
		self.update_page()

	def delete_car(self) :
		confirm = messagebox.askyesno("Delete Confirmation", "Are you sure to delete this vehicle?")

		if confirm :
			del self.vehicles[self.current_index]
			self.settings.save_data(self.vehicles, self.settings.vehicle_path)
			self.current_index = 0
			self.current_vehicle = self.vehicles[self.current_index]
			self.update_page()

	def search(self) :
		item_search = self.search_var.get()
		self.get_data()
		vehicles = self.vehicles
		self.vehicles_index = []
		counter = 0

		if item_search == "" :
			self.create_vehicles_list_box(True)
		else :
			for vehicle in vehicles :
				for numberPlate, detail in vehicle.items() :
					if item_search in numberPlate :
						self.vehicles_index.append(counter)
					elif item_search in detail["vehicle_type"] :
						self.vehicles_index.append(counter)
					elif item_search in detail["vehicle_brand"] :
						self.vehicles_index.append(counter)
					# elif item_search in detail["time_enter"] :
					# 	self.vehicles_index.append(counter)
					# elif item_search in detail["time_leave"] :
					# 	self.vehicles_index.append(counter)
					# elif item_search in detail["duration"] :
					# 	self.vehicles_index.append(counter)
					# elif item_search in detail["price"] :
					# 	self.vehicles_index.append(counter)

				counter +=1

		self.create_vehicles_list_box()



"""
PRICE

Car :
First 1 hour	: 3000
Every next hour	: 2000

Motorcycle :
First 1 hour	: 2000
Every next hour	: 1000
"""