
def show_field(f):
    print('   0 1 2')
    for i in range(len(f)):
        print(str(i) + " " + " " + (' '.join(f[i])))


def user_input(f):
    while True:
        place = input("Введите координаты:").split()
        if len(place)!=2:
            print("Введите две координаты!")
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print("Введите числа!")
            continue
        x,y = map(int,place)
        if not(0<=x and x<3 and 0<=y and y<3):
            print("вы вышли из диапазона: ")
            continue
        if f[x][y]!="-":
            print("Клетка занята: ")
            continue
        break
    return x,y


# def win_v1(f,user):
#     def chek_line(a1,a2,a3,user):
#         if (a1==user and a2==user and a3==user):
#             return True
#     for n in range(3):
#         chek_line(f[n][0], f[n][1], f[n][2], user) or (f[0][n], f[1][n], f[2][n], user) or (f[0][0], f[1][1], f[2][2], user) or (f[2][0], f[1][1], f[0][2], user)
#         return True
#     return False
# win_v1(field,user)

def win_position(f,user):
    f_list=[]
    for l in f:
        f_list+=l
    positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p)))==3:
            return True
    return False

field = [["-"] * 3 for _ in range(3)]
count = 0
while True:
    if count == 9:
        print("Ничья!")
        break
    if count%2==0:
        user = "X"
    else:
        user = "0"
    show_field(field)
    x,y = user_input(field)
    field[x][y]=user
    if win_position(field,user):
        print(f"Выйграл {user}")
        show_field(field)
        break
    count+=1



# def show_field(f):
#     field = [["-"] * 3 for _ in range(3)]
#     print("  0 1 2")
#     for i in range(len(f)):
#         print(str(i), *f[i])
# show_field(field)
