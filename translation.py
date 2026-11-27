from clauses import *

translations = 0
def translate(englishText):
    global translations
    translations += 1
    sentenceText = Sentence(englishText)
    sentenceText.execute()

    latinTranslation = str(sentenceText).capitalize() + "." 
    
    print(f"----------------------Translation #{translations}----------------------")
    print(f"\"{englishText}\" \nto:\n{latinTranslation}\n")

sentencesToTranslate = [
    "At night, we want you."
]


for sentence in sentencesToTranslate:
    translate(sentence)

