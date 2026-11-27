from enums import *
from declensionFuncs import *

class Noun(Word):
    def __init__(self, text, case = NounCase.NONE, number = Number.NONE):
        super().__init__(text, Speech.NOUN)

        self.case = case
        self.number = number


        #Simple Number Predicter
        if number == Number.NONE:
            if text.endswith('s'):
                self.number = Number.PLU

            else:
                self.number = Number.SNG

        if self.number == Number.PLU:
            self.unPluralize()

        self.dictEntry = englishToLatin[self.rawText]
        self.temporal = (self.rawText in englishTemporalWords)

        self.determineGender()
        self.determineDeclension()

        if thoughtProccess:
            print(f"Initalized noun, {self.text} with declension {self.declension}.")

    def determineGender(self):
        match self.dictEntry[2]:
            case 'f':
                self.gender = Gender.FEM
            case 'm':
                self.gender = Gender.MAS
            case 'n':
                self.gender = Gender.NEU
            case 'c':
                self.gender = Gender.COM
            case _:
                self.gender = Gender.NONE

    def determineDeclension(self):
        finalGen = self.dictEntry[1]
        if finalGen.endswith('ae'):
            self.declension = 1
        elif finalGen.endswith('i'):
            self.declension = 2
        elif finalGen.endswith('is'):
            self.declension = 3
        else:
            self.declension = -1

    def unPluralize(self):
        if self.rawText in englishToLatin:
            return

        if self.rawText[:-1] in englishToLatin:
            self.rawText = self.rawText[:-1]
            return

        if self.rawText[:-2] in englishToLatin:
            self.rawText = self.rawText[:-2]
            return

        if self.text.endswith('ies') and (self.rawText[:-3] + 'y' in englishToLatin):
            self.rawText = self.rawText[:-3] + 'y'
            return

        if self.text.endswith('ves') and (self.rawText[:-3] + 'f' in englishToLatin):
            self.rawText = self.rawText[:-3] + 'f'
            return

        raise Exception(f"Could not unpluralize {self.text}")

    def decline(self):
        #Failsafe for unknown/undecided declension. Helps when others parts of speech get miscategorized as noun.
        if (self.declension == -1):
            self.translation = self.dictEntry[0]
            return

        if (self.case, self.number) == (NounCase.NOM, Number.SNG):
            self.translation = self.dictEntry[0]
            return

        genitive = self.dictEntry[1]

        match (self.declension, self.gender):
            case (1, _):
                self.translation = firstDec(genitive, self.case, self.number)
            case (2, Gender.MAS):
                self.translation = secondDecMas(genitive, self.case, self.number)
            case (2, Gender.NEU):
                self.translation = secondDecNeu(genitive, self.case, self.number)
            case (3, Gender.MAS):
                self.translation = thirdDecMas(genitive, self.case, self.number)
            case (3, Gender.FEM):
                self.translation = thirdDecFem(genitive, self.case, self.number)
            case (3, Gender.NEU):
                self.translation = thirdDecNeu(genitive, self.case, self.number, self.dictEntry[0])
            case (_, _):
                raise Exception(f"Unknown Declension for noun {self.text}")