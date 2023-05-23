import tkinter as tk
from tkinter import messagebox
class Finestra(tk.Tk):
	def __init__(self,nome=""):
		super().__init__()
		self.title("Gestione "+ nome)
		self.geometry("750x450")
		self.resizable(1,1)
		self.creawidget()
	def creawidget(self):
		widget1=tk.Label(self,text="expand=True || fill=y || side=top",bg="Red")
		widget1.pack(side="top",expand=True,fill="y")
		
		
		widget2=tk.Label(self,text="expand=False || fill=both || side=top",bg="green")
		widget2.pack(side="top",expand=False,fill="both")
		
		
		widget3=tk.Label(self,text="expand=True || fill=both || side=top",bg="yellow")
		widget3.pack(side="top",expand=True,fill="both")
		
		space=tk.Label(self,text="")
		space.pack(side="top",expand=True,fill="both")
		
		
		widget4=tk.Label(self,text="expand=True || fill=None || side=left",bg="Red")
		widget4.pack(side="left",expand=True,fill=None)
		
		
		widget5=tk.Label(self,text="expand=False || fill=y || side=left",bg="green")
		widget5.pack(side="left",expand=False,fill=None)
		
		
		widget6=tk.Label(self,text="expand=True || fill=x || side=left",bg="yellow")
		widget6.pack(side="left",expand=True,fill="x")
		
		space2=tk.Label(self,text="")
		space2.pack(side="top",expand=True,fill="both")
		
		space3=tk.Label(self,text="")
		space3.pack(side="top",expand=True,fill="both")
		
def main():
	win=Finestra("Pack")
	win.mainloop()
main()
