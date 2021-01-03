from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECKMARK = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    if reps % 2 != 0:
        work_sec = WORK_MIN * 60
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    elif reps != 7:
        short_break_sec = SHORT_BREAK_MIN * 60
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    else:
        long_break_min = LONG_BREAK_MIN * 60
        count_down(long_break_min)
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = int(count / 60)
    sec = int(count % 60)
    if minutes < 10:
        min_text = f"0{minutes}"
    else:
        min_text = f"{minutes}"
    if sec < 10:
        sec_text = f"0{sec}"
    else:
        sec_text = f"{sec}"
    canvas.itemconfig(timer_text, text=f"{min_text}:{sec_text}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark_label.config(text=(reps - 1) * CHECKMARK)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark_label.grid(column=1, row=3)

window.mainloop()
