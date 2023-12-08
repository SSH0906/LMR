from PyQt5.QtWidgets import QDialog, QWidget
from ClassifyWindow import ClassifyWindow
# from RandomPage import RandomPage
import FoodManagement as _FM
import SetUI as _UI
import random


# 버튼 function 클래스
# 프로젝트에서 사용될 모든 버튼의 function method를 가짐
class ButtonFunction(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.second = None

    # option 버튼이 눌리면 실행될 method
    # 스타일을 변경함 (선택-색칠된 버튼, 해제-하얀 버튼)
    # 선택된 option 버튼은 버튼의 text를 now_selected_options에 저장함
    # 선택 후 해제된 option 버튼은 버튼의 text를 now_selected_options 또는 selected_options에서 삭제함
    def toggleButton(self, button):
        if button.isChecked():
            button.setCheckable(False)
            button.setStyleSheet("color: white;"
                                 "background-color: rgb(251, 86, 7);"
                                 "border-radius: 5px;")
            # 선택된 option 버튼의 text를 now_selected_options에 저장
            _FM.now_selected_options.append(button.text())
        else:
            button.setCheckable(True)
            button.setStyleSheet("color: rgb(251, 86, 7);"
                                 "background-color: white;"
                                 "border: 2px solid rgb(251, 86, 7);"
                                 "border-radius: 5px;")
            # 현재 해제한 option이 now_selected_options에 있으면 remove, 없으면 selected_options에서 remove
            # 재분류 시 발생하는 문제 방지
            if button.text() in _FM.now_selected_options:
                _FM.now_selected_options.remove(button.text())
            else:
                stackedWidget = ClassifyWindow.getStackedWidget(self)
                question_index = stackedWidget.currentIndex()
                if button.text() in _FM.selected_options[question_index]:
                    _FM.selected_options[question_index].remove(button.text())

    # next 버튼이 눌리면 실행될 method
    # 새 window를 띄움
    def movePage(self, button):
        self.hide()
        if button.text() == "취향 분석 추천":
            print("취향 분석 추천 window 생성")
            self.second = ClassifyWindow()
        # elif button.text() == "랜덤 추천":
        #     self.second = RandomPage()
        self.second.exec()
        self.show()

    # random 버튼이 눌리면 실행될 method
    # todo: 무작위로 선택된 option을 text 키워드에 저장, 선택된 option button은 스타일 변경
    # 사용 보류
    def randomOption(self, button):
        if button.isChecked():
            # random_option = random.choice(ClassifyWindow.getQOption(self))
            # print(random_option)
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
    # TODO: now_selected_options가 비어있다면 경고창을 띄워야 함
    # alterFoodTable method를 호출하여 food_table을 option에 따라 분류함
    # food_table이 비어있지 않다면 current index를 증가시켜 다음 page로 넘어감
    # food_table이 비었다면 분류 중단, 마지막 page로 이동함
    def progressQuestion(self, button_text):
        # 예산을 묻는 (첫번째)질문이면 progress 버튼이 눌렸으므로 배열에 option이 저장되지 않음
        # option을 별도로 저장함
        if button_text != "다음" and button_text != "결과 보기":
            _FM.now_selected_options.append(button_text)

        # current index를 가져옴
        stackedWidget = ClassifyWindow.getStackedWidget(self)
        page_index = stackedWidget.currentIndex()

        # alterFoodTable method를 호출, food_table을 option에 따라 분류
        _FM.FoodManagement.alterFoodTable(self, question_num=page_index)

        # food_table이 비어있지 않다면
        if len(_FM.food_table) != 0:
            # 눌린 버튼이 "결과 보기"라면 결과 page 생성 및 적용
            if button_text == "결과 보기":
                page = QWidget()
                page.setLayout(_UI.SetUI.setParentVbox(self, "classify_success"))
                print(stackedWidget.count())
                stackedWidget.addWidget(page)
                print(stackedWidget.count())
                ClassifyWindow.setStackedWidget(self, stackedWidget)
                stackedWidget = ClassifyWindow.getStackedWidget(self)
                print(stackedWidget)
            # current index를 증가시켜 다음 page로 넘어감
            stackedWidget.setCurrentIndex(page_index + 1)

        # food_table이 비었다면 분류 중단, 분류 실패 페이지로 이동
        else:
            page_index = stackedWidget.count()
            stackedWidget.setCurrentIndex(page_index - 1)

    # again 버튼이 눌리면 실행될 method
    # 재분류 준비 후 classifyWindow의 첫 page로 이동
    def reclassify(self):
        print("ㅡ분류 준비ㅡ")
        _FM.selected_options[0] = []
        _FM.FoodManagement.readyClassifying(self, is_first=False)
        print("ㅡ준비 완료ㅡ\n")
        stackedWidget = ClassifyWindow.getStackedWidget(self)
        stackedWidget.setCurrentIndex(0)
