from enum import IntEnum

class Speech(IntEnum):
    NONE = -1
    NOUN = 0
    VERB = 1
    ADJ = 2
    ADV = 3
    PREP = 4
    PRO = 5

class NounCase(IntEnum):
    NONE = -1
    NOM = 0
    VOC = 1
    GEN = 2
    DAT = 3
    ACC = 4
    ABL = 5
    LOC = 6

class VerbPerson(IntEnum):
    NONE = -1
    ONE = 0
    TWO = 1
    THR = 2

class Number(IntEnum):
    NONE = -1
    SNG = 0
    PLU = 1

class Gender(IntEnum):
    NONE = -1
    FEM = 0
    MAS = 1
    NEU = 2
    COM = 3

englishToLatin = {
    'i': {NounCase.NOM: 'ego', NounCase.ACC: 'me', NounCase.ABL: 'me'},
    'you': {NounCase.NOM: 'tu', NounCase.ACC: 'te', NounCase.ABL: 'te'},
    'we': {NounCase.NOM: 'nos', NounCase.ACC: 'nos', NounCase.ABL: 'nobis'},
    'you all': {NounCase.NOM: 'vos', NounCase.ACC: 'vos', NounCase.ABL: 'vobis'},
    'and': ['et'],
    'but': ['sed'],
    'because': ['quod'],
    'in': ['in', NounCase.ABL],
    'into': ['in', NounCase.ACC],
    'onto': ['in', NounCase.ACC],
    'through': ['per', NounCase.ACC],
    'to': ['ad', NounCase.ACC],
    'at': ['in', NounCase.ABL],
    'with': ['cum', NounCase.ABL],
    'boy': ['puer', 'pueri', 'm'],
    'girl': ['puella', 'puellae', 'f'],
    'city': ['urbs', 'urbis', 'f'],
    'sister': ['soror', 'sororis', 'f'],
    'father': ['pater', 'patris', 'm'],
    'night': ['nox', 'noctis', 'f'],
    'love': ['amo', 'amare', 'amavi', 'amatum'],
    'work': ['laboro', 'laborare', 'laboravi', 'laboratum'],
    'see': ['video', 'videre', 'vidi', 'visus'],
    'lead': ['duco', 'ducere', 'duxi', 'ductum'],
    'capture': ['capio', 'capere', 'cepi', 'captum'],
    'hear': ['audio', 'audire', 'audivi', 'auditum'],
    'thief': ['fur', 'furis', 'm'],
    'robber': ['fur', 'furis', 'm'],
    'be': ['sum', 'esse', 'fui', 'futurum']
}

englishPrepositions = ['in', 'into', 'onto', 'to', 'through', 'at', 'with']

englishTemporalWords = ['night', 'hour', 'day']

englishConjunctions = ['and', 'but', 'because']

englishPronouns = ['i', 'me', 'you', 'we', 'us', 'y\'all', 'you all']

thoughtProccess = True

class Word:
    def __init__(self, text, partOfSpeech):
        self.text = text
        self.rawText = text
        self.translation = None
        self.needed = True

        if text in englishToLatin:
            self.dictEntry = englishToLatin[text]

        self.partOfSpeech = partOfSpeech

    def __str__(self):
        return self.text