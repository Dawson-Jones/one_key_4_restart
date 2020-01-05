import sys
from PyQt5.Qt import *
from restart_process import one_key
from gui import OneKey


def main():
    one_key()
    app = QApplication(sys.argv)
    window = OneKey()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
