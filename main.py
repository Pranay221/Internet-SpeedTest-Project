import speedtest
from tkinter import *
import tkinter as tk

from tkinter import messagebox

root=tk.Tk()

root.title('Internet Speedtest Application')

root.geometry('400x400')

root.configure(bg='black')

st=speedtest.Speedtest()

font=('Verdana',15,'bold')

def check():

    messagebox.showinfo("Confirmation", '''Speedtest starting...
                           May take up to 1 min... ''')

    down=(str(st.download()//10**6)+" Mbps")
    up=(str(st.upload()//10**6)+" Mbps")
    ping=(str(int(st.results.ping))+" Ms")
    a.set(down)
    bc.set(up)
    c.set(ping)
    m.set("SpeedTest Complete")
    #d.configure(text=str(st.download()//10**6)+" Mbps")
    #u.configure(text=str(st.upload()//10**6)+" Mbps")
    #p.configure(text=str(int(st.results.ping))+" Ms")
    #l.configure(text="SpeedTest Complete")






a=StringVar()
a.set('0 Mbps')
bc=StringVar()
bc.set('0 Mbps')
c=StringVar()
c.set('0 Ms')
m=StringVar()
m.set('Click here to start the SpeedTest...')
dspeed= tk.Label(root, text='Download speed:',bg='black',fg='yellow',font=font).place(x=10,y=10)
d= tk.Label(root,textvariable=a,bg='black',fg='yellow',font=font).place(x=250,y=10)
uspeed= tk.Label(root, text='Upload speed:',bg='black',fg='yellow',font=font).place(x=10,y=50)
u= tk.Label(root,textvariable=bc, bg='black',fg='yellow',font=font).place(x=250,y=50)
ping= tk.Label(root, text='Ping:',bg='black',fg='yellow',font=font).place(x=10,y=90)
p= tk.Label(root,textvariable=c,bg='black',fg='yellow',font=font).place(x=250,y=90)
l= tk.Label(root,textvariable=m,bg='black',fg='yellow',font=(15)).place(x=50,y=250)

b=tk.Button(root,text='SpeedTest',command=check,bg='yellow',fg='black')

b.place(x=50,y=300,height=40,width=300)

root.mainloop()
