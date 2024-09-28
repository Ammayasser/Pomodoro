from tkinter import *
import math

# ---------------------------CONSTANTS--------------------------------#
PINK = "#e2979C"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_NIN = 25
SHORT_BREAK = 5
LONG_BREAK_MIN = 20
reps = 0
basic_timer = None


#  ----------------------------------- TIMER MECHANISM ------------------------------  #


def reset_timer():
    window.after_cancel(basic_timer)
    timer_text_label.config(text="Timer")
    canvas.itemconfig(timer, text="00:00")
    global reps
    reps = 0


#  ----------------------------------- TIMER RESET ---------------------------------  #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_NIN * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_text_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_text_label.config(text="Work Time", fg=GREEN)


#  ----------------------------------- COUNTDOWN MECHANISM ------------------------------  #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")

    if count > 0:
        global basic_timer
        basic_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark_label.config(text="✔")


#  ---------------------------------- UP SETUP ------------------------------------  #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)

canvas = Canvas(width=512, height=512, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(260, 255, image=tomato_img)
timer = canvas.create_text(260, 260, text="00:00", fill="black", font=(FONT_NAME, 40, "bold"))
canvas.grid(row=1, column=1)
timer_text_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, "40", "bold"))
timer_text_label.grid(row=0, column=1)

check_mark_label = Label(fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=2, column=1)
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, padx=5, pady=3, command=reset_timer)
reset_button.grid(row=2, column=0)
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, padx=5, pady=3, command=start_timer)
start_button.grid(row=2, column=2)
window.mainloop()
