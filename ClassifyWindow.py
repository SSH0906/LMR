from PyQt5.QtWidgets import *
import FoodManagement as _FM
import SetUI as _UI


# 취향 분석 추천 창 클래스
# n개의 질문과 결과를 stackedWidget으로 구성
# 랜덤값 또는 사용자 선택값을 받아 실시간으로 분류, 테이블을 구성함
# 결과적으로 조건에 맞는 n개의 음식을 추천 한다
class ClassifyWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.question_index = 0
        self.stackedWidget = None
        print("ㅡ분류 준비ㅡ")
        _FM.FoodManagement.readyClassifying(self, is_first=True)
        print("ㅡ준비 완료ㅡ\n")
        self.initUI()

    # UI 초기화 method
    def initUI(self):
        # stackedWidget 페이지 생성 method 호출, UI 설정
        self.makeStackedWidgetPage()

        # layout 설정
        parent_vbox = QVBoxLayout()
        parent_vbox.addWidget(self.stackedWidget)
        self.setLayout(parent_vbox)

        # Window 속성 설정 method 호출
        _UI.SetUI.setWindow(self, "점메추 - 취향 분석 추천")

        # 창을 띄움
        self.show()

    # stackedWidget 페이지 생성 method
    # 질문 개수 + 2(분류 성공, 실패 페이지)만큼 페이지 stack
    def makeStackedWidgetPage(self):
        # stackedWidget 생성
        self.stackedWidget = QStackedWidget()

        # 질문 페이지 생성 및 적용
        question_num = len(_UI.button_dict["classify"])
        for self.question_index in range(question_num):
            page = QWidget()
            page.setLayout(_UI.SetUI.setParentVbox(self, "classify", self.question_index))
            self.stackedWidget.addWidget(page)

        # 분류 성공 페이지 생성 및 적용
        # page = QWidget()
        # page.setLayout(_UI.SetUI.setParentVbox(self, "classify_success"))
        # self.stackedWidget.addWidget(page)

        # 분류 실패 페이지 생성 및 적용
        page = QWidget()
        page.setLayout(_UI.SetUI.setParentVbox(self, "classify_fail"))
        self.stackedWidget.addWidget(page)

        # 초기 페이지 설정
        self.stackedWidget.setCurrentIndex(0)

    # 외부에서 stackedWidget에 접근할 수 있도록 하는 method
    # 현재 몇 페이지에 있는지(몇 번째 질문인지) 알 수 있게 하기 위함
    def getStackedWidget(self):
        return self.stackedWidget

    def setStackedWidget(self, stackedWidget):
        self.stackedWidget = stackedWidget
