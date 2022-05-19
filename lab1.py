a = '11'
b = 1
c = '0'

print("{0}, {1}, {2}".format(type(a), type(b), type(c)))

tab = ["Ala", "ma", "kota", "kot", "ma", "Ale"]

text = ' '.join(tab)

print(text.split(' '))

sentence = "Metody Inżynierii Wiedzy są najlepsze"

print(sentence)
print(len(sentence))

sentence = sentence.lower()

sentence = sentence.replace('ż', 'z')
sentence = sentence.replace('ą', 'a')

print(sentence)
print(len(sentence))

my_set = set(sentence)

print(my_set)
print(len(my_set))

string = "Napis"
long_string = "Długi napis jest"

tubka = (string, long_string)
print(tubka)

list_letters = ['c', 'b', 'd', 'b']
list_number = [2, 1, 3, 7]
list_all = list_letters + list_number
print(list_all.index('c'))
