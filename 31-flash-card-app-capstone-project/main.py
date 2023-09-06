import tkinter
import random
import pandas

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

try: 
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

random_word = {}
flip_timer = None

# ---------------------------- FLASH CARD ------------------------------- #
def next_card():
    """ take the word from the csv file and display it on the canvas """
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word["French"], fill="black")
    flip_timer = window.after(3000, flip_card)

def is_known():
    """ remove the word from the csv file and display the next word """
    global random_word
    to_learn.remove(random_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    """ flip the card to display the english translation """
    global random_word, flip_timer
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=random_word["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"),fill="black")
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tkinter.PhotoImage(file="images/wrong.png")
unknown_button = tkinter.Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)


check_image = tkinter.PhotoImage(file="images/right.png")
known_button = tkinter.Button(image=check_image, highlightthickness=0, command=is_known)

known_button.grid(row=1, column=1)

next_card()

window.mainloop()