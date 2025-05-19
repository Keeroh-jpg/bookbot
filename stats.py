# Accepts a string and returns the number of words used
def word_count(text):
    count = 0
    for t in text.split():
        count += 1
    return count

def char_count(text):
    text = text.lower()
    chars = {}
    # Loops through each character in a given text
    for t in text:
        # If the character is in the dictionary, increment its count
        if t in chars:
            chars[t] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            chars[t] = 1
    return chars

# This function takes a dictionary of characters and their counts, sorts them in descending order, and returns a list of dictionaries with the character and its count
def sort_on(chars):
    sorted_dict = []
    for ch in chars:
        d = {"char": ch, "num": chars[ch]}
        sorted_dict.append(d)
    def key_func(d):
        return d["num"]
    sorted_dict.sort(reverse=True, key=key_func)
    return sorted_dict




    







    
    

    

    
        
    