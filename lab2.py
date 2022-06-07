
list_of_numbers = [1, 2, 3, 4, 5, 6]
list_of_numbers2 = [7, 8, 9, 10, 11]

list_of_numbers.extend(list_of_numbers2)
print(list_of_numbers)

list_of_numbers.append(12)
print(list_of_numbers)

dict_example = dict({"key": "value", "another_key": "another_value", "number": 1})
print(dict_example.keys(), dict_example.values())

print(bool(" "), bool(""), bool(0), bool(1), bool('0'), bool('1'), bool([]), bool(['', '']))

for i in range(21):
    print(i)

i = 0
while True:
    print(i)
    i += 1
    if i == 21:
        break

my_sentence = "Ala ma kota ale kot ma ale"
my_sentence_array = []

i = 0
temp = ''
for letter in my_sentence:
    i += 1
    if letter != ' ':
        temp += letter
    if letter == ' ' or i == len(my_sentence):
        my_sentence_array.append(temp)
        temp = ''

print(my_sentence_array)


def check_password(password):
    if len(password) < 10:
        return False

    valid_ascii = False
    valid_upper = False
    valid_lower = False

    for letter in password:
        if letter.isupper():
            valid_upper = True
        if letter.islower():
            valid_lower = True
        if letter == "!":
            valid_ascii = True

    return valid_ascii and valid_upper and valid_lower


print(check_password("123"))
print(check_password("KacperHaslo!"))
print(check_password("kacperhaslo!"))
print(check_password("Kacperhaslo"))
print(check_password("Haslo!"))

lista_z_ilomas_elementami_ale_liczby_razem_z_liczba_99 = [1, 2, 3, 4, 99]

for x in lista_z_ilomas_elementami_ale_liczby_razem_z_liczba_99:
    # if x != 99:
    #     print(x)
    if x == 99:
        continue
    print(x)

while True:
    for i in range(len(lista_z_ilomas_elementami_ale_liczby_razem_z_liczba_99)):
        if lista_z_ilomas_elementami_ale_liczby_razem_z_liczba_99[i] == 99:
            print(f'element 99 na {i} miejscu')
            break
    break

# alternatywnie xD

i = 0
while True:
    if lista_z_ilomas_elementami_ale_liczby_razem_z_liczba_99[i] == 99:
        print(f'element 99 na {i} miejscu')
        break
    i += 1
    if i >= len(lista_z_ilomas_elementami_ale_liczby_razem_z_liczba_99):
        print(f'nie ma takiego elementu')
        break


with open('metin.txt', 'r') as file:
    print(file.read(), end="")

print('\n')

with open('metin.txt', 'r') as file:
    print(file.readlines())

jakas_lista_z_jezykow_programowania_jakie_znam = ["java", "golang", "ruby", "python", "html"]

with open('jezyki.txt', 'w') as file:
    for lang in jakas_lista_z_jezykow_programowania_jakie_znam:
        if lang.lower() != 'html':
            file.write(f'{lang}\n')
        else:
            jakas_lista_z_jezykow_programowania_jakie_znam.remove(lang)

print(jakas_lista_z_jezykow_programowania_jakie_znam)

tablica_z_nazwami_miast = ['Olsztyn', 'Gdańsk', 'Warszawa', 'Poznań', 'Sosnowiec']

tylko_3_litery = list(map(lambda x: x[:3], tablica_z_nazwami_miast))
print(tylko_3_litery)
