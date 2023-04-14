
import tkinter as tk
from tkinter import ttk


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {}

		for F in (GraphTraversal, ShortestPath, TravelingSalesmen):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(GraphTraversal)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class GraphTraversal(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = ttk.Label(self, text ="GraphTraversal", font = LARGEFONT)

		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="ShortestPath",
		command = lambda : controller.show_frame(ShortestPath))
	
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		button2 = ttk.Button(self, text ="TravelingSalesmen",
		command = lambda : controller.show_frame(TravelingSalesmen))
	
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="ShortestPath", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="GraphTraversal",
							command = lambda : controller.show_frame(GraphTraversal))

		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		button2 = ttk.Button(self, text ="Traveling Salesmen",
							command = lambda : controller.show_frame(TravelingSalesmen))
	
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)




class TravelingSalesmen(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="TravelingSalesmen", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="ShortestPath",
							command = lambda : controller.show_frame(ShortestPath))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="GraphTraversal",
							command = lambda : controller.show_frame(GraphTraversal))
	
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.mainloop()






