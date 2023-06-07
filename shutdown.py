import tkinter
from tkinter import *
import os

def restart():
    os.system("shutdown -r -t 1") # shutdwon in 1 sec
    
def restart_time():
    os.system("shutdown -r -t 20") # restart after 20 sec

def shutdown():
    os.system("shutdown -s -t 1") # shutdwon in 1 sec  

st = Tk()
st.title("Shut Down App")
st.geometry("500x500")
st.config(bg = "Green")

r_button = Button (st, text="Restart", font = ("arial", 20, "bold"), bg = "red", cursor ="plus", command=restart)
r_button.place(x= 150, y= 60, width = 200, height = 50)

#restart with time
r_button = Button (st, text="Restart time", font = ("arial", 20, "bold"), bg = "red", cursor ="plus", command=restart_time)
r_button.place(x= 150, y= 170, width = 200, height = 50)

#shutdown
r_button = Button (st, text="shutdown", font = ("arial", 20, "bold"), bg = "red", cursor ="plus", command =shutdown)
r_button.place(x= 150, y= 270, width = 200, height = 50)

#close
r_button = Button (st, text="close", font = ("arial", 20, "bold"), bg = "red", cursor ="plus", command = st.destroy)
r_button.place(x= 150, y= 370, width = 200, height = 50)

st.mainloop()


