def sort_on(d):
    return d["num"]

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
print(file_contents)
words = file_contents.split()
number_of_words = len(words)
print(f"The number of words is {number_of_words}")
count = 0
count_lists =  []
for word in words:
    count = count + len(word.lower())
print(f"The number of characters is {count}")

chars_dict = get_chars_dict(file_contents)
chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

for item in chars_sorted_list:
    if not item["char"].isalpha():
        continue
    print(f"The '{item['char']}' character was found {item['num']} times")
