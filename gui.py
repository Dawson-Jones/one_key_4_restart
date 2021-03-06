from PyQt5.Qt import *
from resource.restart_ai_on_opt import Ui_Form


class OneKey(QWidget, Ui_Form):
    send_info_signal = pyqtSignal(int)
    restart_signal = pyqtSignal()
    step_num = 1

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)  # don't show title bar
        self.right_top()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def right_top(self):
        screen = QDesktopWidget().screenGeometry()
        # size = self.geometry()
        self.resize(screen.width() // 2, screen.height() // 2)
        self.move(
            screen.width() - screen.width() // 2,
            0
        )

    def next_step(self):
        if self.step_num == 5:
            self.close()
            return
        if self.step_num != 2:
            self.show_img()
            return
        reply = QMessageBox.question(self, "", "EL 外是否有组件?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.send_info_signal.emit(1)
        elif reply == QMessageBox.No:
            self.send_info_signal.emit(0)
        self.show_img()

    def show_img(self):
        if self.step_num == 1:
            self.restart_signal.emit()

        self.load_img = QPixmap(f'./resource/img/{self.step_num}.jpg')
        self.img_file = self.load_img.scaled(self.img_lb.size(), aspectRatioMode=Qt.KeepAspectRatio)
        self.img_lb.setPixmap(self.img_file)
        if self.step_num == 4:
            self.confim.setText("OK")
        self.step_num += 1

    def send_failed(self):
        QMessageBox.information(self, '', '发送plc失败', QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = OneKey()
    window.show()
    sys.exit(app.exec_())
