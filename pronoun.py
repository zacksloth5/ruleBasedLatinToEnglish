from enums import *

class Pronoun(Word):
    def __init__(self, text, case = NounCase.NONE):
        super().__init__(text, Speech.PRO)

        self.case = case

        self.getPronounProperties()

        self.dictEntry = englishToLatin[self.rawText]

        if thoughtProccess: print(f"Initalized pronoun, {self.text}.")

    def decline(self):
        self.translation = self.dictEntry[self.case]
        
    def getPronounProperties(self):
        match self. text:
            case 'i':
                self.number = Number.SNG
                self.person = VerbPerson.ONE
                self.case = NounCase.NOM
            case 'me':
                self.rawText = 'i'
                self.number = Number.SNG
                self.person = VerbPerson.ONE
                if self.case == NounCase.NONE:
                    self.case = NounCase.ACC
            case 'you':
                self.number = Number.SNG
                self.person = VerbPerson.TWO
            case 'we':
                self.number = Number.PLU
                self.person = VerbPerson.ONE
                self.case = NounCase.NOM
            case 'us':
                self.rawText = 'we'
                self.number = Number.PLU
                self.person = VerbPerson.TWO
                if self.case == NounCase.NONE:
                    self.case = NounCase.ACC