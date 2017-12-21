import tkinter


class MainProgram():
	"""docstring for MainProgram"""
	
	#global stuff
	global window

	window = tkinter.Tk()
	window.geometry("640x480")
	window.title("Tagser")

	#useful
	def clearScreen():
		widget_list = window.grid_slaves()
		for widget in widget_list:
			widget.destroy()

	#events

	def back(event):
		MainProgram.mainMenu()
		window.update_idletasks()

	def addTagsMode(event):
		MainProgram.clearScreen()
		#-things in the menu
		images_path_label = tkinter.Label(master=window, text="Image Folder:")
		images_path_entry = tkinter.Entry(master=window)
		folder_button = tkinter.Button(master=window, text="...")

		tags_label = tkinter.Label(master=window, text="Tags:")
		tags_entry = tags_label = tkinter.Label(master=window)

			#container with images
		set_button = tkinter.Button(master=window, text="Set Tags")
		back_button = tkinter.Button(master=window, text="Back to Menu")

		#-where they go

		images_path_label.grid(column=0,row=0)
		images_path_entry.grid(column=0,row=1)
		folder_button.grid(column=1,row=1)
		
		tags_label.grid(column=0, row=2)
		tags_entry.grid(column=0, row=3)

			#container with images

		set_button.grid(column=0, row=4)
		back_button.grid(column=1, row=4)
		
		
		#-what they do
		back_button.bind("<Button-1>", MainProgram.back)

		window.update_idletasks()

	def viewImagesMode(event):
		MainProgram.clearScreen()
		#-things in the menu
		images_path_label = tkinter.Label(master=window, text="Image Folder:")
		images_path_entry = tkinter.Entry(master=window)
		folder_button = tkinter.Button(master=window, text="...")

		tags_label = tkinter.Label(master=window, text="Tags:")
		tags_entry = tags_label = tkinter.Label(master=window)

			#container with images

		back_button = tkinter.Button(master=window, text="Back to Menu")

		#-where they go

		images_path_label.grid(column=0,row=0)
		images_path_entry.grid(column=0,row=1)
		folder_button.grid(column=1,row=1)
		
		tags_label.grid(column=0, row=2)
		tags_entry.grid(column=0, row=3)

			#container with images

		back_button.grid(column=0, row=4)
		
		#-what they do
		back_button.bind("<Button-1>", MainProgram.back)

		window.update_idletasks()

	#main menu function. It has to be run last because the other pages have to load first	
	def mainMenu():
		MainProgram.clearScreen()
		#things in the menu
		display_images_button = tkinter.Button(master=window, text="Display Images")
		add_tags_button = tkinter.Button(master=window, text="Add Tags")
		
		#where they go
		add_tags_button.grid(column=0, row=1)
		display_images_button.grid(column=0, row=0)

		#what they do
		add_tags_button.bind("<Button-1>", MainProgram.addTagsMode)
		display_images_button.bind("<Button-1>", MainProgram.viewImagesMode)
	
	def start():
		MainProgram.mainMenu()
		window.mainloop()

MainProgram.start()