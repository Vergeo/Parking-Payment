import tkinter as tk
import sys

class Login_page(tk.Frame) :
	def __init__(self, parent, app) :
		self.app = app
		self.settings = app.settings

		super().__init__(parent)
		self.grid(column=0, row=0, sticky="nsew")

		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		self.bg_color = "#02B0AC"
		self.mainframe = tk.Frame(self, bg=self.bg_color)
		self.mainframe.pack(fill="both", expand=True)

		self.mainframe.grid_columnconfigure(0, weight=1)
		self.mainframe.grid_columnconfigure(1, weight=1)
		# self.mainframe.grid_rowconfigure(0, weight=1)

		# Method
		self.create_logo()
		self.create_login_template()

	def create_logo(self) :
		self.logo = self.app.create_image(self.settings.logo_path)
		self.L_logo = tk.Label(self.mainframe, image=self.logo, bg=self.bg_color)
		self.L_logo.grid(column=0, row=0, sticky="nsew", columnspan=2, pady=30)

	def create_login_template(self) :
		self.var_username = tk.StringVar()
		self.var_password = tk.StringVar()

		self.i_username = self.app.create_image(self.settings.i_username_path)
		self.i_password = self.app.create_image(self.settings.i_password_path)
		self.i_quit = self.app.create_image(self.settings.i_quit_path)

		self.L_username = tk.Label(self.mainframe, image=self.i_username)
		self.L_username.grid(column=0, row=1,sticky="e", padx=9,pady=6)

		self.E_username = tk.Entry(self.mainframe, width=23, font=("consolas",20), bd=0, fg=self.bg_color, textvariable=self.var_username)
		self.E_username.grid(column=1, row=1, sticky="w", padx=9,pady=6)

		self.L_password = tk.Label(self.mainframe, image=self.i_password)
		self.L_password.grid(column=0, row=2,sticky="e", padx=9,pady=6)

		self.E_password = tk.Entry(self.mainframe, width=23, font=("consolas",20), bd=0, fg=self.bg_color, textvariable=self.var_password, show="*")
		self.E_password.grid(column=1, row=2, sticky="w", padx=9,pady=6)

		self.B_quit = tk.Button(self.mainframe, image=self.i_quit, borderwidth=0, bd=0, command=self.app.app.exit)
		self.B_quit.grid(column=0, row=3, sticky="e", padx=9,pady=21)

		self.B_login = tk.Button(self.mainframe, text="LOGIN", font=("arial",16, "bold"), bd =0, borderwidth=0, width=26, fg=self.bg_color, command=self.app.login)
		self.B_login.grid(column=1, row=3, sticky="w", padx=10, pady=21)
