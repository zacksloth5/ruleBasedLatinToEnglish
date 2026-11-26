from enums import *
from noun import *
from verb import *
from pronoun import *
from preposition import *


class Clause:
    def __init__(self, text):
        self.text = text
        self.wordList = []
        self.wordObjectList = []

        self.translation = "Not_Yet_Generated"
        self.subject = None

        self.nextSeperator = None

    def execute(self):
        #Split into Wordlist
        self.wordList = self.text.split()

        #Remove Articles
        self.wordList = [word for word in self.wordList if word not in ['a', 'an', 'the']]

        self.initiateWords()

        if thoughtProccess: print('Words in this clause are initiated.\n')

        self.generateTranslation()

        if thoughtProccess: print('Translations in this clause have generated.\n')

        self.translation = ' '.join(word.translation for word in self.wordList)

    def initiateWords(self):
        wordPosition = 0  
        wordNumber = 0
        currPreposition = None

        for word in self.wordList:
            #If we get in a preposition stop counting and go in the prepositional phrase
            if currPreposition:
                argument = Noun(word, currPreposition.argumentType)
                self.wordObjectList.append(argument)

                if argument.temporal and self.wordObjectList[-2].text == 'at':
                    self.wordObjectList[-2].needed = False

                currPreposition = None
                wordNumber += 1
                continue

            if word in englishPrepositions:
                currPreposition = Preposition(word)
                self.wordObjectList.append(currPreposition)
                wordNumber += 1
                continue

            if wordPosition == 0:
                if word in englishPronouns:
                    self.subject = Pronoun(word)
                else:
                    self.subject = Noun(word, NounCase.NOM)
                
                self.wordObjectList.append(self.subject)

            if wordPosition == 1:
                self.wordObjectList.append(Verb(word))

            if wordPosition == 2 and word not in englishConjunctions:
                self.wordObjectList.append(Noun(word, NounCase.ACC))

            if wordPosition >= 2 and word in englishConjunctions:
                self.nextSeperator = word
                self.text = ' '.join(self.wordList[:wordNumber])
                break
            
            wordNumber += 1
            wordPosition += 1

    def generateTranslation(self):
        self.reOrderedWords = [
        [], #Potential starting Ablative of Time-When
        [], #Potential Subject of the Sentence
        [], #Potential Prepositional Phrase of the Sentence
        [], #Potential Object of the Sentence
        []  #Verb of the sentence
        ]

        inPrepostion = False
        withPreposition = False

        for word in self.wordObjectList:
            if word.partOfSpeech == Speech.PREP:
                inPrepostion = True
                withPreposition = False

                if word.needed:
                    self.reOrderedWords[2].append(word)
                    withPreposition = True

                continue

            if inPrepostion:
                word.decline()
                if not withPreposition:
                    self.reOrderedWords[0].append(word)
                else:
                    self.reOrderedWords[2].append(word)

                inPrepostion = False
                continue

            if word.partOfSpeech == Speech.NOUN or word.partOfSpeech == Speech.PRO:
                self.nounTranslation(word)

            if word.partOfSpeech == Speech.VERB:
                word.takeSubject(self.subject)
                word.conjugate()

                if thoughtProccess:
                    print(f"{word.text} conjugated as {word.translation}.")

                self.reOrderedWords[4].append(word)

        self.wordList = [word for wordList in self.reOrderedWords for word in wordList]

    def nounTranslation(self, word):
        #Assumes word is not in a preposition!
        word.decline()
        
        if word.case == NounCase.NOM:
            if word.partOfSpeech == Speech.NOUN:
                self.reOrderedWords[1].append(word)

            if thoughtProccess: print(f"Translated {word} as {word.translation}")

        if word.case == NounCase.ACC:
            self.reOrderedWords[3].append(word)

            if thoughtProccess: print(f"Translated {word} as {word.translation}")

        


    def __str__(self):
        return self.translation

class Sentence:
    def __init__(self, text):
        self.unParsedEnglish = text

        self.text = text
        self.wordList = []

        self.clauses = []
        
        self.translation = "Not_Yet_Generated"

    def execute(self):
        self.filterText()
        self.clauses.append(Clause(self.text))

        currClause = self.clauses[0]
        currClause.execute()

        remainingText = self.text

        while currClause.nextSeperator is not None:
            remainingText = remainingText.removeprefix(currClause.text)
            
            remainingText = remainingText.removeprefix(" " + currClause.nextSeperator)
            currClause.translation += (" " + englishToLatin[currClause.nextSeperator][0])

            newClause = Clause(remainingText)

            newClause.execute()
            self.clauses.append(newClause)

            currClause = newClause

        self.translation = " ".join(clause.translation for clause in self.clauses)

    def filterText(self):
        #Make Lowercase
        self.text = self.text.lower()

        #Remove Punctuation
        self.text = self.text.replace(",","")
        self.text = self.text.replace(".","")

        #Split into Wordlist
        self.wordList = self.text.split()

        #Remove Articles
        self.wordList = [word for word in self.wordList if word not in ['a', 'an', 'the']]

        self.text = " ".join(self.wordList)

    def __str__(self):
        return self.translation
