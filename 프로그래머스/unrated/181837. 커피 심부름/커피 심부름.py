def solution(order):
    ame=4500
    latte=5000
    total=0
    
    for i in order:
        if 'americano' in i or 'anything' in i:
            total+=ame
        else:
            total+=latte
    return total
    