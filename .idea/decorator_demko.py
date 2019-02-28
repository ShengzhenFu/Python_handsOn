def arg_func(arg):
    def func1(func):
        def func2():
            if arg == 'good':
                print(' let\'s play outdoors !')
            if arg == 'bad':
                print(' let\'s play indoors ! ')
            return func()
        return func2
    return func1

@arg_func('bad')
def func3():
    print(' on bad days')

@arg_func('good')
def func4():
    print(' on good days')

func3()
func4()

class A:
    num = 1
    @classmethod
    def func(cls):
        print('num is ', cls.num)

a = A()
a.func()