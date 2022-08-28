from os.path import exists
from os import system
import pickle


def save_obj(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


def check(file):
    return exists(file)


def notspace(string):
    return string != ""


def clear():
    system("clear")
