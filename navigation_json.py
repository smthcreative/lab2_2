'''
Program
'''
import json


def read_json_file(path:str):
    '''
    Function read file json and return 
    dictionary file
    '''
    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def traversal(data):
    '''
    Recursive function traversal take argument,
    print type of data and request user to input
    smth, after it return themself.
    '''
    if isinstance(data, dict) == True:
        print('This objecct is dictionary')
        keys = list(data.keys())
        print("Please choose one of them:\n--> " + "\n--> ".join(keys))
        while True:
            try:
                key = input('>>> ')
                if key == 'exit':
                    exit()
                return traversal(data[key.strip()])
            except KeyError:
                print('Try again')        
    elif isinstance(data, list) == True:
        print('This object is list')
        range_of_idx = len(data) - 1
        print(f"Please choose index of list from 0 to {range_of_idx}")
        while True:
            try:
                idx = input('>>> ')
                if idx == 'exit':
                    exit()
                return traversal(data[int(idx)])
            except (IndexError, ValueError):
                print('Try again')
    print(data)
    print('That`s all\n********************')


def main():
    '''
    Main fuction
    '''
    file = read_json_file('info.json')
    while True:
        print('If you want to exit print exit')
        traversal(file)

if __name__ == '__main__':
    main()
    