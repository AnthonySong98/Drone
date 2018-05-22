from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class lineEditDemo(QWidget):
    def __init__(self):
        super(lineEditDemo,self).__init__()
        e1=QLineEdit()
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont('Arial',20))
        e2=QLineEdit()
        e2.setValidator(QDoubleValidator(0.99,99.99,2))
        e2.textChanged.connect(lambda :self.textchanged(self.e1))
        #e3.editingFinished.connect(self.enter)
        e3=QLineEdit()
        e3.setInputMask('+99_5559_999999')
        flo=QFormLayout()
        flo.addRow("int",e1)
        flo.addRow("int", e2)
        flo.addRow("int", e3)
        self.setLayout(flo)
        self.setWindowTitle('nihao')

    def textchanged(self,b):
        print('输入的内容为'+b.Text())

    def enter(self):
        print('已输入值')



if __name__=='__main__':
    app=QApplication(sys.argv)
    icon=lineEditDemo()
    icon.show()
    sys.exit(app.exec_())

