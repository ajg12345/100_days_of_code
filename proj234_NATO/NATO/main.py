import pandas

with open("nato_phonetic_alphabet.csv") as npa:
    nato_list = npa.readlines()[1:]
    nato_dict = {record.split(',')[0]: record.split(',')[1].strip('\n') for record in nato_list}
print(nato_dict)
name = input().upper()

translated_name = [nato_dict[letter] for letter in name]
print(translated_name)

