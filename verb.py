from enums import *
from conjugationFuncs import *

class Verb(Word):
    def __init__(self, text, person = VerbPerson.NONE, number = Number.NONE):
        super().__init__(text, Speech.VERB)

        self.person = person

        if self.person == VerbPerson.NONE:
            self.person = VerbPerson.THR

        self.number = number

        if thoughtProccess: print(f"Initalized verb, {self.text}")


    def takeSubject(self, subject):
        if self.number != Number.NONE:
            return

        self.number = subject.number

        if subject.partOfSpeech == Speech.PRO:
            self.person = subject.person

        if self.number == Number.SNG and self.person == VerbPerson.THR:
            if self.rawText in englishToLatin:
                pass
            
            elif self.rawText[:-1] in englishToLatin:
                self.rawText = self.rawText[:-1]
    
            elif self.rawText[:-2] in englishToLatin:
                self.rawText = self.rawText[:-2]

        self.dictEntry = englishToLatin[self.rawText]
        self.determineConjugation()

        if thoughtProccess: print(f"{self.text} initalized with conjugation {self.conjugation}.")

    def determineConjugation(self):
        part1, part2 = self.dictEntry[0], self.dictEntry[1]

        if part2.endswith('are'):
            self.conjugation = 1
        elif part2.endswith('ere') and part1.endswith('eo'):
            self.conjugation = 2
        elif part2.endswith('ere') and part1.endswith('io'):
            self.conjugation = 3.1
        elif part2.endswith('ere') and part1.endswith('o'):
            self.conjugation = 3
        elif part2.endswith('ire'):
            self.conjugation = 4

    def conjugate(self):
        if (self.person, self.number) == (VerbPerson.ONE, Number.SNG):
            self.translation = self.dictEntry[0]
            return

        part2 = self.dictEntry[1]

        match self.conjugation:
            case 1:
                self.translation = firstConj(part2, self.person, self.number)
            case 2:
                self.translation = secondConj(part2, self.person, self.number)
            case 3:
                self.translation = thirdConj(part2, self.person, self.number)
            case 3.1:
                self.translation = thirdIOConj(part2, self.person, self.number)
            case 4:
                self.translation = fourthConj(part2, self.person, self.number)