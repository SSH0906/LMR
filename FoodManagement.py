import random

# 무작위로 고를 음식이 dictionary로 저장(food_dict)될 배열
# dictionary: {"음식 이름": _, "가격": _, "음식 계열": _, "주재료": _, "부재료": _, "매운 정도": _, "온도": _}
# 선호도(가중치), 비고는 보류...
food_table = []

# food_dict의 key 별도 저장
# sheet의 첫번째 줄을 불러와 해당 값을 food_dict의 key로 사용
with open("FoodData.csv", 'r', encoding='utf-8-sig') as f:
    food_dict_keys = [word.strip() for word in f.readline().split(',')]

# 고른 option이 임시로 저장될 배열
# 이 배열에 저장된 option을 기반으로 food_table 내 음식 삭제
now_selected_options = []

# 골랐던 모든 option이 저장될 2차원 배열
# 재분류 시 필요, classifyWindow를 새로 띄울 때만 초기화
selected_options = []


# 테이블 관리 클래스
# category_keywords를 기반으로 food_table 축소?
class FoodManagement:
    # 분류 시작 전 분류에 사용될 변수를 초기화 하는 method
    # classifyWindow를 새로 띄울 때 실행됨
    # is_first로 첫분류인지 재분류인지 확인, 첫분류면 selected_options까지 초기화
    def readyClassifying(self, is_first):
        if is_first:
            print("첫분류 준비")
            global selected_options
            selected_options = []
        else:
            print("재분류 준비")
        FoodManagement.initArr(self)
        FoodManagement.initFoodTable(self)

    # food_table, now_selected_options를 비우는 method
    def initArr(self):
        print("food_table, now_selected_options 요소 삭제")
        global food_table, now_selected_options
        food_table, now_selected_options = [], []

    # food_table을 초기화 하는 method
    # FoodData.csv 파일의 모든 음식을 dictionary 형태로 food_table에 저장
    def initFoodTable(self):
        print("food table 초기화")
        with open("FoodData.csv", 'r', encoding='utf-8-sig') as f:
            global food_dict_keys
            f.readline()
            for line in f.readlines():
                food_dict = {}
                i = 0
                for word in line.split(','):
                    food_dict[food_dict_keys[i]] = word.strip()
                    i += 1
                food_table.append(food_dict)

    # food_table을 수정하는 method
    # now_selected_options을 기반으로 option에 맞지 않는 음식은 food_table에서 삭제
    # now_selected_options를 비움
    def alterFoodTable(self, question_num):
        global food_table, food_dict_keys, now_selected_options, selected_options
        prev_num = len(food_table)
        print(f"ㅡ{food_dict_keys[question_num + 1]} 분류 시작ㅡ")

        # 분류 전 selected_options 한번 확인, 필요시 now_selected_options 갱신
        if len(selected_options) > question_num:
            for option in selected_options[question_num]:
                if option not in now_selected_options:
                    now_selected_options.append(option)
            selected_options[question_num] = now_selected_options
        elif len(selected_options) == question_num:
            selected_options.append(now_selected_options)

        print(f"선택된 옵션: {now_selected_options}")

        # 분류
        if question_num == 0:       # 가격
            FoodManagement.comparePrice(self)
        elif question_num == 1:     # 음식 계열
            FoodManagement.compareFoodType(self)
        elif question_num == 2:     # 주재료
            FoodManagement.compareMainIngredient(self)
        elif question_num == 3:     # 부재료
            FoodManagement.compareSubIngredient(self)
        elif question_num == 4:     # 매운 정도
            FoodManagement.compareSpicy(self)
        elif question_num == 5:     # 온도
            FoodManagement.compareTemperature(self)

        print(f"! {prev_num - len(food_table)}개 음식 삭제됨")
        print(f"남은 음식 개수: {len(food_table)}")

        # 현재 선택된 option 초기화
        now_selected_options = []

        print(f"ㅡ{food_dict_keys[question_num + 1]} 분류 완료ㅡ\n")

    # 가격 분류 method
    def comparePrice(self):
        global food_table, now_selected_options

        # option에 '~', '원' 삭제
        price_limit = now_selected_options[0].strip("~원")

        # "무제한!"이 선택됐는지 확인
        # 숫자가 있다면 선택되지 않은 것이므로 food_table에서 가격이 price_limit을 초과하는 음식 삭제
        if price_limit.isalnum():
            food_table = [food_dict for food_dict in food_table
                          if int(food_dict["가격"]) <= int(price_limit)]

    # 음식 계열 분류 method
    def compareFoodType(self):
        global food_table, now_selected_options

        food_table = [food_dict for food_dict in food_table
                      if food_dict["음식 계열"] in now_selected_options]

    # 주재료 분류 method
    def compareMainIngredient(self):
        global food_table, now_selected_options

        food_table = [food_dict for food_dict in food_table
                      if food_dict["주재료"] in now_selected_options]

    # 부재료 분류 method
    def compareSubIngredient(self):
        global food_table, now_selected_options

        food_table = [food_dict for food_dict in food_table
                      if food_dict["부재료"] in now_selected_options]

    # 매운 정도 분류 method
    def compareSpicy(self):
        global food_table, now_selected_options

        options = []
        for option in now_selected_options:
            if option == "맵게":
                options.append('s')
            elif option == "매콤하게":
                options.append('m')
            elif option == "안맵게":
                options.append('n')

        food_table = [food_dict for food_dict in food_table
                      if food_dict["매운 정도"] in options]

    # 온도 분류 method
    def compareTemperature(self):
        global food_table, now_selected_options

        options = []
        for option in now_selected_options:
            if option == "뜨끈하게":
                options.append('h')
            elif option == "시원하게":
                options.append('c')

        food_table = [food_dict for food_dict in food_table
                      if food_dict["온도"] in options]

    def selectRandomFood(self):
        global food_table
        random_index = random.randint(0, len(food_table) - 1)
        print(food_table)
        return food_table[random_index]["음식 이름"]
