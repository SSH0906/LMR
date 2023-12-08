from PyQt5.QtWidgets import *
import FoodManagement as _FM
import SetUI as _UI


# 랜덤 추천 window 클래스
# 모든 음식을 랜덤으로 돌려 1개의 음식을 뽑는다
class RandomPage(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stackedWidget = None
        print("ㅡfood_table 초기화ㅡ")
        _FM.FoodManagement.initFoodTable(self)
        print("ㅡfood_table 초기화 완료ㅡ\n")
        self.initUI()

    # UI 초기화 method
    def initUI(self):
        # stackedWidget 페이지 생성, UI 설정
        self.stackedWidget = QStackedWidget()
        page = QWidget()
        page.setLayout(_UI.SetUI.setParentVbox(self, "random"))
        self.stackedWidget.addWidget(page)

        # layout 설정
        parent_vbox = QVBoxLayout()
        parent_vbox.addWidget(self.stackedWidget)
        self.setLayout(parent_vbox)

        # Window 속성 설정 method 호출
        _UI.SetUI.setWindow(self, "점메추 - 랜덤 추천")

        # 창을 띄움
        self.show()

    # 외부에서 stackedWidget에 접근할 수 있도록 하는 method
    def getStackedWidget(self):
        return self.stackedWidget
