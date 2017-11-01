from markov_python.cc_markov import MarkovChain

mc = MarkovChain()
mc.add_file('C:/Users/dell/PycharmProjects/markov_chain/Wine Reviews.txt')

mc.add_string("red")

word_lst_1 = mc.generate_text(10)

print (word_lst_1)
word_lst_2 = []

for word in word_lst_1:
    if word.isdigit() == False:
        word_lst_2.append(word)
print(word_lst_2)

not_allowed = ["cases", "made", "has", "while"]
not_all_end = ["with", "and", "or", "on", "direct", "that", "are", "now", "through", "the", "supports", "hard", "a"]

word_lst_3 = []
for word in word_lst_2:
    if word not in not_allowed:
        word_lst_3.append(word)
print(word_lst_3)

while word_lst_3[len(word_lst_3) - 1] in not_all_end:
    del word_lst_3[len(word_lst_3) - 1]
print(word_lst_3)

str1 = ' '.join(word_lst_3)
print("This wine is great because it has {}.".format(str1))




