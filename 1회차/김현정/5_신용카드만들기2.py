import sys

sys.stdin = open("_신용카드만들기2.txt")

# 2022.07.29 모의고사 05 신용카드만들기2
# 카드번호는 3, 4, 5, 6, 9로 시작
# 카드번호는 "-"이 들어갈 수 있으며 "-"을 제외한 숫자 개수 16개
# 카드번호가 주어졌을 때 해당 번호로 신용카드 만들 수 있는지 판별
# 카드번호 만들 수 있으면 1, 만들 수 없으면 0 출력

# 테스트 케이스 입력받음
T = int(input())

# 카드 시작번호는 3, 4, 5, 6, 9여야 하므로 이를 검증하기 위한 리스트 정의
card_num1 = ["3", "4", "5", "6", "9"]

# 카드 유효한지 아닌지 결과(0 또는 1)를 담는 리스트 정의
card_list = []

# 테스트 케이스 횟수(T)만큼 for문 실행
for i in range(1, T+1):

    # 카드번호를 입력받음, "-"이 포함되어 있는 카드번호도 존재하여 string 형태로 맞춰줌
    card_num = str(input())

    # 만약 카드 첫째자리가 유효한 카드번호에 해당한다면
    if card_num[0] in card_num1:
        # "-"이 없는 숫자로만 이루어진 신용카드 번호라면
        if "-" not in card_num:
            # 신용카드는 총 16자리라면 유효(1)
            if len(card_num) == 16:
                card_list.append(1)
            # 신용카드 16자리가 아니라면 무효(0)
            else:
                card_list.append(0)
        # "-"이 있는 카드번호가 주어졌을 경우
        else:
            # "-"은 총 3개 들어가므로, 숫자16자리까지 총 19자리여야함.
            # "-" 포함하여 신용카드 19자리라면 유효(1)
            if len(card_num) == 19:
                card_list.append(1)
            # "-" 포함하여 신용카드 19자리가 아니라면 유효(1)
            else:
                card_list.append(0)
    # 카드 첫째자리가 유효한 카드번호에 해당하지 않는다면 무효(0)
    else:
        card_list.append(0)

# 결과값 출력
for h in range(1, len(card_list)+1):
    print(f"#{h}", card_list[h-1])