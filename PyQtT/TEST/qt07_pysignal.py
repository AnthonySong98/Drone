from PyQt5.QtCore import *

class Qtypesigenal(QObject):

    sinout1 = pyqtSignal(str, int)
    def __init__(self):
        super(Qtypesigenal, self).__init__()
        self.sinout=pyqtSignal(str,int)

    def run(self):
        self.sinout.emit('你好',123)


class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    def get(self,msg1,msg2):
        a=msg1
        b=msg2
        print(a,'这是第一个')
        print(b,'这是第二个')

if __name__=='__main__':
    x=Qtypesigenal()
    y=QTypeSlot()
    print(x.sinout)
    print(x.sinout1)
    print(dir(x))
  #  x.sinout.connect(y.get)
  #  x.run()



