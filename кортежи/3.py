friends = ['Кирилл', 'Руслан', 'Дмитрий', 'Александр', 'Екатерина']
popular_names = ['Александр', 'Даниил', 'Михаил', 'Максим', 'Дмитрий', 'Иван', 'Матвей', 'Роман', 'Екатерина', 'Анна']
for i in range (len(friends)):
    if friends[i] in popular_names:
        print(friends[i])