import sys
from PyQt5.Qt import *
from resource.restart_ai_on_opt import Ui_Form


class OneKey(QWidget, Ui_Form):
    send_info_signal = pyqtSignal(int)
    step_num = 1

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def next_step(self):
        if self.step_num == 4:
            QCoreApplication.quit()
            sys.exit()
        if self.step_num != 2:
            self.show_img(self.step_num)
            return
        reply = QMessageBox.question(self, "", "EL 外是否有组件?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.send_info_signal.emit(1)
        elif reply == QMessageBox.No:
            self.send_info_signal.emit(0)
        self.show_img(self.step_num)

    def show_img(self, num):
        self.load_img = QPixmap(f'./resource/img/{num}.jpg')
        self.img_file = self.load_img.scaled(self.img_lb.size(), aspectRatioMode=Qt.KeepAspectRatio)
        self.img_lb.setPixmap(self.img_file)
        if self.step_num == 3:
            self.confim.setText("OK")
        self.step_num += 1


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = OneKey()
    window.show()
    sys.exit(app.exec_())
