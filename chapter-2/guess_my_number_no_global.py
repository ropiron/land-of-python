#!/usr/bin/env python3

def guess_my_number(SMALL,BIG):
    HALF=(SMALL+BIG)/2
    print(int(HALF))
    while True:
        print("up or down")
        guess = input()
        if guess == 'up':
            SMALL=int((SMALL+BIG)/2)
            print(int((SMALL+BIG)/2))

        elif guess == 'down':
            BIG=int((SMALL+BIG)/2)
            print(int((SMALL+BIG)/2))
        else:
            print('BINGO')
            print('Whats small')
            SMALL=int(input())
            print('Whats big')
            BIG=int(input())
            return guess_my_number(SMALL,BIG)
