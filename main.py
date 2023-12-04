import sys
from SetUI import *


class MainPage(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # layout 설정 method 호출
        layout = SetUI.setPage(self, "main")
        self.setLayout(layout)

        # Window 속성 설정 method 호출
        SetUI.setWindow(self, "점메추")

        # 창을 띄움
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainPage()
    sys.exit(app.exec_())
