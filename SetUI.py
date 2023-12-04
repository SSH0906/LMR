from PyQt5.QtCore import Qt
from SetButtons import *

label_dict = {"main": "점심 메뉴 추천",
              "classify": ("오늘의 예산은?", "음식 종류는...", "탄수화물은...", "주재료는...", "맵기는...", "온도는..."),
              "random": ""}

button_dict = {"main": ("취향 분석 추천", "랜덤 추천"),
               "classify": (("4000~8000원", "8000~12000원", "무제한!"),
                            ("한식", "양식", "중식", "일식", "동남아식", "간편식"),
                            ("밥", "빵", "면", "기타"),
                            ("고기", "해산물", "기타"),
                            ("맵게", "매콤하게", "안맵게"),
                            ("뜨끈하게", "시원하게", "상관없음!")),
               "random": ""}


class SetUI(QDialog):
    # Window 양식 설정 method
    # 창 이름(title), 아이콘, (x, y, w, h) 설정
    def setWindow(self, title):
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('lunch_time.png'))
        self.setGeometry(300, 300, 600, 600)

    # layout 설정 method
    def setPage(self, dict_key, question_index=None):

        # main page layout 설정
        if dict_key == "main":
            vbox = SetUI.setLabel(self, label_dict[dict_key])
            vbox = SetUI.mainButtons(self, vbox, button_dict[dict_key])

        # classify page layout 설정
        elif dict_key == "classify":
            vbox = SetUI.setLabel(self, label_dict[dict_key][question_index])
            button_texts = button_dict[dict_key][question_index]

            # 첫 번째 질문 layout 설정
            if question_index == 0:
                vbox = SetUI.stackProceedButtons(self, vbox, button_texts)

            # 이외 질문 layout 설정
            else:
                # option이 4개 이상이면 split 형태로 option 버튼 배치
                if len(button_texts) > 3:
                    vbox = SetUI.splitOptionButtons(self, vbox, button_texts)

                # option이 4개 미만이면 stack 형태로 option 버튼 배치
                else:
                    vbox = SetUI.stackOptionButtons(self, vbox, button_texts)

                # 공통(랜덤, 다음) 버튼 배치
                vbox = SetUI.classifyDefaultButtons(self, vbox)

        else:
            print("label_key값 오류")
            return

        # layout 적용
        self.setLayout(vbox)

    def setLabel(self, label_text):
        label = QLabel(label_text)
        font = label.font()
        font.setPointSize(20)
        font.setFamily("맑은 고딕")
        font.setBold(True)
        label.setFont(font)
        label.setAlignment(Qt.AlignHCenter)

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(label)
        vbox.addStretch()

        return vbox

    # main page에 나타낼 next 버튼 배치
    def mainButtons(self, vbox, button_texts):
        buttons = [MakeButton.setNextButton(self, button_text) for button_text in button_texts]
        for button in buttons:
            vbox.addWidget(button)
        return vbox

    # classify page 예산 질문에 나타낼 proceed 버튼 배치
    def stackProceedButtons(self, vbox, button_texts):
        buttons = [MakeButton.setProceedButton(self, button_text) for button_text in button_texts]
        for button in buttons:
            vbox.addWidget(button)
        return vbox

    # classify page 질문에 나타낼 option 버튼 분할 배치 (option이 4개 미만일 경우)
    def stackOptionButtons(self, vbox, button_texts):
        buttons = [MakeButton.setOptionButton(self, button_text) for button_text in button_texts]
        for button in buttons:
            vbox.addWidget(button)
        return vbox

    # classify page 질문에 나타낼 option 버튼 배치 (option이 4개 이상일 경우)
    def splitOptionButtons(self, vbox, button_texts):
        buttons = [MakeButton.setOptionButton(self, button_text) for button_text in button_texts]
        hbox = QHBoxLayout()
        for i in range(len(buttons)):
            hbox.addWidget(buttons[i])
            if i % 2 != 0:
                vbox.addLayout(hbox)
                hbox = QHBoxLayout()
        return vbox

    # classify page 질문에 (예산 질문 제외)공통으로 나타낼 random(랜덤), proceed(다음) 버튼 배치
    def classifyDefaultButtons(self, vbox):
        hbox = QHBoxLayout()
        hbox.addWidget(MakeButton.setRandomButton(self, "랜덤"))
        hbox.addWidget(MakeButton.setProceedButton(self, "다음"))
        vbox.addLayout(hbox)
        return vbox
