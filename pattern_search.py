def pattern_search(text, pattern, replacement, case_sensitive=True):
    fixed_text = ""
    num_skips = 0
    for index in range(len(text)):
        match_count = 0
        if num_skips > 0:
            num_skips -= 1
            continue
        for char in range(len(pattern)): 
            if case_sensitive and pattern[char] == text[index + char]:
                match_count += 1
            elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
                match_count += 1
            else:
                fixed_text += text[index]
                break
        if match_count == len(pattern):
            print(pattern, "found at index", index)
            fixed_text += replacement
            num_skips = len(pattern) - 1
    return fixed_text

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
fixed_intro = pattern_search(friends_intro, "Language", "language")
fixed_intro = pattern_search(fixed_intro, "pylhon", "Python", False)
fixed_intro = pattern_search(fixed_intro, "idil", "ideal", False)
fixed_intro = pattern_search(fixed_intro, "zzz ", "")
fixed_intro = pattern_search(fixed_intro, "syntacs", "syntax")
fixed_intro = pattern_search(fixed_intro, "languuUuage", "language")
print(fixed_intro)