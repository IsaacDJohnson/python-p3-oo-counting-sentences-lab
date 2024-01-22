#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
            self._value = ""
        else:
            self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val


    def is_exclamation(self):
        return self.value.endswith("!")
    
    def is_question(self):
        return self.value.endswith("?")

    def is_sentence(self):
        return self.value.endswith(".")

    def count_sentences(self):

        sentences = [s.strip() for s in re.split(r'[.!?]', self.value) if s.strip()]
        return len(sentences)

pass