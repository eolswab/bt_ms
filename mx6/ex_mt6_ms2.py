# # # 📌Q2.  여러분은 6명의 멤버를 거느리는 영업팀의 영업관리자 입니다. 각 멤버별로 올해 실적을 보고 잘한 멤버는 보너스를 주고 못한 멤버는 면담을 하려고 합니다. 파이썬을 이용하여 함수를 만들어 보너스 대상자와 면담 대상자를 골라주세요.
# # #
# # # 😲조건 1 - 예비 보너스 대상자는 평균 실적 1등 2등 입니다.
# # # 😲조건 2 - 예비 면담 대상자는 평균 실적 5등 6등 입니다.
# # # 😲조건 3 - 보너스 대상자의 평균 실적이 5보다 크지 않으면 보너스 대상자에서 제외 됩니다.
# # # 😲조건 4 - 면담 대상자의 평균 실적이 3보다 크면 면담 대상자에서 제외 됩니다.
# #
# #
# # # 이름, 실적
# # member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
# # member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
# #            [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
# #            [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]
#
# sales_management(member_names, member_records)
# 보너스 대상자 병돌이
# 보너스 대상자 을순이
#
# 면담 대상자 갑순이


def sales_management(names, records):
    record_dict = dict()  # 멤버의 실적을 기록할 dict 생성
    # 실적 기록
    for i in range(len(names)):
        record_dict[names[i]] = records[i]

    # 실적을 평균으로 바꿔서 저장
    for (k, v) in record_dict.items():
        total = 0
        for i in v:
            total = total + i
        mean = total / len(v)
        record_dict[k] = mean
    # 평균 실적이 높은 순서대로 저장
    ranking = [(v, k) for k, v in record_dict.items()]
    ranking = sorted(ranking, reverse=True)

    # 예비 보너스, 면담 대상자 저장
    bonus_names = (ranking[0][1], ranking[1][1])
    counsel_name = (ranking[4][1], ranking[5][1])

    # 5보다 작으면 보너스 대상자 제외
    for bn in bonus_names:
        if record_dict[bn] < 5:
            continue
        print(f"보너스 대상자 {bn}")
    print()

    # 3보다 높으면 면담 대상자 제외
    for cn in counsel_name:
        if record_dict[cn] > 3:
            continue
        print(f"면담 대상자 {cn} ")