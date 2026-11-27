from enums import *
from CaseHandling.conjugationFuncs import *

class Verb(Word):
    def __init__(self, text, person = VerbPerson.NONE, number = Number.NONE, infinitive = False):
        super().__init__(text, Speech.VERB)

        self.person = person

        if self.person == VerbPerson.NONE:
            self.person = VerbPerson.THR

        self.number = number

        self.infinitive = infinitive

        if thoughtProccess: print(f"Initalized verb, {self.text}")


    def takeSubject(self, subject):
        if self.number != Number.NONE:
            return

        self.number = subject.number

        if subject.partOfSpeech == Speech.PRO:
            self.person = subject.person

        self.determineRawText()

        

        self.dictEntry = englishToLatin[self.rawText]
        self.determineConjugation()

        if thoughtProccess: print(f"{self.text} initalized with conjugation {self.conjugation}.")

    def determineRawText(self):
        #Accounting for the irregular verb, 'to be'.
        if self.rawText in ['am', 'are', 'is']:
            self.rawText = 'be'

        #Accounts for changing something like 'he works' to 'he work' for parsing.
        if self.number == Number.SNG and self.person == VerbPerson.THR:
            if self.rawText in englishToLatin:
                pass
            
            elif self.rawText[:-1] in englishToLatin:
                self.rawText = self.rawText[:-1]
    
            elif self.rawText[:-2] in englishToLatin:
                self.rawText = self.rawText[:-2]

        

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
        elif part1.endswith('sum'):
            self.conjugation = 0
        elif part1.endswith('volo'):
            self.conjugation = 0.1
        else:
            #-1 will be the conj. for unknown or unrecognized.
            self.conjugation = -1

    def conjugate(self):
        part1 = self.dictEntry[0]
        part2 = self.dictEntry[1]

        if self.infinitive:
            self.translation = part2
            return

        if (self.person, self.number) == (VerbPerson.ONE, Number.SNG):
            self.translation = part1
            return

        

        match self.conjugation:
            case 0:
                self.translation = toBeConj(part1, part2, self.person, self.number)
            case 0.1:
                self.translation = toWantConj(part1, self.person, self.number)
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
            case -1:
                warnings.warn(f'No conjugation found for {self.rawText}, translation will be the 1st principal part.')
                self.translation = part1

