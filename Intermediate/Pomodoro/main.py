from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfigure(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 2 != 0:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count/60)
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
      
    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
title_label.grid(row=0, column=1)

check_label = Label(fg=GREEN, bg=YELLOW,font=(FONT_NAME, 20))
check_label.grid(row=3, column=1)

start_button = Button(text= "Start", command=start_timer, highlightbackground= YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text= "Reset", command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Intermediate/Pomodoro/tomato.png")
canvas.create_image(100,112, image=tomato_img)

timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"), )
canvas.grid(row=1, column=1)

window.mainloop()