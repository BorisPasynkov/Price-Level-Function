def ResistLevel():
    
    global HPvec
    global IndexVec
    global highc
    global current_high
    global ResElVec
    
    
    levborder=0.001
    timerange=23   
    fourmin=4 

    
    if len(highc)>=fourmin:
        if highc[-1]>highc[-2] and highc[-1]>highc[-3] and highc[-1]>highc[-4]:
            current_high=highc[-1]
        else: 
            if len(HPvec)==0:
                if current_high!=0:
                    HPvec.append(current_high)
                    currdat=highc[0:]
                    Index=[index for index, element in enumerate(currdat) if element == current_high]
                    IndexVec.append(Index[-1])
            
            elif len(HPvec)>0:
                 if current_high!=HPvec[-1]:
                     HPvec.append(current_high)
                     currdat=highc[0:]
                     Index=[index for index, element in enumerate(currdat) if element == current_high]
                     IndexVec.append(Index[-1])
                     if len(HPvec)>1:
                        for k in range(0,len(HPvec)-1):
                            if HPvec[-1]>(HPvec[k]+HPvec[k]*levborder):
                                HPvec[HPvec.index(HPvec[k])] = 0
                                IndexVec[IndexVec.index(IndexVec[k])] = 0
                            elif HPvec[-1]>=(HPvec[k]-HPvec[k]*levborder) and HPvec[-1]<=(HPvec[k]+HPvec[k]*levborder):
                                if len(ResElVec)==0:
                                    if (IndexVec[-1]-IndexVec[k])>=timerange:
                                        ResEL=[(HPvec[k]-HPvec[k]*levborder),(HPvec[k]+HPvec[k]*levborder),HPvec[-1]]
                                        ResElVec.append(list(ResEL))
                                elif len(ResElVec)>0:
                                    for l in range(0,len(ResElVec)):
                                        if HPvec[-1]>=ResElVec[l][0] and HPvec[-1]<=ResElVec[l][1]:
                                            if HPvec[-1]!=ResElVec[l][2]:
                                                HPvec[HPvec.index(HPvec[-1])] = 0
                                                IndexVec[IndexVec.index(IndexVec[-1])] = 0
                                    if HPvec[-1]!=ResElVec[-1][2] and HPvec[-1]>=(HPvec[k]-HPvec[k]*levborder) and HPvec[-1]<=(HPvec[k]+HPvec[k]*levborder):
                                        if (IndexVec[-1]-IndexVec[k])>=timerange:           
                                            ResEL=[(HPvec[k]-HPvec[k]*levborder),(HPvec[k]+HPvec[k]*levborder),HPvec[-1]]
                                            ResElVec.append(list(ResEL))        
                        
                        HPvec=list(filter(lambda x: x!= 0, HPvec))                        
                        IndexVec=list(filter(lambda x: x!= 0, IndexVec))                        
                                                
                                                
                                                
                                                
    return HPvec, IndexVec, current_high, ResElVec
