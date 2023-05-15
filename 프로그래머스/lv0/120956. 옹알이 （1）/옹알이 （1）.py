def solution(babbling):
    count=0
    canspeak=["aya","ye","woo","ma"]
    for s in babbling:
        temp=s
        for can in canspeak:
            if can in temp:
                temp=temp.replace(can,' ')
                print(temp)
        temp=temp.strip()
        if len(temp)==0:
            count+=1
    return count