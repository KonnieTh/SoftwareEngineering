from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk, Image

root = Tk()
root.geometry("700x500")
root.configure(bg='#4DEFA4')
#images
img = (Image.open("img.png"))
resizedImg = img.resize((150,150))
newImg = ImageTk.PhotoImage(resizedImg)

searchicon = (Image.open("download.png"))
searchicon = ImageTk.PhotoImage(searchicon)

medal=(Image.open("new_medal.png"))
#resizedmedal = medal.resize((80,50))
newMedal = ImageTk.PhotoImage(medal)

#labels
profile = Label(root, text="Profile", font=20,fg='#090A76',bg='#4DEFA4' )
imageProfile = Label(root, image=newImg)
imageMedal = Label(root, image=newMedal)
username = Label(root, text="username:.....", font= 20,fg='#090A76',bg='#4DEFA4')
searchText = Label(root,text="Search for players",fg='#090A76',bg='#4DEFA4')

#buttons
friendsButton = Button(root,text="Friends",bg='#090A76', fg='white')
trophiesButton = Button(root,text="Trophies",bg='#090A76',fg='white')
friendsButton.config(height=1,width=10)
trophiesButton.config(height=1,width=10)

backButton = Button(root,text="Back",bg='#4DEFA4',fg='#090A76',highlightbackground='#090A76',highlightthickness = 2, bd=2)
backButton.config(height=1,width=8)

searchButton = Button(root)
searchButton.config(height=1,width=2)
searchbar = Entry(root,width= 30,fg='#090A76')

#renders
profile.place(relx=0.5,rely=0.05, anchor=CENTER)
imageProfile.place(relx=0.5,rely=0.22, anchor=CENTER)
imageMedal.place(x=250, y=30)
username.place(relx=0.5,rely=0.4, anchor=CENTER)
friendsButton.place(relx=0.5,rely=0.48, anchor=CENTER)
trophiesButton.place(relx=0.5,rely=0.55, anchor=CENTER)
backButton.place(x=10,y=465)
searchText.place(relx= 0.8, rely= 0.05, anchor=E)
searchbar.place(relx=0.92, y=50, anchor=E)
searchButton.place(x=460, y=50,anchor=E)
root.mainloop()