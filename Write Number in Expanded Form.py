def expanded_form(num):
    result = []
    res = list(map(int, str(num)))
    for i in range(0, len(res)):
        if res[i] !=0:
            result.append(res[i]*10**(len(res)-i-1))
    return (" + ".join(map(str,result)))
