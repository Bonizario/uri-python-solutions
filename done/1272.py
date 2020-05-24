# 1272 Hidden Message
import re
# \w returns only "a-Z", "0-9" and "_"
# + returns one or more occurrences (in this case \w+ will return the words)


def decode(message):
    new_message = ""
    regex = r'\w+'
    list_of_words = re.findall(regex, message)
    if list_of_words:
        for i in range(len(list_of_words)):
            new_message += list_of_words[i][0]
        return new_message
    else:
        return ""


num_inputs = int(input())
for _ in range(num_inputs):
    raw_message = input().strip()
    decoded_message = decode(raw_message)
    print(decoded_message)
