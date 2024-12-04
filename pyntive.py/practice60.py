def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count
print(word_counter("Apple"))


# -------------OR---------------


s = "Apple"
word_count = { char:s.count(char) for char in s}
print(word_count)