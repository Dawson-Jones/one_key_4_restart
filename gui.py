from PyQt5.Qt import *
from resource.restart_ai_on_opt import Ui_Form


class OneKey(QWidget, Ui_Form):
    step_num = 1

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def next_step(self):
        self.show_img(self.step_num)

    def show_img(self, num):
        self.load_img = QPixmap(f'./resource/img/{num}.jpg')
        self.img_file = self.load_img.scaled(self.img_lb.size(), aspectRatioMode=Qt.KeepAspectRatio)
        self.img_lb.setPixmap(self.img_file)
        self.step_num += 1


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = OneKey()
    window.show()
    sys.exit(app.exec_())
