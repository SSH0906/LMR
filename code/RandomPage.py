from SetButtons import *


# 랜덤 추천 페이지 클래스
# 모든 음식을 랜덤으로 돌려 1개의 음식을 뽑는다
class RandomPage(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindow()
        self.show()

    # Window 양식 설정 method
    # 창 이름(점메추), 아이콘, (x, y, w, h) 설정
    def setWindow(self):
        self.setWindowTitle('점메추 - 랜덤 추천')
        self.setWindowIcon(QIcon('lunch_time.png'))
        self.setGeometry(300, 300, 600, 600)
