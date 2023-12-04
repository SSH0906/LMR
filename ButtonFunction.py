import random
import SetUI

from PyQt5.QtWidgets import *
from ClassifyPage import ClassifyPage
from RandomPage import RandomPage


class ButtonFunction(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.second = None

    # option 버튼이 눌리면 실행될 method
    # 스타일을 변경함
    #
    def toggleButton(self, button):
        print(button.isChecked())
        if button.isChecked():
            button.setCheckable(False)
            button.setStyleSheet("color: white;"
                                 "background-color: rgb(251, 86, 7);"
                                 "border-radius: 5px;")
        else:
            button.setCheckable(True)
            button.setStyleSheet("color: rgb(251, 86, 7);"
                                 "background-color: white;"
                                 "border: 2px solid rgb(251, 86, 7);"
                                 "border-radius: 5px;")

    # next 버튼이 눌리면 실행될 method
    # 다음 페이지로 넘어감
    def movePage(self, button):
        self.hide()
        if button.text() == "랜덤 추천":
            self.second = RandomPage()
        elif button.text() == "취향 분석 추천":
            self.second = ClassifyPage()
        self.second.exec()
        self.show()

    # random 버튼이 눌리면 실행될 method
    # q_label_index를 확인하고 질문에 맞는 옵션을 랜덤하게 고름
    def randomOption(self, button):
        if button.isChecked():
            random_option = random.choice(ClassifyPage.getQOption(self))
            print(random_option)
            button.setCheckable(False)
            button.setStyleSheet("color: white;"
                                 "background-color: rgb(131, 56, 236);"
                                 "border-radius: 5px;")
        else:
            button.setCheckable(True)
            button.setStyleSheet("color: rgb(131, 56, 236);"
                                 "background-color: white;"
                                 "border: 2px solid rgb(131, 56, 236);"
                                 "border-radius: 5px;")

    # proceed 버튼이 눌리면 실행될 method
    # 현재 layout을 초기화 하고 새 layout 적용하여 다음 질문으로 넘어감
    def progressQuestion(self, button_text):
        # 현재 layout의 모든 widget과 item을 삭제하여 초기화
        ButtonFunction.clearPage(self)
        # if button_text == "추천 결과":
        #     # 결과창
        #     pass
        # else:
        #     try:
        #         # 다음 질문으로
        #         question_index = ClassifyPage.getQuestionIndex(self)
        #         question_index += 1
        #         ClassifyPage.setQuestionIndex(self, question_index)
        #         SetUI.SetUI.setPage(self, "classify", question_index)
        #     except Exception as e:
        #         print(e)

    def clearPage(self):
        for i in reversed(range(self.layout().count())):
            if self.layout().itemAt(i).widget() is not None:
                self.layout().removeWidget(self.layout().itemAt(i).widget())
            else:
                self.layout().removeItem(self.layout().itemAt(i))
