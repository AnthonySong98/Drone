import sys
from PyQt5.QtWidgets import QWidget,QApplication,QToolTip,QLabel,QVBoxLayout
from PyQt5.QtGui import QIcon,QFont

class Icon(QWidget):
    def __init__(self):
        super(Icon,self).__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('这是一个<b>气泡</b>')
        self.setGeometry(200,300,400,400)
        self.setWindowTitle('程序图标')
        self.setWindowIcon(QIcon('E:\python3/icon/2.ico'))


if __name__=='__main__':
    app=QApplication(sys.argv)
    icon=Icon()
    icon.show()
    sys.exit(app.exec_())

