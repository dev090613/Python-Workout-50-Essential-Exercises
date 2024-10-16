def pig_latin(word: str) -> str:
    if word[0] in "aeiou":
        word += "way"
        return word
    return word[1:] + word[0] + "ay"


result = pig_latin("air")
result1 = pig_latin("eat")
result2 = pig_latin("python")
result3 = pig_latin("computer")
print(result)
print(result1)
print(result2)
print(result3)
