from clauses import *

translations = 0
def translate(englishText):
    global translations
    translations += 1
    sentenceText = Sentence(englishText)
    sentenceText.execute()

    latinTranslation = str(sentenceText).capitalize() + "." 
    
    print(f"----------------------Translation #{translations}----------------------")
    print(f"\"{englishText}\" \nto:\n{latinTranslation}")

sentencesToTranslate = [
    "The father leads the boy through the city, but the girl hears the bird."
]


for sentence in sentencesToTranslate:
    translate(sentence)


