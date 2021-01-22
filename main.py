from tkinter import *
import random

window=Tk()
window.title("Rock-Paper-Scissor")
window.geometry("550x200")
window.resizable(False,False)

def rock(choice):
    global uscore,cscore
    c_choice=computer_choice()
    result=""
    if c_choice == 'scissor':
        result='YOU WIN!!!!'
        uscore+=1
    elif c_choice == 'paper':
        result='YOU LOSS'
        cscore+=1
    else:
        result='TIE'

    final_result(choice,c_choice,result)

def paper(choice):
    global uscore, cscore
    c_choice=computer_choice()
    result=""
    if c_choice == 'rock':
        result='YOU WIN!!!!'
        uscore += 1
    elif c_choice == 'scissor':
        result='YOU LOSS'
        cscore += 1
    else:
        result='TIE'

    final_result(choice,c_choice,result)

def scissor(choice):
    global uscore, cscore
    c_choice=computer_choice()
    result=""
    if c_choice == 'paper':
        result='YOU WIN!!!!'
        uscore += 1
    elif c_choice == 'rock':
        result='YOU LOSS'
        cscore += 1
    else:
        result='TIE'

    final_result(choice,c_choice,result)


def computer_choice():
    com_choice=random.choice(['rock', 'paper', 'scissor'])
    return com_choice


def final_result(choice,c_choice,result):
    ur_text.set(choice.upper())
    com_text.set(c_choice.upper())
    result_text.set(result)
    u_score.set(uscore)
    cm_score.set(cscore)

ur_text=StringVar()
com_text=StringVar()
result_text=StringVar()
u_score=StringVar()
cm_score=StringVar()
uscore=cscore=0

input_frame = Frame(window)
input_frame.grid(row = 0, column = 0, rowspan = 3, columnspan = 2)

result_frame = Frame(window, background='black')
result_frame.grid(row = 0, column = 2, rowspan = 6, columnspan = 4)

score_frame = Frame(window)
score_frame.grid(row = 5, column = 0, rowspan = 3, columnspan = 2)

button_rock=Button(input_frame, text = "ROCK", fg = "blue",font='bold', width = 10, height = 1, bd = 2,bg='pink', cursor = "hand2", command = lambda :rock('rock'))
button_rock.pack(pady=1)

button_paper=Button(input_frame, text = "PAPER", fg = "blue",font='bold', width = 10, height = 1, bd = 2, bg = "pink", cursor = "hand2", command = lambda :paper('paper'))
button_paper.pack(pady=1)

button_scissor=Button(input_frame, text = "SCISSOR", fg = "blue",font='bold', width = 10, height = 1, bd = 2, bg = "pink", cursor = "hand2", command = lambda :scissor('scissor'))
button_scissor.pack(pady=1)

label_you=Label(result_frame, text='YOU',fg='yellow',font='bold', width=15, height=2,bg='black')
label_you.grid(row=0,column=0,pady=5)

label_user=Label(result_frame, textvariable=ur_text,fg='red',font='bold', width=15, height=2,bg='black')
label_user.grid(row=0,column=1,pady=5)

label_com=Label(result_frame, text='COMPUTER',fg='yellow', font='bold', width=15, height=2,bg='black')
label_com.grid(row=1,column=0)

label_comp=Label(result_frame, textvariable=com_text,fg='red',font='bold', width=15, height=2,bg='black')
label_comp.grid(row=1,column=1,pady=5)

label_result=Label(result_frame, textvariable=result_text,fg='green',font=('bold', 20), width=15, height=2,bg='black')
label_result.grid(row=2,column=0,columnspan=3, rowspan=2, pady=5)

ur_score=Label(score_frame, text='Your Score',fg='black',font='bold', width=15, height=1)
ur_score.grid(row=0,column=0,pady=1)

score_ur=Label(score_frame, textvariable=u_score,fg='blue',font='bold', width=10, height=1)
score_ur.grid(row=0,column=1,pady=1)

com_score=Label(score_frame, text='Computer Score',fg='black',font='bold', width=15, height=1)
com_score.grid(row=1,column=0,pady=1)

c_score=Label(score_frame, textvariable=cm_score,fg='blue',font='bold', width=10, height=1)
c_score.grid(row=1,column=1,pady=1)

window.mainloop()