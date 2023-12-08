from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ButtonFunction import ButtonFunction


# option 버튼 스타일 지정 클래스
# option button: 맑은 고딕, 13pt, rgb(251, 86, 7)
class QPushButtonOption(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("맑은 고딕", 13)
        self.setFont(font)
        self.setStyleSheet("color: rgb(251, 86, 7);"
                           "background-color: white;"
                           "border: 2px solid rgb(251, 86, 7);"
                           "border-radius: 5px;")


# next 버튼 스타일 지정 클래스
# next button: 맑은 고딕, 13pt, bold, rgb(255, 0, 110)
class QPushButtonNext(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("맑은 고딕", 13)
        font.setBold(True)
        self.setFont(font)
        self.setStyleSheet("color: rgb(255, 0, 110);"
                           "background-color: white;"
                           "border: 2px solid rgb(255, 0, 110);"
                           "border-radius: 5px;")


# random 버튼 스타일 지정 클래스
# random button: 맑은 고딕, 13pt, rgb(131, 56, 236)
class QPushButtonRandom(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("맑은 고딕", 13)
        self.setFont(font)
        self.setStyleSheet("color: rgb(131, 56, 236);"
                           "background-color: white;"
                           "border: 2px solid rgb(131, 56, 236);"
                           "border-radius: 5px;")


# proceed 버튼 스타일 지정 클래스
# proceed button: 맑은 고딕, 13pt, bold, rgb(58, 134, 255)
class QPushButtonProceed(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("맑은 고딕", 13)
        font.setBold(True)
        self.setFont(font)
        self.setStyleSheet("color: rgb(58, 134, 255);"
                           "background-color: white;"
                           "border: 2px solid rgb(58, 134, 255);"
                           "border-radius: 5px;")


# again 버튼 스타일 지정 클래스
# again button: 맑은 고딕, 13pt, bold, rgb(58, 134, 255)
class QPushButtonAgain(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QFont("맑은 고딕", 13)
        font.setBold(True)
        self.setFont(font)
        self.setStyleSheet("color: rgb(58, 134, 255);"
                           "background-color: white;"
                           "border: 2px solid rgb(58, 134, 255);"
                           "border-radius: 5px;")


# 버튼 생성 클래스
# 프로젝트에서 사용될 모든 버튼 set method를 가짐
class MakeButton(QDialog):

    # option 버튼 생성 method
    # 클릭 시 toggleButton method 호출
    def setOptionButton(self, button_text):
        # 버튼 생성
        button = QPushButtonOption(self)
        button.setText(button_text)
        button.setCheckable(True)

        # 버튼을 누르면 toggleButton method 호출
        button.clicked.connect(lambda: ButtonFunction.toggleButton(self, button))
        return button

    # next 버튼 생성 method
    # 클릭 시 movePage method 호출
    def setNextButton(self, button_text):
        # 버튼 생성
        button = QPushButtonNext(self)
        button.setText(button_text)
        button.setCheckable(True)

        # 버튼을 누르면 movePage method 호출
        button.clicked.connect(lambda: ButtonFunction.movePage(self, button))
        return button

    # random 버튼 생성 method
    # 클릭 시 randomOption 호출
    def setRandomButton(self, button_text):
        # 버튼 생성
        button = QPushButtonRandom(self)
        button.setText(button_text)
        button.setCheckable(True)

        # 버튼을 누르면 randomOption 호출
        button.clicked.connect(lambda: ButtonFunction.randomOption(self, button))
        return button

    # proceed 버튼 생성 method
    # 클릭 시 progressQuestion 호출
    def setProceedButton(self, button_text):
        # 버튼 생성
        button = QPushButtonProceed(self)
        button.setText(button_text)
        button.setCheckable(True)

        # 버튼을 누르면 progressQuestion 호출
        button.clicked.connect(lambda: ButtonFunction.progressQuestion(self, button_text))
        return button

    # again 버튼 생성 method
    # 클릭 시 reclassify 호출
    def setAgianButton(self, button_text):
        # 버튼 생성
        button = QPushButtonAgain(self)
        button.setText(button_text)
        button.setCheckable(True)

        # 버튼을 누르면 reclassify 호출
        button.clicked.connect(lambda: ButtonFunction.reclassify(self))
        return button
