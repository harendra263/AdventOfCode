from typing import Set, List
from collections import Counter

with open('data/day02.txt') as f:
    ids = [line.strip() for line in f]


def char_count_values(word: str) -> Set[int]:
    char_counts = Counter(word)
    return set(char_counts.values())


def checkSum(ids: List[str]) -> int:
    """
    returns  (# of strings character occuring exactly twice)
             (# strings character occuring exactly thrice)
    """
    num_twos = 0
    num_threes = 0

    for box_id in ids:
        ccv = char_count_values(box_id)
        if 2 in ccv:
            num_twos += 1
        if 3 in ccv:
            num_threes += 1
    
    return num_twos * num_threes


print(checkSum(ids))


# Given a list of ids, exactly two differ by exactly one character
# find the remaining characters

def characters_in_common(ids: List[str]) -> str:
    leave_one_outs = Counter()
    
    for box_id in ids:
        for i in range(len(box_id)):
            leave_one_out = tuple(box_id[:i] + "_" + box_id[(i+1):])
            leave_one_outs[leave_one_out] += 1
        
    
    [(best, count),(not_best, not_best_count)] = leave_one_outs.most_common(2)

    assert count == 2
    assert not_best_count == 1
    return "".join([c for c in best if c != "_"])

print(characters_in_common(ids))

            


characters_in_common(ids)   