import tkinter as tk
from PIL import Image, ImageTk
import sys

from settings import Settings
from login_page import Login_page
from app_page import App_page
from tkinter import messagebox

class Window(tk.Tk) :
	def __init__(self, app) :
		self.app = app
		self.settings = app.settings
		self.logged_in = False
		super().__init__()

		# Config
		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.icon_pic = tk.PhotoImage(file=self.settings.logo_path)
		self.iconphoto(False, self.icon_pic)
		# self.resizable(0,0)

		self.user = ""

		# Pages
		self.pages = {}

		# Method
		self.create_menu()
		self.create_container()
		self.create_page()

	def create_menu(self) :
		self.menubar = tk.Menu(self)
		self.configure(menu=self.menubar)

		self.file_menu = tk.Menu(self.menubar, tearoff=False)
		self.file_menu.add_command(label="New Vehicle",command=self.new_vehicle)
		self.file_menu.add_command(label="Exit", command=self.app.exit)

		self.help_menu = tk.Menu(self.menubar, tearoff=False)
		self.help_menu.add_command(label="About",command=self.about)

		self.menubar.add_cascade(label='File', menu=self.file_menu)
		self.menubar.add_cascade(label='Help', menu=self.help_menu)

	def create_container(self) :
		self.container = tk.Frame(self)
		self.container.pack(fill="both", expand=True)

	def create_page(self) :
		self.pages["login_page"] = Login_page(self.container, self)

	def create_image(self, path) :
		image = ImageTk.PhotoImage(Image.open(path))
		return image

	def change_page(self, page) :
		page = self.pages[page]
		page.tkraise()

	def login(self) :
		username = self.pages["login_page"].var_username.get()
		password = self.pages["login_page"].var_password.get()
		self.user = username
		match = self.settings.login(username, password)
		if match :
			self.pages["app_page"] = App_page(self.container, self)
			self.change_page("app_page")
			self.logged_in = True
		else :
			messagebox.showerror("Login Error!", "Wrong username or password!")

	def new_vehicle(self) :
		if self.logged_in :
			self.pages["app_page"].add_new_car()
		else :
			messagebox.showerror("Error!", "You have not logged in yet!")

	def about(self) :
		messagebox.showinfo("About", "Creator\t: Vergeo\nVersion\t: 1.0")


class App :
	def __init__(self) :
		self.settings = Settings()
		self.main_window = Window(self)

	def run(self) :
		self.main_window.mainloop()

	def exit(self) :
		confirm = messagebox.askyesno("Exit Confirmation", "Are you sure you want to close the program?")
		if confirm :
			sys.exit()

if __name__ == "__main__" :
	Good_Parking = App()
	Good_Parking.run()