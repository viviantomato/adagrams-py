import random
from lib2to3.pgen2.pgen import DFAState

# initiate the empty list 
# to keep the original pool - make a copy of dictionary
# get letter from the copy dict/pool  random.ran()
# draw one letter a time, x 10, for loop (0, 10),  
# also update the qty. of the letter in each loop
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

SCORE_POOL = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10    
}

def copy_letter_from_original(pool):
    pool_dict_copy = {}
    for key, value in pool.items():
        pool_dict_copy[key] = value
    return pool_dict_copy

def draw_letters():   
    res_letters = []
    letter_bank_dict = copy_letter_from_original(LETTER_POOL)
    while len(res_letters) < 10:   
        letter = random.choice(list(letter_bank_dict.keys()))
        if letter_bank_dict[letter] > 0:
            res_letters.append(letter)
            letter_bank_dict[letter] -= 1
    #print(res_letters)
    return res_letters

def create_dict(data):
    # initiatite word_dict 
    data_dict = {}
    for element in data:
        if element not in data_dict:
            data_dict[element] = 1
        else:
            data_dict[element] += 1
    return data_dict

def uses_available_letters(word, letter_bank):
    # convert word to capital
    # for each key, value in word dict.items()
    # check if key of word_dict <= key of letetr_bank dict
    # return True
    # else: return False
    word = word.upper()
    word_dict = create_dict(word)
    letter_bank_dict = create_dict(letter_bank)

    for letter, quantity in word_dict.items():
        if letter not in letter_bank_dict:
            return False
        else:
            if quantity > letter_bank_dict[letter]:
                return False        
    return True    

def score_word(word):   
# word as string
# variable stores the final score
# if len(word) >= 7 and <= 10, add 8 points
# loop thru each element of in word
# add points based on the value of the key

    total_score = 0
    word = word.upper()
    if len(word) >= 7 and len(word) <= 10:
        total_score += 8
    '''
    # time complexity :O(n)
    score_dict = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1)
    score_dict.update(dict.fromkeys (['D', 'G'], 2))
    score_dict.update(dict.fromkeys(['B', 'C', 'M', 'P'], 3))
    score_dict.update(dict.fromkeys (['F', 'H', 'V', 'W', 'Y'], 4))
    score_dict.update(dict.fromkeys (['K'], 5))
    score_dict.update(dict.fromkeys (['J', 'X'], 8))
    score_dict.update(dict.fromkeys (['Q','Z'], 10))
    '''

    for letter in word:
        if letter in SCORE_POOL.keys():
            total_score += SCORE_POOL[letter]
    return total_score


def get_highest_word_score(word_list):
    # return tuple (word, total_score) leave this line
    
    max_score = 0
    final_word_dict = {}
    for word in word_list:
        word_score = score_word(word)
        if word_score > max_score:
            max_score = word_score
    for word in word_list:
        if score_word(word) == max_score:
            final_word_dict[word] = len(word)
    print(final_word_dict)


    if len(final_word_dict) == 1:
        return final_word_dict[word], max_score
    else:
        if 10 in final_word_dict.values():
            name = [k for k, v in final_word_dict.items() if v == 10]   
            return (name, max_score)    
        elif 10 not in final_word_dict.values():
            name = min(final_word_dict, key=final_word_dict.get)
            return (name, max_score)
        #else: #there two same length

            #return the first one 