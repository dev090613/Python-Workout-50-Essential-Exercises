def pl_sentence(sentence: str) -> str:
    sentence = sentence.strip().split()
    
    result = []
    for w in sentence:
        if w[0] in "aeiou":
            result.append(f'{w}way')
            continue
        result.append(f'{w[1:]}{w[0]}ay')
    return " ".join(result)


msg = pl_sentence('this is a test translation')
print(msg)
