#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 16:49:23 2021

@author: divyeshdhanvijay
"""

from tkinter import *
import random 

root=Tk()
root.title("Multi-dimensional arrays")
root.geometry("500x500")

label=Label(root)

array_3d = [[[1,2,3,4,5,6],["Black","White"],["A","B","C","D","E","F","G","H"]]]
print(array_3d[0][1][1])


def new_password(): 
    random_no_1 =  random.randint(0,5)
    random_no_2 =  random.randint(0,1)
    random_no_3 =  random.randint(0,6)
    
    letter1 = str(array_3d[0][0][random_no_1])
    letter2 = (array_3d[0][1][random_no_2])
    letter3 = (array_3d[0][0][0])
    label["text"] = letter1 + letter2 + + letter3
    
    
button = Button(root, text= "Get new password", command= new_password)
button.place(relx = 0.5, rely = 0.6, anchor= CENTER)
    
label.place(relx = 0.5, rely = 0.7, anchor= CENTER)
    
root.mainloop()