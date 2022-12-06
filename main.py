from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from data import *

#colors
co0 = "#444466"  # black
co1 = "#feffff"  # White
co2 = "#6f9fbd"  # blue
co3 = "#403d3d"   # ash

window = Tk()
window.title('TIMUN 5.0 Organizing Committee')
window.geometry('550x510')
window.resizable(width=False, height=False)
window.configure(bg=co1)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

main_frame = Frame(window, width=540, height=305, bg=co1)
main_frame.grid(row=0, column=0, padx=1, pady=1)

def choose_timun(i):
    global l_icon_1, timun_image

    main_frame['bg'] = timun[i]['others'][1]

    timun_name['text'] = i
    timun_name['bg'] = timun[i]['others'][1]
    timun_info['text'] = timun[i]['info'][1]
    timun_info['bg'] = co3
    timun_number['text'] = timun[i]['info'][0]
    timun_number['bg'] = timun[i]['others'][1]

    image = timun[i]['others'][0]
    timun_image = Image.open(image)
    timun_image = timun_image.resize((250, 250))
    timun_image = ImageTk.PhotoImage(timun_image)

    l_icon_1 = Label(main_frame, image=timun_image, bg=timun[i]['others'][1])
    l_icon_1.place(x=60, y=50)


    timun_name['fg'] = co1

    # loading status
    timun_hp['text'] = timun[i]['info'][2]
    timun_age['text'] = timun[i]['about'][0]
    timun_university['text'] = timun[i]['about'][1]
    timun_academic['text'] = timun[i]['about'][2]
    
    timun_info.lift()
    timun_number.lift()

timun_name = Label(main_frame,text = "timun name", anchor="center", font=("Ivy 20 bold"), fg=co1)
timun_name.place(x=15, y=15)

timun_info = Label(main_frame,text = "timun info", anchor="center", font=("Verdana 10 bold"), fg=co1)
timun_info.place(x=20, y=50)

timun_number = Label(main_frame,text = "timun number", anchor="center", font=("Verdana 8 bold"), fg=co1)
timun_number.place(x=20, y=75)

timun_info.lift()
timun_number.lift()


#status--------------------------

timun_status = Label(window, text="About", font=("Verdana 20"), bg=co1, fg=co0)
timun_status.place(x=15, y=310)

timun_st = Label(window, text="Name:", font=("Verdana 10"), bg=co1, fg=co0)
timun_st.place(x=15, y=362)

timun_hp = Label(window, text="name", font=("Verdana 10"), bg=co1, fg=co0)
timun_hp.place(x=95, y=362)

timun_st = Label(window, text="Age:", font=("Verdana 10"), bg=co1, fg=co0)
timun_st.place(x=15, y=385)

timun_age = Label(window, text="age", font=("Verdana 10"), bg=co1, fg=co0)
timun_age.place(x=95, y=385)

timun_st = Label(window, text="University:", font=("Verdana 10"), bg=co1, fg=co0)
timun_st.place(x=15, y=410)

timun_university = Label(window, text="university", font=("Verdana 10"), bg=co1, fg=co0)
timun_university.place(x=95, y=410)

timun_st = Label(window, text="Academic:", font=("Verdana 10"), bg=co1, fg=co0)
timun_st.place(x=15, y=435 )

timun_academic = Label(window, text="academic", font=("Verdana 10"), bg=co1, fg=co0)
timun_academic.place(x=95, y=435)


#loading all timuns

img_timun_1 = Image.open('Images/Prajjawal.jpeg')
img_timun_1 = img_timun_1.resize((40, 40))
img_timun_1 = ImageTk.PhotoImage(img_timun_1)

icon_1 = Button(window, text='Prajjawal',command = lambda:choose_timun('Prajjawal'), width=150, image=img_timun_1, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_1.place(x=375, y=10)

img_timun_2 = Image.open('Images/Sujal.jpg')
img_timun_2 = img_timun_2.resize((40, 40))
img_timun_2 = ImageTk.PhotoImage(img_timun_2)

icon_2 = Button(window, text='Sujal', command = lambda:choose_timun('Sujal'), width=150, image=img_timun_2, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_2.place(x=375, y=65)

img_timun_3 = Image.open('Images/Aarti.jpg')
img_timun_3 = img_timun_3.resize((40, 40))
img_timun_3 = ImageTk.PhotoImage(img_timun_3)

icon_3 = Button(window, text='Aarati',command = lambda:choose_timun('Aarati'), width=150, image=img_timun_3, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_3.place(x=375, y=120)

img_timun_4 = Image.open('Images/Diparshan.jpg')
img_timun_4 = img_timun_4.resize((40, 40))
img_timun_4 = ImageTk.PhotoImage(img_timun_4)

icon_4 = Button(window, text='Diparshan', width=150,command = lambda:choose_timun('Diparshan'), image=img_timun_4, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_4.place(x=375, y=175)

img_timun_5 = Image.open('Images/Sworup.jpg')
img_timun_5 = img_timun_5.resize((40, 40))
img_timun_5 = ImageTk.PhotoImage(img_timun_5)

icon_5 = Button(window, text='Sworup',command = lambda:choose_timun('Sworup'), width=150, image=img_timun_5, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_5.place(x=375, y=230)

img_timun_6 = Image.open('Images/Dipesh.jpg')
img_timun_6 = img_timun_6.resize((40, 40))
img_timun_6 = ImageTk.PhotoImage(img_timun_6)

icon_6 = Button(window, text='Dipesh',command = lambda:choose_timun('Dipesh'), width=150, image=img_timun_6, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_6.place(x=375, y=285)



choose_timun('Prajjawal')   
window.mainloop()