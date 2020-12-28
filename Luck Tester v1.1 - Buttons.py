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
    
col_label = tkinter.Label(luck,text='Choose Background Color ')
col_label.pack()

def blue():
    luck.configure(bg='blue')
def yellow():
    luck.configure(bg='yellow')
def red():
    luck.configure(bg='red')    
def green():
    luck.configure(bg='green') 
def black():
    luck.configure(bg='black')     
    
blue_button = tkinter.Button(luck,text ='Blue', command=blue)  
blue_button.pack()

yellow_button = tkinter.Button(luck,text='Yellow', command=yellow)  
yellow_button.pack()

red_button = tkinter.Button(luck,text='Red', command=red)  
red_button.pack()

green_button = tkinter.Button(luck,text='Green', command=green)  
green_button.pack()

black_button = tkinter.Button(luck,text='Black', command=black)  
black_button.pack()

myLabel = tkinter.Label(luck,text='\n\nCheck Your Luck for the Day!!')
myLabel.pack()

myButton = tkinter.Button(luck,text='Test Your Luck',command=LuckGen)
myButton.pack()

luck.mainloop()
