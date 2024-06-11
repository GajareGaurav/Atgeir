word = input("Enter something: ")

def count_vowels_consonants(word):
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0
    

    for char in word.lower():
        if char.isalpha(): 
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

vowel_count, consonant_count = count_vowels_consonants(word)

print(f"No. of vowels: {vowel_count}")
print(f"No. of consonants: {consonant_count}")
