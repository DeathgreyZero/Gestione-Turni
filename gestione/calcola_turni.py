import array_persona

turni = []
count = 0
for i in array_persona and count < 6:
    if i == 'Matteo':
        turni = [i][count]
        count+=1
    else:
        turni = [i][count+1]
        count+=1

print turni
