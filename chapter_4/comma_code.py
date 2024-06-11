cats = ['Tiptoes', 'Frankie', 'Oreo', 'Draco', 'Obi', 'Buddy']

for i in range(len(cats)):
    if not i == len(cats)-1:
        print(cats[i], end=', ')
    else:
        print('and ' + cats[i], end='.')