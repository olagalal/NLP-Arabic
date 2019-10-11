from NLPAR import *
import tkinter as tk
from tkinter import *

class NLPCS(tk.Tk):
	def __init__(self):	
		tk.Tk.__init__(self)
		self.title("GUI")
		self.geometry("250x100")
		self.f1=tk.Frame(self)
		self.f2=tk.Frame(self)
		self.f3=tk.Frame(self)
		self.f1.pack()
		self.f2.pack()
		self.f3.pack()
		
		self.l1=tk.Label(self.f1,text='Word')
		self.e1=tk.Entry(self.f1)
		
		self.l2=tk.Label(self.f2,text='Tag')
		self.e2=tk.Entry(self.f2)
		
		self.b=tk.Button(self.f3, text="Get Tag", command=self.main)
		
		self.f1.pack()
		self.f2.pack()
		self.f3.pack()
		
		self.l1.pack(side=LEFT)
		self.e1.pack(side=RIGHT)
		self.l2.pack(side=LEFT)
		self.e2.pack(side=RIGHT)
		self.b.pack()
	
	def main(self):
		w =self.e1.get()
		ans = self.pos(w)
		self.e2.delete(0, 'end')
		self.e2.insert(0, ans)

	
	def pos(self, w):
		ob = NLPAR()
		L=[]
		L.append(w)
		p = ob.ARPosTag(L)
		return p[0][1]
		
	
app = NLPCS()
app.mainloop()
