# Задача 1. Да се напише функция, която да търси в списък. Като параметър да приема
# списък и да принтира ако елементът е в списъка неговата позиция, ако ли не да
# принтира, че не е намерен.
# Вход: [1, 2, 5, 9, 10], 5 Вход: [1, 2, 5, 9, 10], 3
# Изход: Position 2 Изход: Not found


def List_search(List, Element) :
    # for i in range(len(List)) : 
    #     if Element == List[i] :
    #         pos = i
    # if print(f'Position {pos}')
    # print('Not Found')

    if Element in List :
        print(f'Position {List.index(Element)}')
    else :
        print('Not Found')




List_1 = [1, 2, 5, 9, 10]

List_search(List_1, 3)

