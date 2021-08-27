text = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

counter = len(text)

for idx in croatia:      
    counter -= text.count(idx)

print(counter)