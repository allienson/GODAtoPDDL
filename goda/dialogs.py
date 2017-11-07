# from tkinter import *
# master = Tk()

# def var_states():
#    print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))


# def dialog(objects, tasks):	
# 	i = 0
# 	Label(master, text="Selecione os elementos que devem ser inicializados:").grid(row=0, sticky=W)
# 	for obj in objects:
# 		if(objects[obj] == True):
# 			Checkbutton(master, text=obj, variable=objects[obj], onvalue=True, offvalue=False).grid(row=i+2, sticky=W)
# 			i+=1
	
# 	Label(master, text="Selecione as regras opcionais:").grid(row=i+2, sticky=W)
# 	j=0
# 	#i+4
# 	for task in tasks:
# 		if 'opt' in task:
# 			Checkbutton(master, text=task, variable=tasks[j], onvalue=True, offvalue=False).grid(row=i+6, sticky=W)
# 			j+=1		

# 	Button(master, text='Accept', command=master.quit).grid(row=i+10, sticky=W, pady=4)
# 	mainloop()
# 	#return objects
# from tkinter import *
# from tkinter import ttk
# root = Tk()


# frame = ttk.Frame(root)
# frame['padding'] = (10,10)
# frame['borderwidth'] = 3

# label = ttk.Label(root, text='Full name:')


# # l =ttk.Label(root, text="Starting...")
# # l.grid()
# # l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
# # l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
# # l.bind('<1>', lambda e: l.configure(text='Clicked left mouse button'))
# # l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
# # l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))

# def dialog(objects, tasks):	
# 	# root = Tk()
# 	# my_gui = GuessingGame(root)
# 	root.mainloop()


import tkinter as tk

class Chooser(tk.Frame):
    def __init__(self, root, objects, tasks, *args, **kwargs):
        self.objects = objects
        self.tasks = tasks
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root

        self.vsb = tk.Scrollbar(self, orient="vertical")
        self.text = tk.Text(self, width=40, height=20, 
                            yscrollcommand=self.vsb.set)
        self.vsb.config(command=self.text.yview)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

        self.objLabel = tk.Label(self, text="Selecione os objetos:")
        self.objLabel.pack()

        for item in self.objects:
            if(objects[item] == True):
	            cb = tk.Checkbutton(self, text=item, onvalue=True, offvalue=False)
	            self.text.window_create("end", window=cb)
	            self.text.insert("end", "\n") # to force one checkbox per line

def dialog(objects, tasks):
    root = tk.Tk()
    Chooser(root, objects, tasks).pack(side="top", fill="both", expand=True)
    root.mainloop()