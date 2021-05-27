from tkinter import *

root = Tk()
logo = PhotoImage(file="img.png")
root.overrideredirect(1)
root.configure(bg="#0a1931")
ws = root.winfo_screenwidth()
x = int((ws / 2) - (1350 / 2))
root.resizable(False, False)
root.geometry(f"1180x760+{x}+0")
root.title('Criss Cross')
Tops = Frame(root, bg="#0a1931", pady=2, width=1180, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)
Gametitle = Label(Tops, bg="#0a1931", image=logo, justify=CENTER, cursor="cross")
Gametitle.grid(row=0, column=0)
MainFrame = Frame(root, bg="#0a1931", bd=10, width=1180, height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)
LeftFrame = Frame(MainFrame, bg="#0a1931", bd=10, width=750, height=500, relief=RIDGE, pady=2, padx=10, cursor="pirate")
LeftFrame.pack(side=LEFT)
RightFrame = Frame(MainFrame, bg="#0a1931", bd=10, width=560, height=500, relief=RIDGE, pady=2, padx=10)
RightFrame.pack(side=RIGHT)
RightFrame1 = Frame(RightFrame, bg="#0a1931", bd=10, width=560, height=200, relief=RIDGE, pady=2, padx=10)
RightFrame1.grid(row=0, column=0)
RightFrame2 = Frame(RightFrame, bg="#0a1931", bd=10, width=560, height=200, relief=RIDGE, pady=2, padx=10)
RightFrame2.grid(row=1, column=0, sticky=NSEW)
Gamestate = Label()
cells = []
button1 = button2 = button3 = button4 = button5 = button6 = button7 = button8 = button9 = Button()


def states():
    return [button1["text"], button2["text"], button3["text"],
            button4["text"], button5["text"], button6["text"],
            button7["text"], button8["text"], button9["text"]]


def result(chance):
    x_o = "".join(chance)
    win = [x_o[:3], x_o[3:6], x_o[6:], x_o[2:8:2], x_o[::4], x_o[::3], x_o[1::3], x_o[2::3]]
    if "XXX" in win:
        return -1
    elif "OOO" in win:
        return 1
    elif "_" not in chance:
        return 0
    else:
        return 2


def minimax(current, ismaximizing, grid):
    state = result(grid)
    if state < 2:
        return state
    bot = "O" if current == "X" else "X"
    bestscore = float('-inf') if ismaximizing else float('inf')
    for n, cell in enumerate(grid):
        if cell == "_":
            grid[n] = current
            score = minimax(bot, not ismaximizing, grid)
            grid[n] = "_"
            bestscore = max(score, bestscore) if ismaximizing else min(score, bestscore)
    return bestscore


def ai_play():
    global cells, button1, button2, button3, button4, button5, button6, button7, button8, button9
    cells = states()
    cells = ['_' if cell == " " else cell for cell in cells]
    bestscore = float('-inf')
    move = 0
    for n, cell in enumerate(cells):
        if cell == "_":
            cells[n] = "O"
            score = minimax('X', False, cells)
            cells[n] = "_"
            if score > bestscore:
                bestscore = score
                move = n
    btn = globals()[f"button{move + 1}"]
    checker(btn, False)


def enable():
    for child in LeftFrame.winfo_children():
        if child['text'] == " ":
            child["state"] = NORMAL


def disable():
    for child in LeftFrame.winfo_children():
        child["state"] = DISABLED


def checker(button, click):
    if click:
        button["text"] = 'X'
        Gamestate["text"] = "Thinking!"
        if not checkWin():
            disable()
            root.after(1000, ai_play)
    else:
        button["text"] = "O"
        enable()
        Gamestate["text"] = "Your Turn!"
    button["relief"] = SUNKEN
    button["state"] = DISABLED
    checkWin()


def play():
    global Gamestate, button1, button2, button3, button4, button5, button6, button7, button8, button9
    button1 = Button(LeftFrame, text=" ", font=("Comic Sans MS", 26, 'bold'), height=3, width=8, bg='#e7e7de',
                     command=lambda: checker(button1, True), relief=GROOVE, fg="#0a1931", disabledforeground="#0a1931")
    button1.grid(row=1, column=0, sticky=NSEW)
    button2 = Button(LeftFrame, text=" ", font=("Comic Sans MS", 26, 'bold'), height=3, width=8, bg='#e7e7de',
                     command=lambda: checker(button2, True), relief=GROOVE, fg="#0a1931", disabledforeground="#0a1931")
    button2.grid(row=1, column=1, sticky=NSEW)
    button3 = Button(LeftFrame, text=" ", font=("Comic Sans MS", 26, 'bold'), height=3, width=8, bg='#e7e7de',
                     command=lambda: checker(button3, True), relief=GROOVE, fg="#0a1931", disabledforeground="#0a1931")
    button3.grid(row=1, column=2, sticky=NSEW)
    button4 = Button(LeftFrame, text=" ", font=("Comic Sans MS", 26, 'bold'), height=3, width=8, bg='#e7e7de',
                     command=lambda: checker(button4, True), relief=GROOVE, fg="#0a1931", disabledforeground="#0a1931")
    button4.grid(row=2, column=0, sticky=NSEW)
    button5 = Button(LeftFrame, text=" ", font=("Comic Sans MS", 26, 'bold'), height=3, width=8, bg='#e7e7de',
                     command=lambda: checker(button5, True), relief=GROOVE, fg="#0a1931", disabledforeground="#0a1931")
    button5.grid(row=2, column=1, sticky=NSEW)
    button6 = Button(LeftFrame, text=" ", font=("Comic Sans MS", 26, 'bold'), height=3, width=8, bg='#e7e7de',
                     command=lambda: checker(button6, True), relief=GROOVE, fg="#0a1931", disabledforeground="#0a1931")
    button6.grid(row=2, column=2, sticky=NSEW)
    button7 = Button(LeftFrame, text=" ", font=("Comic Sans MS", 26, 'bold'), height=3, width=8, bg='#e7e7de',
                     command=lambda: checker(button7, True), relief=GROOVE, fg="#0a1931", disabledforeground="#0a1931")
    button7.grid(row=3, column=0, sticky=NSEW)
    button8 = Button(LeftFrame, text=" ", font=("Comic Sans MS", 26, 'bold'), height=3, width=8, bg='#e7e7de',
                     command=lambda: checker(button8, True), relief=GROOVE, fg="#0a1931", disabledforeground="#0a1931")
    button8.grid(row=3, column=1, sticky=NSEW)
    button9 = Button(LeftFrame, text=" ", font=("Comic Sans MS", 26, 'bold'), height=3, width=8, bg='#e7e7de',
                     command=lambda: checker(button9, True), relief=GROOVE, fg="#0a1931", disabledforeground="#0a1931")
    button9.grid(row=3, column=2, sticky=NSEW)
    Gamestate = Label(RightFrame1, font=("Comic Sans MS", 70, 'italic'), text="Your Turn!", width=8, bd=21,
                      bg="#0a1931",
                      fg="#dddddd",
                      justify=CENTER, cursor="spraycan")
    Gamestate.grid(row=0, column=0)


