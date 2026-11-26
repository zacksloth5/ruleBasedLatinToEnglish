from clauses import *


translations = 0
def translate(englishText):
    global translations
    translations += 1
    sentenceText = Sentence(englishText)
    sentenceText.execute()

    print(f"----------------------Translation #{translations}----------------------")
    print(f"\"{englishText}\" \nto:\n{str(sentenceText).capitalize()}\n")

sentencesToTranslate = [
"At night, the father works"
]


for sentence in sentencesToTranslate:
    translate(sentence)

