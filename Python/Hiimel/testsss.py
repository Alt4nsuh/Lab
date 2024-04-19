import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import nltk
import re
nltk.download('words')
from nltk.corpus import words as nltk_words


class SpellingChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")
        self.text = ScrolledText(self.root, font=("Arial", 14))
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack(expand=True, fill='both')
        self.old_spaces = 0
        self.english_words = set(nltk_words.words())
        self.a =[]

        self.suggestions_label = tk.Label(self.root, text="", anchor='w', justify='left', wraplength=600)
        self.suggestions_label.pack(side='bottom', fill='x', padx=10, pady=5)

        self.check_button = tk.Button(self.root, text="Check Spelling", command=self.manual_spell_check)
        self.check_button.pack(side='bottom', pady=5)

        self.root.mainloop()

    def check(self, event):
        content = self.text.get("1.0", tk.END)
        space_count = content.count(" ")
        if space_count != self.old_spaces:
            self.old_spaces = space_count

            for tag in self.text.tag_names():
                self.text.tag_delete(tag)

            for word in content.split(" "):
                if re.sub(r"[^\w]", "", word.lower()) not in self.english_words:
                    position = content.find(word)
                    self.text.tag_add("misspelled", f"1.{position}", f"1.{position + len(word)}")
                    self.text.tag_config("misspelled", foreground="red")
                    self.a.append(word)  

    def manual_spell_check(self):
        content = self.text.get("1.0", tk.END)
        words_to_check = re.findall(r'\b\w+\b', content)
        suggestions = []
        for word in words_to_check:
            if word.lower()  in self.a:
                suggestions.extend(self.spell_check(word))
                
        if suggestions:
            top_suggestions = ", ".join(word for word, _ in suggestions)
            self.suggestions_label.config(text=f"Suggestions for misspelled words:\n{top_suggestions}")
        else:
          self.suggestions_label.config(text=f"buruu ug alga")
    def wagner_fischer(self, s1, s2):
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            s1, s2 = s2, s1
            len_s1, len_s2 = len_s2, len_s1
        
        current_row = range(len_s1 + 1)
        for i in range(1, len_s2 + 1):
            previous_row, current_row = current_row, [i] + [0] * len_s1
            for j in range(1, len_s1 + 1):
                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                if s1[j - 1] != s2[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)

        return current_row[len_s1]

    def spell_check(self, word):
        suggestions = []

        for correct_word in self.english_words:
            distance = self.wagner_fischer(word, correct_word)
            suggestions.append((correct_word, distance))

        suggestions.sort(key=lambda x: x[1])
        return suggestions[:5]


if __name__ == "__main__":
    SpellingChecker()
