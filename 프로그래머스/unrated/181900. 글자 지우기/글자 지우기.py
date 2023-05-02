def solution(my_string, indices):
    sorted_indice=sorted(indices,reverse=True)
    
    data=[]
    for i in range(len(my_string)):
        data.append(my_string[i])
    
    for i in sorted_indice:
        del data[i]
    
    return "".join(data)