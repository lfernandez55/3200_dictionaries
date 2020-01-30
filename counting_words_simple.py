romeo_talk = "It is the east and Juliet is the sun Arise fair sun . . . ."
words_list = romeo_talk.split(" ")
word_count_dict = {}
for word in words_list:
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] += 1

print(word_count_dict)