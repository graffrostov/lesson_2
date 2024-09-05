# переменные variable

print('lesson_2, variables')    # печатаем название урока

number_of_complete_DZ = 12      # переменная отвечающая за количество выполненых заданий, целочисленное значение, int
number_of_hours = 1.5           # переменная содержит количество затраченых часов, дробное, float
course_name = 'Python'          # переменная содержит название курса, str

# среднее время на задачу, вычисляемая переменная, float
time_for_task = number_of_hours / number_of_complete_DZ

# печатаем, численные переменные перевёл в тип str, иначе появляются ненужные пробелы
print('Курс:', course_name + ', всего выполнено задач:', str(number_of_complete_DZ) + ', затрачено часов:', str(number_of_hours) + ', среднее время выполнения', time_for_task, 'часа.')