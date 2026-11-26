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
    "I see the boy.",
    "The girl loves the father.",
    "The father captures the thief.",
    "We hear the sister.",
    "You lead the boy into the city.",
    "The boy works in the city.",
    "I love you, but you capture the robber.",
    "The sister sees the girl at night.",
    "We lead the thief through the city."
]


for sentence in sentencesToTranslate:
    translate(sentence)

