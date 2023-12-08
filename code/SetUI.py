from PyQt5.QtCore import Qt
from SetButtons import *
import FoodManagement as _FM

# window, page마다 배치할 label의 text가 저장된 dictionary
label_dict = {"main": "점심 메뉴 추천",
              "classify": ("오늘의 예산은?", "음식 종류는...", "탄수화물은...", "주재료는...", "맵기는...", "온도는..."),
              "classify_success": "오늘 점심은",
              "classify_fail": "조건을 만족하는 음식이 없어요.\n더 많은 옵션을 골라보는 건 어때요?",
              "random": ""}

# window, page마다 배치할 button의 text가 저장된 dictionary
button_dict = {"main": ("취향 분석 추천", "랜덤 추천"),
               "classify": (("~8000원", "~12000원", "무제한!"),
                            ("한식", "양식", "중식", "일식", "동남아식", "간편식"),
                            ("밥", "빵", "면", "기타"),
                            ("고기", "해산물", "기타"),
                            ("맵게", "매콤하게", "안맵게"),
                            ("뜨끈하게", "시원하게")),
               "classify_success": "다시 하기",
               "classify_fail": "다시 하기",
               "random": ""}


# UI 설정 클래스
# window와 layout을 설정함
class SetUI(QDialog):

    # Window 설정 method
    # 창 이름(title), 아이콘, (x, y, w, h) 설정
    def setWindow(self, title):
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('lunch_time.png'))
        self.setGeometry(300, 300, 600, 600)

    # 전체 layout 설정 method
    # 모든 widget이 배치된 vbox를 반환함
    def setParentVbox(self, dict_key, question_index=None):

        # main window layout 설정
        if dict_key == "main":
            vbox = SetUI.setLabel(self, label_dict[dict_key])
            vbox = SetUI.mainButtons(self, vbox, button_dict[dict_key])

        # classify window layout 설정
        elif dict_key == "classify":
            vbox = SetUI.setLabel(self, label_dict[dict_key][question_index])
            button_texts = button_dict[dict_key][question_index]

            # 첫 번째 page layout 설정
            if question_index == 0:
                vbox = SetUI.stackProceedButtons(self, vbox, button_texts)

            # 이외 page layout 설정
            else:
                # option이 4개 이상이면 split 형태로 option 버튼 배치
                if len(button_texts) > 3:
                    vbox = SetUI.splitOptionButtons(self, vbox, button_texts)

                # option이 4개 미만이면 stack 형태로 option 버튼 배치
                else:
                    vbox = SetUI.stackOptionButtons(self, vbox, button_texts)

                # 공통(다음) 버튼 배치
                # 마지막 질문이면 "다음" 버튼 text를 "결과 보기" 버튼으로 변경
                if question_index == len(button_dict):
                    vbox = SetUI.classifyDefaultButtons(self, vbox, is_last=True)
                else:
                    vbox = SetUI.classifyDefaultButtons(self, vbox, is_last=False)

        # classify window - success page layout 설정
        elif dict_key == "classify_success":
            # label에 추천 음식 추가
            random_food = _FM.FoodManagement.selectRandomFood(self)
            label = label_dict[dict_key] + f"\n[{random_food}]\n어때요?"
            vbox = SetUI.setLabel(self, label)
            vbox = SetUI.classifyResultButtons(self, vbox, button_dict[dict_key])

        # classify window - fail page layout 설정
        elif dict_key == "classify_fail":
            vbox = SetUI.setLabel(self, label_dict[dict_key])
            vbox = SetUI.classifyResultButtons(self, vbox, button_dict[dict_key])

        else:
            print("label_key값 오류")
            return

        return vbox

    # label 배치 method
    # label: 맑은 고딕, 20pt, bold, 중앙 정렬
    def setLabel(self, label_text):
        label = QLabel(label_text)
        font = label.font()
        font.setPointSize(20)
        font.setFamily("맑은 고딕")
        font.setBold(True)
        label.setFont(font)

        # 수평 중앙 정렬
        label.setAlignment(Qt.AlignHCenter)

        # 수직 중앙 정렬 (위아래로 stretch)
        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(label)
        vbox.addStretch()

        return vbox

    # main window에 버튼 배치하는 method
    # "취향 분석 추천", "랜덤 추천" (next)버튼 배치
    def mainButtons(self, vbox, button_texts):
        buttons = [MakeButton.setNextButton(self, button_text) for button_text in button_texts]
        for button in buttons:
            vbox.addWidget(button)
        return vbox

    # classify window 첫번째 page에 버튼 배치하는 method
    # "4000~8000원", "8000~12000원", "무제한!" (proceed)버튼 배치
    def stackProceedButtons(self, vbox, button_texts):
        buttons = [MakeButton.setProceedButton(self, button_text) for button_text in button_texts]
        for button in buttons:
            vbox.addWidget(button)
        return vbox

    # classify window 두번째 page부터 나타낼 option 버튼 배치하는 method
    # option이 4개 미만일 경우
    def stackOptionButtons(self, vbox, button_texts):
        buttons = [MakeButton.setOptionButton(self, button_text) for button_text in button_texts]
        for button in buttons:
            vbox.addWidget(button)
        return vbox

    # classify window 두번째 page부터 나타낼 option 버튼 >분할< 배치하는 method
    # option이 4개 이상일 경우
    def splitOptionButtons(self, vbox, button_texts):
        buttons = [MakeButton.setOptionButton(self, button_text) for button_text in button_texts]
        hbox = QHBoxLayout()
        for i in range(len(buttons)):
            hbox.addWidget(buttons[i])
            if i % 2 != 0:
                vbox.addLayout(hbox)
                hbox = QHBoxLayout()
        return vbox

    # classify window 두번째 page부터 공통으로 나타낼 버튼 배치하는 method
    # 마지막 질문이면 "결과 보기" 버튼, 이외엔 "다음" (proceed)버튼 배치
    def classifyDefaultButtons(self, vbox, is_last):
        if is_last:
            vbox.addWidget(MakeButton.setProceedButton(self, "결과 보기"))
        else:
            vbox.addWidget(MakeButton.setProceedButton(self, "다음"))
        return vbox

    # classify window 결과(fail, success) page에 나타낼 버튼 배치하는 method
    # "다시 하기"(again) 버튼 배치
    def classifyResultButtons(self, vbox, button_text):
        again_button = MakeButton.setAgianButton(self, button_text)
        vbox.addWidget(again_button)
        return vbox
