from enums import *

def firstConj(infinitive, person, number):
    stem = infinitive[:-3] 

    match (person, number):
        case (VerbPerson.TWO, Number.SNG):
            return stem + 'as'

        case (VerbPerson.THR, Number.SNG):
            return stem + 'at'

        case (VerbPerson.ONE, Number.PLU):
            return stem + 'amus'

        case (VerbPerson.TWO, Number.PLU):
            return stem + 'atis'

        case (VerbPerson.THR, Number.PLU):
            return stem + 'ant'

def secondConj(infinitive, person, number):
    stem = infinitive[:-3] 
    
    match (person, number):
        case (VerbPerson.TWO, Number.SNG):
            return stem + 'es'

        case (VerbPerson.THR, Number.SNG):
            return stem + 'et'

        case (VerbPerson.ONE, Number.PLU):
            return stem + 'emus'

        case (VerbPerson.TWO, Number.PLU):
            return stem + 'etis'

        case (VerbPerson.THR, Number.PLU):
            return stem + 'ent'

def thirdConj(infinitive, person, number):
    stem = infinitive[:-3] 
    
    match (person, number):
        case (VerbPerson.TWO, Number.SNG):
            return stem + 'is'

        case (VerbPerson.THR, Number.SNG):
            return stem + 'it'

        case (VerbPerson.ONE, Number.PLU):
            return stem + 'imus'

        case (VerbPerson.TWO, Number.PLU):
            return stem + 'itis'

        case (VerbPerson.THR, Number.PLU):
            return stem + 'unt'

def thirdIOConj(infinitive, person, number):
    stem = infinitive[:-3] 
        
    match (person, number):
        case (VerbPerson.TWO, Number.SNG):
            return stem + 'is'

        case (VerbPerson.THR, Number.SNG):
            return stem + 'it'

        case (VerbPerson.ONE, Number.PLU):
            return stem + 'imus'

        case (VerbPerson.TWO, Number.PLU):
            return stem + 'itis'

        case (VerbPerson.THR, Number.PLU):
            return stem + 'iunt'

def fourthConj(infinitive, person, number):
    stem = infinitive[:-3] 

    match (person, number):
        case (VerbPerson.TWO, Number.SNG):
            return stem + 'is'

        case (VerbPerson.THR, Number.SNG):
            return stem + 'it'

        case (VerbPerson.ONE, Number.PLU):
            return stem + 'imus'

        case (VerbPerson.TWO, Number.PLU):
            return stem + 'itis'

        case (VerbPerson.THR, Number.PLU):
            return stem + 'iunt'

def toBeConj(oneSingularForm, person, number):
    stem = oneSingularForm[:-3] 

    match (person, number):
        case (VerbPerson.TWO, Number.SNG):
            return stem + 'es'

        case (VerbPerson.THR, Number.SNG):
            return stem + 'est'

        case (VerbPerson.ONE, Number.PLU):
            return stem + 'sumus'

        case (VerbPerson.TWO, Number.PLU):
            return stem + 'estis'

        case (VerbPerson.THR, Number.PLU):
            return stem + 'sunt'

