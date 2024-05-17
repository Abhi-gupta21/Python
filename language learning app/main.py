BACKGROUND_COLOR = "#B1DDC6"
import tkinter
import pandas
import random
# ------------------------------ CARD WORDS SETUP ------------------------ #
new_word = {"French": "apelle", "English": "name"}
flip = 0
try:
    data_frame = pandas.read_csv("day 31 capstone/data/french_words_to_be_learnt.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv("day 31 capstone/data/french_words.csv")
    data_frame.to_csv("day 31 capstone/data/french_words_to_be_learnt.csv", index = False)
    data_frame = pandas.read_csv("day 31 capstone/data/french_words_to_be_learnt.csv")

data_list_of_dict = data_frame.to_dict(orient = "records")


def change_word_and_remove_word():
    global new_word
    global data_list_of_dict
    global data_frame
    global flip
    french_word_to_be_removed = new_word["French"]
    print(new_word["French"])
    english_word_to_be_removed = new_word["English"]
    print(new_word["English"])
    french_list = [i for i in data_frame["French"].to_list() if i != french_word_to_be_removed]
    english_list = [i for i in data_frame["English"].to_list() if i != english_word_to_be_removed]
    new_words_dict = {"French": french_list, "English": english_list}
    data_frame = pandas.DataFrame(new_words_dict)
    data_frame.to_csv("day 31 capstone/data/french_words_to_be_learnt.csv", index = False)
    data_list_of_dict = data_frame.to_dict(orient = "records")
    canvas.itemconfig(canvas_image, image = front_image)
    canvas.itemconfig(card_title_text, text = "French", fill = "black")
    new_word = random.choice(data_list_of_dict)
    canvas.itemconfig(card_word_text, text = new_word["French"], fill = 'black')
    flip = window.after(3000, flip_card)



def change_word_only():
    global new_word
    global data_list_of_dict
    canvas.itemconfig(canvas_image, image = front_image)
    canvas.itemconfig(card_title_text, text = "French", fill = "black")
    new_word = random.choice(data_list_of_dict)
    canvas.itemconfig(card_word_text, text = new_word["French"], fill = 'black')
    global flip
    flip = window.after(3000, flip_card)



def flip_card():
    canvas.itemconfig(canvas_image, image = back_image)
    canvas.itemconfig(card_title_text, text = "English", fill = "white")
    global new_word
    canvas.itemconfig(card_word_text, text = new_word["English"], fill = "white")
    window.after_cancel(flip)

# ----------------------------------------------- UI SETUP ------------------------------------------------ #

window = tkinter.Tk()
window.config(bg = BACKGROUND_COLOR)
window.config(padx = 50, pady = 50)

canvas = tkinter.Canvas(width = 800, height = 526, highlightthickness = 0, bg = BACKGROUND_COLOR)
front_image = tkinter.PhotoImage(file = "day 31 capstone/images/card_front.png")
back_image = tkinter.PhotoImage(file = "day 31 capstone/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image = front_image)
canvas.grid(row = 0, column = 0, columnspan = 2)

card_title_text = canvas.create_text(400, 150, text = "Title", font = ("Ariel", 40, "italic"))
card_word_text = canvas.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))

tick_image = tkinter.PhotoImage(file = "day 31 capstone/images/right.png")
right_button = tkinter.Button(image = tick_image, highlightthickness = 0, command = change_word_and_remove_word)
right_button.grid(row = 1, column = 0)

cross_image = tkinter.PhotoImage(file = "day 31 capstone/images/wrong.png")
wrong_button = tkinter.Button(image = cross_image, highlightthickness = 0, command = change_word_only)
wrong_button.grid(row = 1, column = 1)

window.mainloop()



