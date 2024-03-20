import pandas
new_dict = {item: 'f' for item in [1, 2, 3] if item%2 == 0}
print(new_dict)

sentence = 'what is the airspeed of an unladen swallow?'
sen_list = sentence.split()
result = {word: len(word) for word in sen_list}

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15}
weather_f = {key : (value* 9/5 + 32) for key, value in weather_c.items()}

student_data = {"student": ['Aaron','Dom','Dani'], "score": [100, 50, 30]}
student_data_frame = pandas.DataFrame(student_data)
#how to iterate through a pandas data frame:
# with iterrows
for index, row in student_data_frame.iterrows():
    if row.student == 'Aaron':
        print(row)