# 전체 학생 수 n
# 도난당한 학생 번호 배열 lost
# 여벌 체육복 학생 배열 reserve
# 수업을 들을 수 있는 학생의 최댓값

def solution(n, lost, reserve)
    answer = n
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
    # set을 사용해서 중복값 없애기
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
        
    # 만약에 lost의 전, 다음 원소가 reserve에 있다면
    for i in set_reserve
        if (i-1) in set_lost
            set_lost.remove(i - 1)
        elif (i+1) in set_lost
            set_lost.remove(i + 1)
            
    
    return answer-len(set_lost)