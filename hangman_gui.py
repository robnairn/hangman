from tkinter import *
from string import ascii_uppercase
from tkinter import messagebox
import random

window = Tk()
window.title('Hangman')

images = [PhotoImage(file='hangman.png'), PhotoImage(file='image1.png'), PhotoImage(file='image2.png'), PhotoImage(file='image3.png'), PhotoImage(file='image4.png'), PhotoImage(file='image5.png'), PhotoImage(file='image6.png'), PhotoImage(file='image7.png'), PhotoImage(file='image8.png'), PhotoImage(file='image9.png'), PhotoImage(file='image10.png')]

word_list = ['BAT', 'GIRAFFE', 'WILLING', 'OVERJOYED', 'TORPID', 'ROTTEN', 'TREMENDOUS', 'HUMDRUM', 'COLOUR', 'UNSUITABLE', 'CYCLE', 'GUESS', 'BOW', 'WASTE', 'DISCREET', 'STICKS', 'THREAD', 'SHADE', 'BURY', 'INCOMPETENT', 'NOISE', 'BORDER', 'GARRULOUS', 'LEVEL', 'MACHO', 'VIGOROUS', 'MIND', 'MASS', 'COUNTRY', 'POWER']


def new_game():
    global word_spaces
    global number_of_guesses
    number_of_guesses = 0
    label_image.config(image=images[0])
    the_word = random.choice(word_list)
    word_spaces = ' '.join(the_word)
    label_word.set(' '.join('_' * len(the_word)))

def guess(letter):
    global number_of_guesses
    if number_of_guesses < 10:
        txt = list(word_spaces)
        guessed = list(label_word.get())
        if word_spaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                    label_word.set(''.join(guessed))
            if label_word.get() == word_spaces:
                    messagebox.showinfo('Hangman','You guessed it!')
        else:
            number_of_guesses += 1
            label_image.config(image = images[number_of_guesses])
            if number_of_guesses == 10:
                messagebox.showwarning('Hangman','Game Over')

# word row 0
label_word = StringVar()
Label(window, textvariable=label_word, font=('Helvetica 24 bold')).grid(row=0, column=0, columnspan=7, padx=10)

# image row 1
label_image = Label(window)
label_image.grid(row=1, column=0, columnspan=7, padx=10, pady=30)

# keyboard
n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=('Helvetica 18'), width=4).grid(row=2+n//7, column=n%7)
    n += 1
Button(window, text='New Game', command=new_game, font=('Helvetica 18'), width=9).grid(row=5, column=5, columnspan=2)

new_game()
window.mainloop()