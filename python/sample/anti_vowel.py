def anti_vowel(text):
    s=""
    for a in text:
        if a.lower() not in "aeiou":
            s=s+a
    return s
    