# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:30:47 2022

Resources:
https://docs.python.org/3/library/tkinter.html
https://realpython.com/python-gui-tkinter/
https://www.tutussfunny.com/search-using-python-gui-mysql/
https://stackoverflow.com/questions/41528482/output-data-from-list-using-search-button-python

@author: crystalpiroozy2525
"""

import tkinter as tk
import psycopg2
import pandas as pd
from tkinter import *
#The AWS database has been deleted, so that costs do not accrue for myself and unauthorized
#access does not take place. However, the test() function was created to demonstrate the input 
#and index retrieval method with tkinter.

#list retrieval function
x = ['22-33-44-4536', '22-77-44-7265', '33-66-54-6625', '12-43-22-1234']

def test():
    text = e1.get()
    #.upper()

    for a in x:
        b = x.index(text)
        c = x[b]
        e1.delete(0, END)
        e1.insert(END, x[2])
        print("x = ", x)
        print("You searched: ", c)
        print('ParcelID: ', c, 'and ', 'Index in list "x": ', b)


#AWS RDS cloud PostgreSQL database retrieval function    
def submit_fid():
    global myresult
    parcelid = e1.get()

    engine = psycopg2.connect(
    database="MapleRidge",
    user="###",
    password="###",
    host="###",
    port='5432'
    )
    cursor = engine.cursor()
    try:
        cursor.execute("""
          SELECT conduit.facilityid, conduit.drawingid, conduit.originalso As originalsource 
          FROM stormwater.conduit CROSS JOIN stormwater.parcel WHERE parcel.taxid = %s 
          AND ST_Intersects(parcel.geom, conduit.geom)
          """, (parcelid,))
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        e1.delete(0, END)
        e1.insert(END, x[2])
    except Exception as e:
       print(e)
       psycopg2.rollback()
       psycopg2.close()

#tkinter GUI development  
main_window = Tk()
main_window.title("Search Stormwater Database")
main_window.geometry("300x200")

fid_label = tk.Label(main_window, text="Parcelid").place(x=10, y=10)

#command in fid_button is replaced with the test() function to demonstrate the retrieval and output method using the GUI.

fid_button = Button(main_window, text="Search", command=test ,height = 1, width = 13).place(x=140, y=40)

fid_output = tk.Label(main_window, text = "")
fid_output.pack(pady=50)

e1 = Entry(main_window)
e1.place(x=140, y=10)

main_window.mainloop()







