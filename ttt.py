from tkinter import *
from tkinter import messagebox


main = Tk()
main.title('TIC TAC TO GAME')

gui = Frame(pady=70)
gui.configure(bg='black')
clicked = True
count = 0 

gui.pack()

def reset():
    global count
    count = 0
    
    b1["text"] = " "
    b2["text"] = " "
    b3["text"] = " "
    b4["text"] = " "
    b5["text"] = " "
    b6["text"] = " "
    b7["text"] = " "
    b8["text"] = " "
    b9["text"] = " "
        
def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player X Wins")
        reset()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player X Wins")
        reset()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player X Wins")
        reset()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player X Wins")
        reset()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player X Wins")
        reset()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player X Wins")
        reset()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player  X Wins")
        reset()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player X Wins")
        reset()

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player O Wins")
        reset()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player O Wins")
        reset()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player O Wins")
        reset()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player O Wins")
        reset()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player O Wins")
        reset()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player O Wins")
        reset()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player O Wins")
        reset()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        winner = True
        messagebox.showinfo("Tic Tac Toe","Congratulation! Player O Wins")
        reset()

def b_click(b):
    global clicked,count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe","Sorry, That box is already been selected\nPick Another box..")

    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe","Oops!, It's a Draw!")
        reset()


#button
b2 = Button(gui, text= " ",font=("Helvetica",20),height=3,width=6,command= lambda: b_click(b2),bg='#E9E8E8')
b3 = Button(gui, text= " ",font=("Helvetica",20),height=3,width=6,command= lambda: b_click(b3),bg='#E9E8E8')
b1 = Button(gui, text= " ",font=("Helvetica",20),height=3,width=6,command= lambda: b_click(b1),bg='#E9E8E8')
b4 = Button(gui, text= " ",font=("Helvetica",20),height=3,width=6,command= lambda: b_click(b4),bg='#E9E8E8')
b5 = Button(gui, text= " ",font=("Helvetica",20),height=3,width=6,command= lambda: b_click(b5),bg='#E9E8E8')
b6 = Button(gui, text= " ",font=("Helvetica",20),height=3,width=6,command= lambda: b_click(b6),bg='#E9E8E8')
b7 = Button(gui, text= " ",font=("Helvetica",20),height=3,width=6,command= lambda: b_click(b7),bg='#E9E8E8')
b8 = Button(gui, text= " ",font=("Helvetica",20),height=3,width=6,command= lambda: b_click(b8),bg='#E9E8E8')
b9 = Button(gui, text= " ",font=("Helvetica",20),height=3,width=6,command= lambda: b_click(b9),bg='#E9E8E8')
#grid
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)


main.mainloop()
