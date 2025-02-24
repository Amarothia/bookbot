def word_count(words: str) -> int:
    return len(words.split())

def character_count(words: str) -> dict:
    characters_counted = {}
    character = ""

    for c in words:
        character = c.lower()
        if character not in characters_counted:
            characters_counted[character] = 1
        else:
            characters_counted[character] += 1

    sorted_count_key_list = sorted(characters_counted) # this only sorts the keys
    sorted_dict = {}

    for key in sorted_count_key_list:
        sorted_dict[key] = characters_counted[key]

    return sorted_dict
