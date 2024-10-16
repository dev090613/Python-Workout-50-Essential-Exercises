def ubbi_dubbi(word: str) -> str:
    vowels = "aeiou"
    translated = []
    for c in word:
        if c in vowels:
            translated.append("ub")
        translated.append(c)
    return "".join(translated)

answer1 = ubbi_dubbi("soap")
answer2 = ubbi_dubbi("elephant")
print(answer1, answer2)
