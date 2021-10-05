import os
import io
import pygame
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from gtts import gTTS
from googletrans import Translator

class Translation(object):
    def __init__(self, master):
       frame = Frame(master)
       frame.grid()
       tabControl = ttk.Notebook(root)
       tabControl.configure(width = 340, height = 200)

       self.translate_tab = ttk.Frame(tabControl)
       tabControl.add(self.translate_tab, text = "Translate")
       tabControl.grid()
       self.translate_tab.grid_propagate(0)

       self.about_tab = ttk.Frame(tabControl)
       tabControl.add(self.about_tab, text = "About")
       tabControl.grid()

       self.speak_it = BooleanVar()
       self.languages = {
           'Arabic': 'ar', 'Belarussian': 'be', 'Bulgarian': 'bg', 'Bosnian': 'bs',
           'Czech': 'cs', 'Danish': 'da', 'German': 'de', 'Greek': 'el', 
           'English': 'en', 'Spanish': 'es', 'Persian': 'fa', 'Finnish': 'fi', 
           'French': 'fr', 'Irish': 'ga', 'Hebrew': 'he', 'Hindi': 'hi', 
           'Croatian': 'hr', 'Haitian': 'ht', 'Hungarian': 'hu', 'Armenian': 'hy',
           'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Korean': 'ko',
           'Kurdish': 'ku', 'Latin': 'la', 'Lithuanian': 'lt', 'Latvian': 'lv',
           'Dutch': 'nl', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt',
           'Romanian': 'ro', 'Russian': 'ru', 'Somalia': 'so', 'Albanian': 'sq',
           'Serbian': 'sr', 'Swedish': 'sv', 'Swahili': 'sw', 'Turkish': 'tr',
           'Vietnamise': 'vi'}
       self.translate_page()
       self.about_page()

    def translate_page(self):
        self.top_label = Label(self.translate_tab, text = "Enter Text:")
        self.top_label.grid(column = 0, row = 0)
        self.word_entry = Entry(self.translate_tab, witdh = 48)
        self.word_entry.grid(column = 0, row = 1, columnspan = 3, padx = 5, pady = 5)

        self.language_label = Label(self.translate_tab, text = "Language: ")
        self.language_label.grid(column = 0, row = 2, pady = 5)
        self.language_menu = ttk.Combobox(self.translate_tab, values = [*self.languages.keys()])
        self.language_menu.grid(column = 1, row = 2)
        self.language_menu.current(0)

        self.translat_button = Button(self.translate_tab, text = "Translate!", command = self.translation)
        self.translat_button.grid(column = 0, row = 3, pady = 15)
        self.speak_check = Checkbutton(self.translate_tab, text = "Say it!", variable = self.speak_it)
        self.speak_check.grid(column = 1, row = 3)

        self.word_frame = LabelFrame(self.translate_tab, text = "Translation:", width = 300, height = 50)
        self.word_frame.grid(column = 0, row = 4, columnspan = 3)
        self.word_frame.grid_propagate(0)
        self.word_result = Label(self.word_frame, text = "")
        self.word_result.grid()
    
    def about_page(self):
        pass

    def translation(self):
        trans = Translator()
        word = self.word_entry.get()
        lang = str(self.languages.get(self.language_menu.get()))
        result = str(trans.translate(word, dest = lang).text)
        self.word_result.configure(text = result)
        if self.speak_it.get():
            with io.BytesIO() as file:
                gTTS(text = result, lang = "en").write_to_fp(file)
                file.seek(0)
                pygame.mixer.init()
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    continue

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    root = Tk()
    root.title("Translator")
    root.geometry("350x230")
    root.iconbitmap("icon.ico")
    Translation(root)
    root.mainloop()
