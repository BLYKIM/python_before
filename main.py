
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def solution(lottos, win_nums):
    answer = []
    zeros = 0

    tmp = 0
    for i, l in enumerate(lottos):
        if l in win_nums:
            tmp += 1
        if l == 0:
            zeros += 1
    if not zeros and not tmp:
        answer.append(6)
    else:
        answer.append(7 - (tmp+zeros))
    if tmp == 0:
        answer.append(6)
    else:
        answer.append(7 - tmp)


    return answer

lottos={44, 1, 0, 0, 31, 25}
