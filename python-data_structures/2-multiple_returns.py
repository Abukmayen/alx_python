#!/usr/bin/python3


def multiple_returns(sentence):
    # Get the length of the sentence
    length = len(sentence)
    
    # Check if the sentence is empty
    if length == 0:
        first_char = None
    else:
        # Get the first character of the sentence
        first_char = sentence[0]

    return (length, first_char)

if __name__ == "__main__":
    sentence = "At Holberton school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
