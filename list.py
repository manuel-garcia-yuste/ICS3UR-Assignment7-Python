#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : December 2019
# This program run a list


def adding(list0):
    theSum = 0
    for number in list0:
        theSum = theSum + number

    return theSum


def main():
    # input
    lst = []
    total = int(input('Total numbers in List: '))

    # process
    for num in range(total):
        num = int(input('Enter number '))
        lst.append(num)

    # calling function
    sum0 = adding(lst)

    # output
    print("The sum of the elements is :", (sum0))


if __name__ == "__main__":
    main()
