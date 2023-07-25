from tkinter import *
import calendar
from datetime import date

root = Tk()

def showcalendar():
    #get the month and the year the user has chosen in the spinbox
    month = int(month_box.get())
    year = int(year_box.get())
    #pass the values chosen by user to the calendar module to get a formatted text calendar representing the specified year and month
    output_calendar = calendar.month(year, month)
    #clear out any existing data from the sreen 1.0 indicates the beginning of the field and 'end' indicates the end of the field
    calendar_field.delete(1.0,'end')
    #finally insert the calendar generated earlier and display on the screen in the calendar_field
    calendar_field.insert('end',output_calendar)
    
    
def reset():
     #clear out any existing data from the sreen 1.0 indicates the beginning of the field and 'end' indicates the end of the field
    calendar_field.delete(1.0,'end')
    #set month and year to the present month and year respectively when the screen is cleared
    month_var.set(current_month)
    year_var.set(current_year)
    #using the config() method to display the current month and year in the screen when it is cleared
    month_box.config(textvariable=month_var)
    year_box.config(textvariable=year_var)
 
 #function to close the window or screen and exit from the program   
def close():
    root.destroy()

root.title("Calendar")
root.geometry('500x500')
root.resizable(0,0)
root.config(background='lightblue')

#defining 4 frames for the header title,the month and year entry,the display and the buttons
header_frame = Frame(root)
entry_frame = Frame(root)
result_frame = Frame(root)
button_frame = Frame(root)

#frames are placed in blocks using the pack() method,expand=True to enable the widget to resize and expand in its available space
#fill attribure to both to allow the widget to expandto occupy the entire window in the x and y direction
header_frame.pack(expand=True,fill='both')
entry_frame.pack(expand=True,fill='both')
result_frame.pack(expand=True,fill='both')
button_frame.pack(expand=True,fill='both')

#specify 3 labels for header,month and year
header_label = Label(header_frame,text='CALENDAR',font=('ariel',25,'bold'),fg='#A020F0')
header_label.pack(expand=True,fill='both')

month_label = Label(entry_frame,text='Month:',font=('ariel',15,'bold'),fg='#000000')
month_label.place(x=30,y=0)

year_label = Label(entry_frame,text='Year:',font=('ariel',15,'bold'),fg='#000000')
year_label.place(x=275,y=0)

#using the Intvar() function with the entry_frame to set and receive integer data for the month and year
month_var = IntVar(entry_frame)
year_var = IntVar(entry_frame)

#get the current month and year and set it to the intvar()
current_month = date.today().month
current_year = date.today().year
month_var.set(current_month)
year_var.set(current_year)

current_day = date.today()
print(current_day)


#setting the range of values for the month and year in the spinbox and specifying the current month and year it should hold
month_box = Spinbox(entry_frame,from_=1,to=12,width=10,command=showcalendar,textvariable=month_var,font=('ariel',12))
year_box = Spinbox(entry_frame,from_=0000,to=3000,width=10,command=showcalendar,textvariable=year_var,font=('ariel',12))

month_box.place(x=130,y=5)
year_box.place(x=360,y=5)

calendar_field = Text(result_frame,width=20,height=8,font=("courier",18),relief=RIDGE,borderwidth=2)
calendar_field.pack()

display_button = Button(button_frame,text="DISPLAY",bg="#A020F0",cursor='hand2',fg='#E0FFFF',font=("ariel",15),command=showcalendar)

reset_button = Button(button_frame,text="RESET",bg="#A020F0",cursor='hand2',fg='#E0FFFF',font=("ariel",15),command=reset)

close_button = Button(button_frame,text="CLOSE",bg="#A020F0",cursor='hand2',fg='#E0FFFF',font=("ariel",15),command=close)

display_button.place(x=55,y=0)
reset_button.place(x=210,y=0)
close_button.place(x=350,y=0)





root.mainloop()