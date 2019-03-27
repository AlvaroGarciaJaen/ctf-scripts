#!/usr/bin/env python3

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    print(bcolors.HEADER + 'HEADER' + bcolors.ENDC)
    print(bcolors.OKBLUE + 'OKBLUE' + bcolors.ENDC)
    print(bcolors.OKGREEN + 'OKGREEN' + bcolors.ENDC)
    print(bcolors.WARNING + 'WARNING' + bcolors.ENDC)
    print(bcolors.FAIL + 'FAIL' + bcolors.ENDC)
