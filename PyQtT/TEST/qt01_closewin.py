from PyQt5.QtWidgets import QMainWindow,QHBoxLayout,QPushButton,QApplication,QWidget
import sys

class winform(QMainWindow):
    def __init__(self):
        super(winform,self).__init__()
        self.setWindowTitle('关闭主窗口的例子')
        self.button1=QPushButton('关闭主窗口')
        self.button1.clicked.connect(self.clickbutton)

        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame=QWidget()  #小部件
        main_frame.setLayout(layout) #小部件的布局
        self.setCentralWidget(main_frame)  #把部件放进去 。

    def clickbutton(self):
        sender=self.sender()
        print(sender.text()+'被按下去了')
        qapp=QApplication.instance()
        qapp.quit()


if __name__=="__main__":
    app=QApplication(sys.argv)
    form=winform()
    form.show()
    sys.exit(app.exec_())
