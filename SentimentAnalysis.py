punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(word):
    for mark in punctuation_chars:
        word = word.replace(mark, "")
    return word


def get_pos(text):
    positive_word_number = 0
    list_of_words_from_text = text.split(" ")
    for word in list_of_words_from_text:
        standartized_word = strip_punctuation(word)
        if standartized_word.lower() in positive_words:
            positive_word_number += 1
    return positive_word_number


def get_neg(text):
    negative_word_number = 0
    list_of_words_from_text = text.split(" ")
    for word in list_of_words_from_text:
        standartized_word = strip_punctuation(word)
        if standartized_word.lower() in negative_words:
            negative_word_number += 1
    return negative_word_number


data_to_process = open('project_twitter_data.csv', 'r')
lines_twitter_data = data_to_process.readlines()
answer_file = open('resulting_data.csv', "w")

first_line = "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score"
answer_file.write(first_line)
answer_file.write("\n")
print(lines_twitter_data)
for line in lines_twitter_data:
    if line == "tweet_text,retweet_count,reply_count\n":
        continue
    scores = ""
    list_values = line.split(",")
    scores = '{}, {}, {}, {}, {}'.format(int(list_values[1]), int(list_values[2]), get_pos(list_values[0]),
                                     get_neg(list_values[0]),
                                     (get_pos(list_values[0]) - get_neg(list_values[0])))
    answer_file.write(scores)
    answer_file.write("\n")

answer_file.close()
data_to_process.close()
