import characters as c
import battle as b
from tkinter import *

root = Tk()
root.geometry("700x1000")
root.title("Animal Battle")

# create text widget to display battle results
text_widget = Text(root, wrap=WORD, height=40)
text_widget.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
text_widget.config(state=DISABLED)


def start_battle(char_1, char_1_strength, char_2, char_2_strength):
    character1 = c.Cat(char_1, char_1_strength, 100)
    character2 = c.Cat(char_2, char_2_strength, 100)
    results = b.battle(character1, character2)

    text_widget.config(state=NORMAL)
    for message in results:
        print(message)
        text_widget.insert(END, message)
        text_widget.see(END)  # Scroll to the end of Text widget

    text_widget.config(state=DISABLED)


# Create Entry widgets for player names and strengths
Label(root, text="Player 1 Name:").grid(row=0, column=0, padx=10, pady=5)
player_1_name = Entry(root, width=20)
player_1_name.grid(row=0, column=1, padx=10, pady=5)
Label(root, text="Player 1 Strength:").grid(row=1, column=0, padx=10, pady=5)
player_1_strength = Entry(root, width=20)
player_1_strength.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Player 2 Name:").grid(row=0, column=2, padx=10, pady=5)
player_2_name = Entry(root, width=20)
player_2_name.grid(row=0, column=3, padx=10, pady=5)
Label(root, text="Player 2 Strength:").grid(row=1, column=2, padx=10, pady=5)
player_2_strength = Entry(root, width=20)
player_2_strength.grid(row=1, column=3, padx=10, pady=5)


# add button to start battle and open window
button = Button(root,
                text="Begin Battle!",
                fg="blue",
                command=lambda: start_battle(player_1_name.get(), int(player_1_strength.get()), player_2_name.get(),
                                             int(player_2_strength.get())))
button.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

root.mainloop()
