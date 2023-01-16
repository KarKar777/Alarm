from playsound import *
from datetime import *
from tkinter import *
n = ''
def s(event):
    global n
    n = txt.get()
    root.destroy()



def alarm(user_minutes, s):
    user_minutes = int(user_minutes)
    data = datetime.now()
    minutes = data.minute
    hours = data.hour
    minutes = (minutes + user_minutes) % 60
    hours += (minutes + user_minutes) // 60
    while True:
        newData = datetime.now()
        if minutes == newData.minute and hours == newData.hour:
            root = Tk()
            root.title('Timer')
            root.geometry('400x200+600+300')
            playsound("s.mp3", False)
            l = Label(text=s)
            l.pack()
            root.mainloop()
            break


root = Tk()
root.title('Timer')
root.geometry('400x200+600+300')

txt = StringVar()

l = Label(text="Введите через сколько минут вы хотите получить\nнапоминание и о чем вам напомнить через пробел.")
b = Button(text='Запустить')
e = Entry(textvariable=txt)
b.bind('<Button-1>', s)
l.pack()
e.pack()
b.pack()
root.mainloop()
n = n.split()

alarm(n[0], n[1])