str = input()
k = 0
k1 = 0
for i in range(len(str)-1):
    if (str[i] == "Ж" or str[i] == "ж" or str[i] == "Ш" or str[i] == "ш") and (str[i+1] == "Ы" or str[i+1] == "ы"):
        k1 += 1;
    elif (str[i] == "Ч" or str[i] == "ч" or str[i] == "Щ" or str[i] == "щ") and (str[i + 1] == "Я" or str[i+1] == "я"):
        k += 1;
if k == 0 and k1 == 0:
    print('Ошибок нет')

else:
    if k1 != 0 and k == 0:
        print('Количество ошибок по правилу ЖИ/ШИ:')
        print(k1)
    elif k != 0 and k1 == 0:
        print('Количество ошибок по правилу ЧА/ЩА:')
        print(k)
    else:
        print('Количество ошибок по правилу ЖИ/ШИ:')
        print(k1)
        print('Количество ошибок по правилу ЧА/ЩА:')
        print(k)

