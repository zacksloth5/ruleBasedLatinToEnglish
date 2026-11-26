from enums import *


class Preposition(Word):
    def __init__(self, text):
        super().__init__(text, Speech.PREP)

        self.dictEntry = englishToLatin[text]

        self.translation = self.dictEntry[0]
        self.argumentType = self.dictEntry[1]