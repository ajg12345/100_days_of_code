

# list comprehension example
names = ['jimmy','jake','phil']
new_list = [name.upper() for name in names]

# list comprehension example with conditional
new_j_list = [name.upper() for name in names if name[0] == 'j']

if __name__ == "__main__":
    input_string = input("enter the word to translate")
    print(new_list)
    print(new_j_list)
