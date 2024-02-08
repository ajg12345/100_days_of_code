from prettytable import PrettyTable

table = PrettyTable()

table.field_names  = ["Pokemon", "type"]
table.add_row(["squirtle", "water"])
table.add_row(["charmander", "fire"])
print(table.align)
table.align = 'l'
print(table)