import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text = "Timer")
    check_mark.config(text = "")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_countdown_timer():
    global reps
    reps = reps + 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text = "Break", fg = RED)
    elif reps%2 == 1:
        count_down(work_sec)
        timer_label.config(text = "Work", fg = GREEN)
    else:
        count_down(short_break_sec)
        timer_label.config(text = "Break", fg = PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min = int(count/60)
    sec = count % 60
    
    if sec < 10:
        sec = "0" + str(sec)
    canvas.itemconfig(timer_text, text = str(min) + ":" + str(sec))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_countdown_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_mark.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("POMODORO")
window.config(padx = 100, pady = 50, bg = YELLOW)



canvas = tkinter.Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = tkinter.PhotoImage(file = "day 28 (project)/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 132, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)



timer_label = tkinter.Label(text = "Timer", font = (FONT_NAME, 45, "bold"), fg = GREEN, bg = YELLOW, highlightthickness = 0)
timer_label.grid(row = 0, column = 1)

start_button = tkinter.Button(text = "Start", command = start_countdown_timer)
start_button.grid(row = 2, column = 0)

reset_button = tkinter.Button(text = "Reset", command = reset_timer)
reset_button.grid(row = 2, column = 2)

check_mark = tkinter.Label(text = "", fg = GREEN, bg = YELLOW, highlightthickness = 0)
check_mark.grid(row = 3, column = 1)





window.mainloop()