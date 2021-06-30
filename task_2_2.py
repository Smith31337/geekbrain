my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for item in my_list:
    number = ''
    diff1 = ''
    diff2 = ''
    for s in item:
        if s in '1234567890':
            number += s
        else:
            if number:
                diff2 += s
            else:
                diff1 += s
    if not number:
        new_list.append(item)
        continue
    number = f'{diff1}{int(number):02d}{diff2}'
    new_list.append('"')
    new_list.append(number)
    new_list.append('"')
print(new_list)
res = ' '.join(new_list)
print(res)

