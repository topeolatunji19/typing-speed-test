import random
import time
from tkinter import *
from tkinter import messagebox
import threading

generated_text = "man boy and dog cat movie joke allow turn baby adult teenager commit change moose then crude merit " \
                  "can ate an burger enemy friend court peace chest burn tune churn crave bing pong your come ape " \
                  "leap crowd muse rabbit frog complex audit pringle ping down bad good slap punch kick toad hobbit " \
                  "hot spot internet kids land play state box timmy fred amy apple juice orange camel toe sheep goat " \
                 "miami beach front back"
sample_text_list = generated_text.split()


# Function to get the sample words for the user to type
def get_words():
    # To randomly rearrange the words to be typed
    shuffled_words = random.sample(sample_text_list, len(sample_text_list))
    final_words = "  ".join(shuffled_words)
    words_to_type.delete("1.0", "end")
    words_to_type.insert(INSERT, final_words)


# Timer
def countdown(*args):
    time.sleep(60)
    count_words()


# Get words
def count_words():
    user_text = text_entry_box.get(1.0, "end-1c")
    user_text_list = user_text.split()
    correct_words = [word for word in user_text_list if word in sample_text_list]
    score = len(correct_words)
    is_ok = messagebox.askokcancel(title="Speed Test", message=f"Time Up!\nYour typing speed is "
                                                               f"{score} wpm 'words per minute'\n"
                                                               f"Do you want to restart test?")
    if is_ok:
        text_entry_box.delete("1.0", "end")
        get_words()
        text_entry_box.bind("<Key>", threading.Thread(target=countdown).start())
    else:
        text_entry_box.delete("1.0", "end")
        messagebox.showinfo(title="Score", message=f"Your final typing speed is {score} wpm 'words per minute'")

# --------------------------------- GUI Configuration ------------------------------------#


window = Tk()
window.title("Typing Speed Test")
window.minsize(width=400, height=500)

words_to_type_label = Label(window, text="Click 'GET WORDS' to get the words to type and "
                                         "enter those words below in the space provided below")
words_to_type_label.grid(row=1, column=1)

words_to_type = Text(height=10, width=42, wrap="word")
words_to_type.grid(row=2, column=1)
words_to_type.configure(font=("Arial", 20, "bold"))

get_words_button = Button(window, text="GET WORDS", command=get_words)
get_words_button.grid(row=3, column=1)

text_entry_label = Label(window, text="Enter the words above in the box below with 60 seconds. "
                                      "Start typing in the box to begin the timer.")
text_entry_label.grid(row=4, column=1)

text_entry_box = Text(height=10, width=53, wrap="word")
text_entry_box.grid(row=5, column=1)

# Binding to ensure the countdown function is called immediately any key is called within the text_entry_box widget
# The threading class is used to ensure that the countdown timer runs in the background and
# the program does not freeze for the countdown period.
text_entry_box.bind("<Key>", threading.Thread(target=countdown).start())

window.mainloop()
