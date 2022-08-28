#!/usr/bin/python3

from os import system as run
from sys import argv as params

current_pkgs = params[1]
iso_pkgs = params[2]

with open(current_pkgs, 'r') as f:
    current_pkgs = f.readlines()

with open(iso_pkgs, 'r') as f:
    iso_pkgs = f.readlines()


run('clear')
for pkg in current_pkgs:
    run(f"pacman -Si {pkg}")
    if pkg in iso_pkgs:
        print("pkg is in iso")
        if input("d to delete ") == 'd':
            iso_pkgs.remove(pkg)
        run('clear')
    elif input("a to add ") == 'a':
        iso_pkgs.append(pkg)
    run('clear')

with open("iso_pkglist", "w+") as f:
    f.writelines(iso_pkgs.__iter__())
