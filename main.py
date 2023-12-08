import sys
from SetUI import *


# 메인 창 클래스
# "점심 메뉴 추천" label 아래로 "취향 분석 추천", "랜덤 추천" (next)버튼을 배치한 window
class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    # UI 초기화 method
    def initUI(self):
        # 전체 layout을 설정하는 method 호출
        parent_vbox = SetUI.setParentVbox(self, "main")

        # layout 설정
        self.setLayout(parent_vbox)

        # Window 속성 설정 method 호출
        SetUI.setWindow(self, "점메추")

        # 창을 띄움
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
