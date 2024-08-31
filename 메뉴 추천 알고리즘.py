import pandas as pd #외부데이터 읽어오는 명령어

menu_df = pd.read_csv('menu.csv')  #메뉴 데이터를 담은 csv 파일을 읽어옴

def recommend_menu():   #함수 정의
    word=input("원하는 메뉴 종류를 선택하세요/한식과 일식 중식 중 한 가지로 선택") 

    filtered_df = menu_df[menu_df['종류']==word]  #사용자의 선택에 따라 필터링하는 명령어

    if word=='한식':
        answer1=input("국물이 있는 음식이 먹고싶나요?:")
        filtered_df = filtered_df[filtered_df['국물']==answer1]  
        if not filtered_df.empty:   #이 명령어는 필터링된 데이터프레임에 남은 데이터가 있는지 여부를 알려줌
            answer2=input('매운 건 어떠세요? 네/ 아니요로 대답:')
            filtered_df = filtered_df[filtered_df['매운맛']==answer2]

    elif word == '양식' or word == '일식':
        answer1 = input("고기 종류는 어떠세요?/네 아니요로 대답:")
        if word == '양식':
            filtered_df=filtered_df[filtered_df['국물']=='아니요']  #양식에는 국물있는 음식이 없음.
        if not filtered_df.empty:
            filtered_df=filtered_df[filtered_df['매운맛']=='아니요']  #양식과 일식에는 매운 음식이 없음.

    if not filtered_df.empty:
        recommended_menus=filtered_df['이름'].tolist()
        print(''.join(recommended_menus)'를 추천해드릴게요!')
    else:
        print("추천해드릴 메뉴가 없습니다.")

recommend_menu()  #함수 호출 (파이썬에서는 함수 정의에서가 아닌 호출에서 실행됨)

# '='는 변수에 값을 할당하는 연산자
# '=='는 두 값이 같은지를 비교하는 연산자. ex) if 조건문