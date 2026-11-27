from enums import *
from noun import *
from verb import *
from pronoun import *
from preposition import *


class Clause:
    def __init__(self, text, prevClause, clauseNumber):
        self.text = text
        self.wordList = []
        self.wordObjectList = []

        self.translation = "Not_Yet_Generated"
        self.subject = None

        self.nextSeperator = None
        self.clauseNumber = clauseNumber
        self.prevClause = prevClause

        if thoughtProccess: print(f'Initialized clause #{self.clauseNumber}')

    def execute(self):
        #Split into Wordlist
        self.wordList = self.text.split()

        #Remove Articles
        self.wordList = [word for word in self.wordList if word not in ['a', 'an', 'the']]

        self.initiateWords()

        if thoughtProccess: print(f'Words in clause #{self.clauseNumber}  are initiated.\n')

        self.generateTranslation()

        if thoughtProccess: print(f'Translations in clause #{self.clauseNumber} have generated.\n')

        self.translation = ' '.join(word.translation for word in self.wordList)

    def initiateWords(self):
        wordPosition = 0  
        wordNumber = 0
        currPreposition = None
        inInfinitive = False

        #Iterative loop which attempts to classify each word in the sentence
        for word in self.wordList:
            #If we get in a preposition stop counting and go in the prepositional phrase
            if currPreposition:
                argument = Noun(word, currPreposition.argumentType)
                self.wordObjectList.append(argument)

                #Ablative of time-when does not need a preposition.
                if argument.temporal and self.wordObjectList[-2].text == 'at':
                    self.wordObjectList[-2].needed = False

                currPreposition = None
                wordNumber += 1
                continue

            if word in englishPrepositions and not inInfinitive:
                currPreposition = Preposition(word)
                self.wordObjectList.append(currPreposition)
                wordNumber += 1
                continue

            #The first word not in a preposition is assumed to be the subject if it does not have 4 dictionary entries
            if wordPosition == 0:
                if word in englishPronouns:
                    self.subject = Pronoun(word, NounCase.NOM)
                    self.subject.needed = False
                else:
                    self.subject = Noun(word, NounCase.NOM)

                    #Checks if the subject is actually a verb. Then it will revert to the previous clause subject.
                    #It then increase position so that it is now interpretted as a verb and the noun is never added to the list
                    if len(self.subject.dictEntry) == 4:
                        self.subject = self.prevClause.subject
                        self.subject.needed = False
                        wordPosition += 1
            
                self.wordObjectList.append(self.subject)

            #The second word not in a preposition is assumed to be the verb.
            if wordPosition == 1:
                self.wordObjectList.append(Verb(word))

                if word in infitivalVerbs:
                    inInfinitive = True

            if wordPosition == 2 and word == 'to' and inInfinitive:
                wordNumber += 1
                continue

            #The third word not in a preposition is assumed to be the object if it is not a conjunction.
            if wordPosition == 2 and word not in englishConjunctions:
                if inInfinitive:
                    self.wordObjectList.append(Verb(word, infinitive = True))
                    #Now let an object still be taken, so do not increase the wordPosition
                    inInfinitive = False
                    wordNumber += 1
                    continue

                elif word in englishPronouns:
                    self.wordObjectList.append(Pronoun(word, NounCase.ACC))    
                else:
                    self.wordObjectList.append(Noun(word, NounCase.ACC))

            #After the subject and verb have been found, if a conjunction is spotted start a new clause and truncate this one.
            if wordPosition >= 2 and word in englishConjunctions:
                self.nextSeperator = word
                self.text = ' '.join(self.wordList[:wordNumber])
                break

            #Iterate wordNumber (the literal number) and wordPosition (excludes prepositions and conjunctions).
            wordNumber += 1
            wordPosition += 1

    def generateTranslation(self):
        self.reOrderedWords = [
        [], #Potential starting Ablative of Time-When
        [], #Subject of the Sentence
        [], #Potential Prepositional Phrase of the Sentence
        [], #Potential Object of the Sentence
        []  #Verb of the sentence
        ]

        inPrepostion = False
        withPreposition = False

        #Go through the words of the sentence!
        for word in self.wordObjectList:
            #Preposition module and handling!
            if word.partOfSpeech == Speech.PREP:
                inPrepostion = True
                withPreposition = False

                #Only if the preposition is determined as needed as many ablatives render it unnecesary.
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

                #To make infinitival verbs appear first
                self.reOrderedWords[4].insert(0, word)

        self.wordList = [word for wordList in self.reOrderedWords for word in wordList]

    def nounTranslation(self, word):
        #Assumes word is not in a preposition!
        word.decline()
        
        if word.case == NounCase.NOM:
            #Makes it so that pronouns in the nominative are not added (as they are assumed).
            if word.needed: 
                self.reOrderedWords[1].append(word)

            if thoughtProccess: print(f"Translated {word} as {word.translation}")

        if word.case == NounCase.ACC:
            if word.needed:
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
        self.clauses.append(Clause(self.text, None, 1))

        currClause = self.clauses[0]
        currClause.execute()

        remainingText = self.text

        while currClause.nextSeperator is not None:
            remainingText = remainingText.removeprefix(currClause.text)
            
            remainingText = remainingText.removeprefix(" " + currClause.nextSeperator)
            currClause.translation += (" " + englishToLatin[currClause.nextSeperator][0])

            newClause = Clause(remainingText, currClause, currClause.clauseNumber + 1)

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
