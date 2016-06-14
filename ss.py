class Foo(object):
    #定义实例方法
    def instance_method(self):
        print('是类{}的实例方法，只能被实例对象调用'.format(Foo))

    #定义静态方法
    @staticmethod
    def static_method():
        print('静态方法')
    #定义类方法
    @classmethod
    def class_method(cls):
        print('类方法')      
    



foo = Foo()
#实例方法测试
foo.instance_method()#True
#Foo.instance_method(self)#False,NameError: name 'self' is not defined
#静态方法测试
foo.static_method()#True
Foo.static_method()#True
#类方法测试
foo.class_method()#True
Foo.class_method()#True

'''
实例方法只能被实例对象调用，静态方法(由@staticmethod装饰的方法)、类方法(由@classmethod装饰的方法)，可以被类或类的实例对象调用。
实例方法，第一个参数必须要默认传实例对象，一般习惯用self。
静态方法，参数没有要求。
类方法，第一个参数必须要默认传类，一般习惯用cls。
'''

# coding:utf-8

class Book(object):

    def __init__(self,title):
        self.title = title

    #define the class method
    @classmethod
    def create(cls,title):
        book=cls(title=title)#实例化
        return book
    
        

book1 = Book('Python')
book2 = Book.create('Django')
print(book1.title)
print(book2.title)

##################
##################
'''
继承类中的区别 从下面代码可以看出，如果子类继承父类的方法，子类覆盖了父类的静态方法，
子类的实例继承了父类的static_method静态方法，调用该方法，还是调用的父类的方法和类属性。
子类的实例继承了父类的class_method类方法，调用该方法，调用的是子类的方法和子类的类属性。
'''
# coding:utf-8

class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*args):
        return sum(args) / len(args)

    @staticmethod
    def static_method():
        return Foo.averag(Foo.X, Foo.Y)
    #可以看出两类方法的区别
    @classmethod
    def class_method(cls):
        return cls.averag(cls.X, cls.Y)

class Son(Foo):
    X = 3
    Y = 5

    @staticmethod
    def averag(*args):
        return sum(args) / 3

p = Son()
print(p.static_method())#调用的还是父类的属性和方法
print(p.class_method())#调用的是子类的属性和方法






























    
