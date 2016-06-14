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

    
