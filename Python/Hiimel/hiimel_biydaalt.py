import tkinter as tk
from tkinter.scrolledtext import ScrolledText
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
        self.english_words = set(nltk_words.words())
        self.misspelled_words = {}

        self.check_button = tk.Button(self.root, text="Check Spelling", command=self.manual_spell_check)
        self.check_button.pack(side='bottom', pady=5)

        self.suggestion_buttons = []
        self.root.mainloop()

    def clear_suggestion_buttons(self):
        for button in self.suggestion_buttons:
            button.destroy()
        self.suggestion_buttons = []

    def check(self, event):
        content = self.text.get("1.0", tk.END)
        self.misspelled_words.clear()
        self.text.tag_remove("misspelled", "1.0", tk.END)

        words = re.findall(r'\b\w+\b', content)
        offset = 0
        for word in words:
            if word.lower() not in self.english_words:
                start_index = content.find(word, offset)
                offset = start_index + len(word)  # update offset to the end of the current word
                index = f"1.{start_index}"
                self.text.tag_add("misspelled", index, f"{index}+{len(word)}c")
                self.text.tag_config("misspelled", foreground="red")
                self.misspelled_words[index] = word.lower()

    def manual_spell_check(self):
        self.clear_suggestion_buttons()
        for index, word in self.misspelled_words.items():
            suggestions = self.spell_check(word)[:5]  # Get top 5 suggestions
            for correct_word, _ in suggestions:
                btn = tk.Button(self.root, text=correct_word,
                                command=lambda w=word, c=correct_word, i=index: self.replace_word(i, w, c))
                btn.pack(side='bottom')
                self.suggestion_buttons.append(btn)

    def replace_word(self, index, old, new):
        self.text.delete(index, f"{index}+{len(old)}c")
        self.text.insert(index, new)
        self.check(None)  # Re-check spelling to update tags and dictionary

    def spell_check(self, word):
        suggestions = []
        for correct_word in self.english_words:
            distance = self.wagner_fischer(word, correct_word)
            suggestions.append((correct_word, distance))
        suggestions.sort(key=lambda x: x[1])
        return suggestions

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

if __name__ == "__main__":
    SpellingChecker()
