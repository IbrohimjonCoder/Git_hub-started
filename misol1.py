def count_vowels_and_consonants(text: str) -> dict:
    vowels_set = set("aeiou")
    
    unli_soni = 0
    undosh_soni = 0
    
    for char in text.lower():
        if char.isalpha():
            if char in vowels_set:
                unli_soni += 1
            else:
                undosh_soni += 1
                
    return {"unli": unli_soni, "undosh": undosh_soni}

print(count_vowels_and_consonants("Salom Dunyo!"))