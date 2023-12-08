from PyQt5.QtWidgets import *
import SetUI


# 분류 추천 페이지 클래스
# 여러 질문을 거쳐 조건에 맞는 n개의 음식을 추천 한다
class ClassifyPage(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.question_index = 0
        self.stackedWidget = None
        self.initUI()

    def initUI(self):
        self.stackedWidget = QStackedWidget()
        question_num = len(SetUI.button_dict["classify"])
        for self.question_index in range(question_num):
            page = QWidget()
            page.setLayout(SetUI.SetUI.setPage(self, "classify", self.question_index))
            self.stackedWidget.addWidget(page)

        self.stackedWidget.setCurrentIndex(0)

        layout = QVBoxLayout()
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)
        self.show()

        # Window 속성 설정 method 호출
        SetUI.SetUI.setWindow(self, "점메추 - 취향 분석 추천")

        # 창을 띄움
        self.show()

    def getStackedWidget(self):
        return self.stackedWidget
