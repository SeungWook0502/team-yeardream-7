from random import sample

class SetNum:
    def set_num():
        print('Number Set Done.')
        return sample(range(10), 4)

    def check_palindrome(target):
        for i in range(1, len(target)//2+1):
            if target[i-1] != target[i*-1]:
                return False
        return True
