import os
os.remove("gugudan.txt")

f = open("gugudan.txt", 'w')


def gugudan(i):
    print("=" * 13)
    print("{0:^13}".format("%s단" %i))
    print("=" * 13)
    for j in range(1, 10):
        print("  {0} * {1} = {2}" .format(i, j, i * j))
        f.write("  {0} * {1} = {2}\n" .format(i, j, i * j))
    print("=" * 13)


while 1:
    number = input("숫자를 입력하세요: ")

    if number.isdecimal() == False:
        break;
   
    gugudan(int(number))


f.close()

