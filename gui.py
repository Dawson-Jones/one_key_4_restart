from PyQt5.Qt import *
from resource.restart_ai_on_opt import Ui_Form


class OneKey(QWidget, Ui_Form):
    step_num = 1

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def next_step(self):
        if self.step_num == 1:
            self.confirm_widget()
        if self.step_num == 2:
            self.el_set_0()

    def confirm_widget(self):
        self.cn_lb.setText("确认EL外是否有组件")
        self.en_lb.setText("Confirm if there are widget outside the EL")
        self.step_num += 1


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = OneKey()
    window.show()
    sys.exit(app.exec_())
