#!/usr/bin/env python3

SMALL=1
BIG=100

def guess_my_number():
    global SMALL
    global BIG
    total=SMALL+BIG
    # print(total)
    # print(bin(total))
    ash=bin(total>>1)
    return (int(str(ash),2))
    # print(ash)
    # print(int(str(ash),2))


def bigger():
    global SMALL
    global BIG
    SMALL=1+int(guess_my_number())
    return guess_my_number()


def smaller():
    global SMALL
    global BIG
    BIG=1-int(guess_my_number())
    return guess_my_number()


def start_over():
    global SMALL
    global BIG
    SMALL=1
    BIG=100
    return guess_my_number()
