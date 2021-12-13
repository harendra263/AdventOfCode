

def sametype(s1: str, s2: str) -> bool:
    return s1.lower() == s2.lower()


def reduct(polymer: str)-> str:
    did_reduce = True
    while did_reduce :
        did_reduce = False
        
        for i in range(1, len(polymer)):
            unit1 = polymer[i-1]
            unit2 = polymer[i]
            if sametype(unit1, unit2) and unit1 != unit2:
                polymer = polymer[:i-1] + polymer[i+1:]
                did_reduce = True
                print(len(polymer))
                break
    return polymer



TEST_CASE ="dabAcCaCBAcCcaDA"


assert reduct(TEST_CASE) == "dabCBAcaDA"

with open('data/day05.txt') as f:
    polymer = f.read().strip()


print(reduct(polymer))







