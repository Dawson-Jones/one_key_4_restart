import time
from PyQt5.Qt import *
from resource.restart_ai_on_opt import Ui_Form
from restart_process import one_key


class OneKey(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = OneKey()
    window.show()
    sys.exit(app.exec_())