new_game = Button(RightFrame2, text="New Game", font=("Comic Sans MS", 23, 'italic'), height=3, width=26, bg='#e7e7de',
                  fg="#0a1931", cursor="exchange", command=play)
new_game.grid(row=0, column=0, sticky=NSEW)
close = Button(RightFrame2, text="Exit", height=3, width=26, font=("Comic Sans MS", 23, 'italic'), bg='#e7e7de',
               command=root.destroy, cursor="shuttle", fg="#0a1931")
close.grid(row=1, column=0, sticky=NSEW)


def checkWin():
    end = False
    state = [button1["text"], button2["text"], button3["text"], button4["text"], button5["text"], button6["text"],
             button7["text"], button8["text"], button9["text"]]
    if state[0] == 'X' and state[1] == 'X' and state[2] == 'X':
        end = True
        button1["bg"] = button2["bg"] = button3["bg"] = "#edeef7"
        Gamestate["text"] = "You won!"
    elif state[3] == 'X' and state[4] == 'X' and state[5] == 'X':
        button4["bg"] = button5["bg"] = button6["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "You won!"
    elif state[6] == 'X' and state[7] == 'X' and state[8] == 'X':
        button7["bg"] = button8["bg"] = button9["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "You won!"
    elif state[0] == 'X' and state[3] == 'X' and state[6] == 'X':
        button1["bg"] = button4["bg"] = button7["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "You won!"
    elif state[1] == 'X' and state[4] == 'X' and state[7] == 'X':
        button2["bg"] = button5["bg"] = button8["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "You won!"
    elif state[2] == 'X' and state[5] == 'X' and state[8] == 'X':
        button3["bg"] = button6["bg"] = button9["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "You won!"
    elif state[0] == 'X' and state[4] == 'X' and state[8] == 'X':
        button1["bg"] = button5["bg"] = button9["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "You won!"
    elif state[2] == 'X' and state[4] == 'X' and state[6] == 'X':
        button3["bg"] = button5["bg"] = button7["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "You won!"
    elif state[0] == 'O' and state[1] == 'O' and state[2] == 'O':
        end = True
        button1["bg"] = button2["bg"] = button3["bg"] = "#edeef7"
        Gamestate["text"] = "I won!"
    elif state[3] == 'O' and state[4] == 'O' and state[5] == 'O':
        button4["bg"] = button5["bg"] = button6["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "I won!"
    elif state[6] == 'O' and state[7] == 'O' and state[8] == 'O':
        button7["bg"] = button8["bg"] = button9["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "I won!"
    elif state[0] == 'O' and state[3] == 'O' and state[6] == 'O':
        button1["bg"] = button4["bg"] = button7["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "I won!"
    elif state[1] == 'O' and state[4] == 'O' and state[7] == 'O':
        button2["bg"] = button5["bg"] = button8["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "I won!"
    elif state[2] == 'O' and state[5] == 'O' and state[8] == 'O':
        button3["bg"] = button6["bg"] = button9["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "I won!"
    elif state[0] == 'O' and state[4] == 'O' and state[8] == 'O':
        button1["bg"] = button5["bg"] = button9["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "I won!"
    elif state[2] == 'O' and state[4] == 'O' and state[6] == 'O':
        button3["bg"] = button5["bg"] = button7["bg"] = "#edeef7"
        end = True
        Gamestate["text"] = "I won!"
    elif state[0] in "XO" and state[1] in "XO" and state[2] in "XO" and state[3] in "XO" and \
            state[4] in "XO" and state[5] in "XO" and state[6] in "XO" and \
            state[7] in "XO" and state[8] in "XO":
        button1["bg"] = button2["bg"] = button3["bg"] = button4["bg"] = button5["bg"] = button6["bg"] = button7["bg"] = \
            button8["bg"] = button9["bg"] = "#edeef7"
        Gamestate["text"] = "Draw!"
        end = True
    if end:
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        button4["state"] = DISABLED
        button5["state"] = DISABLED
        button6["state"] = DISABLED
        button7["state"] = DISABLED
        button8["state"] = DISABLED
        button9["state"] = DISABLED
    return end


play()
root.mainloop()
