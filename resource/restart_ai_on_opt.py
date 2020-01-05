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
        self.cn_lb = QtWidgets.QLabel(Form)
        self.cn_lb.setStyleSheet("font: 18pt \"Ubuntu Mono\";")
        self.cn_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.cn_lb.setObjectName("cn_lb")
        self.verticalLayout.addWidget(self.cn_lb)
        self.en_lb = QtWidgets.QLabel(Form)
        self.en_lb.setStyleSheet("font: 18pt \"Ubuntu Mono\";")
        self.en_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.en_lb.setObjectName("en_lb")
        self.verticalLayout.addWidget(self.en_lb)
        self.confim = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confim.sizePolicy().hasHeightForWidth())
        self.confim.setSizePolicy(sizePolicy)
        self.confim.setObjectName("confim")
        self.verticalLayout.addWidget(self.confim)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cn_lb.setText(_translate("Form", "启动opt电脑上的AI重置程序"))
        self.en_lb.setText(_translate("Form", "Start the AI reset program on the opt computer"))
        self.confim.setText(_translate("Form", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
