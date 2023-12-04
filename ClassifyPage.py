from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import PyQt5.QtWidgets as QtWidgets
import SetButtons
import SetUI
# from SetUI import *


# 분류 추천 페이지 클래스
# 여러 질문을 거쳐 조건에 맞는 n개의 음식을 추천 한다
class ClassifyPage(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.question_index = 0
        self.initUI()

    def initUI(self):
        # layout 설정 method 호출
        SetUI.SetUI.setPage(self, "classify", self.question_index)

        # Window 속성 설정 method 호출
        SetUI.SetUI.setWindow(self, "점메추 - 취향 분석 추천")

        # 창을 띄움
        self.show()

    def resetUI(self):
        SetUI.SetUI.setPage(self, "classify", self.question_index)
        self.show()

    def getQuestionIndex(self):
        return self.question_index

    def setQuestionIndex(self, question_index):
        self.question_index = question_index
