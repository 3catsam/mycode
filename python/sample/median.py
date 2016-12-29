def median(ss):
    ss=sorted(ss)
    
    if len(ss)%2==1:
        return ss[int(len(ss)/2.0)]
    else:
        return (ss[int(len(ss)/2.0)]+ss[int(len(ss)/2.0)-1])/2.0
    

median([5, 2, 3, 1, 4])