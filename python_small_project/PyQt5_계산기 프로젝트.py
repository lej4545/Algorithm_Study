import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('cal_main_ui.ui')[0]

class DemoForm(QMainWindow, form_class):
    cal_type = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def Radio1Click(self):
        DemoForm.cal_type = "+"
        print(DemoForm.cal_type)
    def Radio2Click(self):
        DemoForm.cal_type = "-"
        print(DemoForm.cal_type)
    def Radio3Click(self):
        DemoForm.cal_type = "*"
        print(DemoForm.cal_type)
    def Radio4Click(self):
        DemoForm.cal_type = "/"
        print(DemoForm.cal_type)

    def ButtonResultClick(self):
        print(DemoForm.cal_type)
        if DemoForm.cal_type == "+":
            result = int(self.text_In1.toPlainText()) + int(self.text_In2.toPlainText())
            self.label.setText(str(result))
        elif DemoForm.cal_type == "-":
            result = int(self.text_In1.toPlainText()) - int(self.text_In2.toPlainText())
            self.label.setText(str(result))
        elif DemoForm.cal_type == "*":
            result = int(self.text_In1.toPlainText()) * int(self.text_In2.toPlainText())
            self.label.setText(str(result))
        elif DemoForm.cal_type == "/":
            if int(self.text_In2.toPlainText()) != 0:
                result = int(self.text_In1.toPlainText()) / int(self.text_In2.toPlainText())
                self.label.setText(str(result))
            else:
                QMessageBox.about(self,'message','0 나누기 에러')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()