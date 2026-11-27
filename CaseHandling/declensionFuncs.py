from enums import *

def firstDec(genitive, case, number):
    stem = genitive[:-2]

    match (case, number):
        case (NounCase.ACC, Number.SNG):
            return stem + 'am'
        case (NounCase.ABL, Number.SNG):
            return stem + 'a'
            
        case (NounCase.NOM, Number.PLU):
            return stem + 'ae'
        case (NounCase.ACC, Number.PLU):
            return stem + 'as'
        case (NounCase.ABL, Number.PLU):
            return stem + 'is'

def secondDecMas(genitive, case, number):
    stem = genitive[:-1]
    
    match (case, number):
        case (NounCase.ACC, Number.SNG):
            return stem + 'um'
        case (NounCase.ABL, Number.SNG):
            return stem + 'o'
            
        case (NounCase.NOM, Number.PLU):
            return stem + 'i'
        case (NounCase.ACC, Number.PLU):
            return stem + 'os'
        case (NounCase.ABL, Number.PLU):
            return stem + 'is'

def secondDecNeu(genitive, case, number):
    stem = genitive[:-1]
        
    match (case, number):
        case (NounCase.ACC, Number.SNG):
            return stem + 'um'
        case (NounCase.ABL, Number.SNG):
            return stem + 'o'
            
        case (NounCase.NOM, Number.PLU):
            return stem + 'a'
        case (NounCase.ACC, Number.PLU):
            return stem + 'a'
        case (NounCase.ABL, Number.PLU):
            return stem + 'is'

def thirdDecMas(genitive, case, number):
    stem = genitive[:-2]
    
    match (case, number):
        case (NounCase.ACC, Number.SNG):
            return stem + 'em'
        case (NounCase.ABL, Number.SNG):
            return stem + 'e'
        
        case (NounCase.NOM, Number.PLU):
            return stem + 'es'
        case (NounCase.ACC, Number.PLU):
            return stem + 'es'
        case (NounCase.ABL, Number.PLU):
            return stem + 'ibus'
       
def thirdDecFem(genitive, case, number):
    stem = genitive[:-2]

    match (case, number):
        case (NounCase.ACC, Number.SNG):
            return stem + 'em'
        case (NounCase.ABL, Number.SNG):
            return stem + 'e'
        
        case (NounCase.NOM, Number.PLU):
            return stem + 'es'
        case (NounCase.ACC, Number.PLU):
            return stem + 'es'
        case (NounCase.ABL, Number.PLU):
            return stem + 'ibus'

def thirdDecNeu(genitive, case, number, starCase):
    stem = genitive[:-2]
    
    match (case, number):
        case (NounCase.ACC, Number.SNG):
            return starCase
        case (NounCase.ABL, Number.SNG):
            return stem + 'e'
        
        case (NounCase.NOM, Number.PLU):
            return stem + 'a'
        case (NounCase.ACC, Number.PLU):
            return stem + 'a'
        case (NounCase.ABL, Number.PLU):
            return stem + 'ibus'   