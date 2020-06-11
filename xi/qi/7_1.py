class pl:
    #默认执行__init__ 方法第一个参数必须为 self（公用）
    def __init__(self,name):
        print(name)
        self.name=name
        self.__name=name#私有属性
        print("这是我私有的",self.__name)
        return
    def play(self):
        print(self.name)
        return
k=pl("dsda")
k.play()