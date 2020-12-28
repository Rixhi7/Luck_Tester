import tkinter
import random
luck=tkinter.Tk()
luck.title('Luck Tester')       
luck.geometry('400x400')        #for window size

#Function to generate and print Luck
def LuckGen():                  
    r=random.randint(1,10)
    s=''
    if r<3:
        s= 'Take Care'
    if r>7:
        s='Today\'s your day!!'        
    lucklabel= tkinter.Label(luck,text='Luck = '+str(r)+'\n'+s)
    lucklabel.pack()


#Function to assign bg color of the app
def color():
    col = col_text.get()
    luck.configure(bg=col)

    
col_label = tkinter.Label(luck,text='Enter Background Color ')
col_label.pack()

col_text = tkinter.Entry(luck,width=30)
col_text.pack()

col_button = tkinter.Button(luck,text='Submit', command=color)
col_button.pack()

myLabel = tkinter.Label(luck,text='\n\nCheck Your Luck for the Day!!')
myLabel.pack()

myButton = tkinter.Button(luck,text='Test Your Luck',command=LuckGen)
myButton.pack()


luck.mainloop()
