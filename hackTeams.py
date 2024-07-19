def countTeams(t1,t2,p):
    if(p<t1 and p<t2):
        return -1
    if(p-t1 == 0 or p-t2 == 0):
        return 1
    else:
        uset1 = countTeams(t1,t2,p-t1)
        uset2 = countTeams(t1,t2,p-t2)
        if(uset1 > 0 and uset2 < 0):
            return 1+uset1
        if(uset1 < 0 and uset2 > 0):
            return 1+uset2
        if(uset1<0 and uset2<0):
            return uset2
        else:
            return min(1+uset1, 1+uset2)
        

print(countTeams(2,4,5))