from random import randint

class  Die:
    '''表⽰⼀个骰⼦的类'''
    def __init__(self, num_sides = 6):
        '''默认骰子有6面'''
        self.num_sides = num_sides

    def roll(self):
        '''返回⼀个介于1和骰⼦⾯数之间的随机值'''
        return randint(1, self.num_sides)
    
    