# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restart_ai_on_opt.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.img_lb = QtWidgets.QLabel(Form)
        self.img_lb.setText("")
        self.img_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.img_lb.setObjectName("img_lb")
        self.verticalLayout.addWidget(self.img_lb)
        self.confim = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confim.sizePolicy().hasHeightForWidth())
        self.confim.setSizePolicy(sizePolicy)
        self.confim.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.confim.setObjectName("confim")
        self.verticalLayout.addWidget(self.confim)
        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)
        self.confim.clicked.connect(Form.next_step)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.confim.setText(_translate("Form", "下一步/next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
