# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:21:58 2021

@author: sharp
"""

def SupportLevel():
    
    global LPvec
    global IndexVecL
    global lowc
    global current_low
    global SupElVec
    
    levborder=0.001
    timerange=23   
    fourmin=4 

    
    if len(lowc)>=fourmin:
        if lowc[-1]<lowc[-2] and lowc[-1]<lowc[-3] and lowc[-1]<lowc[-4]:
            current_low=lowc[-1]
        else: 
            if len(LPvec)==0:
                if current_low!=0:
                    LPvec.append(current_low)
                    currdat=lowc[0:]
                    Index=[index for index, element in enumerate(currdat) if element == current_low]
                    IndexVecL.append(Index[-1])
            
            elif len(LPvec)>0:
                 if current_low!=LPvec[-1]:
                     LPvec.append(current_low)
                     currdat=lowc[0:]
                     Index=[index for index, element in enumerate(currdat) if element == current_low]
                     IndexVecL.append(Index[-1])
                     if len(LPvec)>1:
                        for m in range(0,len(LPvec)-1):
                            if LPvec[-1]<(LPvec[m]-LPvec[m]*levborder):
                                LPvec[LPvec.index(LPvec[m])] = 0
                                IndexVecL[IndexVecL.index(IndexVecL[m])] = 0
                            elif LPvec[-1]>=(LPvec[m]-LPvec[m]*levborder) and LPvec[-1]<=(LPvec[m]+LPvec[m]*levborder):
                                if len(SupElVec)==0:
                                    if (IndexVecL[-1]-IndexVecL[m])>=timerange:
                                        SupEL=[(LPvec[m]-LPvec[m]*levborder),(LPvec[m]+LPvec[m]*levborder),LPvec[-1]]
                                        SupElVec.append(list(SupEL))
                                elif len(SupElVec)>0:
                                    for n in range(0,len(SupElVec)):
                                        if LPvec[-1]>=SupElVec[n][0] and LPvec[-1]<=SupElVec[n][1]:
                                            if LPvec[-1]!=SupElVec[n][2]:
                                                LPvec[LPvec.index(LPvec[-1])] = 0
                                                IndexVecL[IndexVecL.index(IndexVecL[-1])] = 0
                                    if LPvec[-1]!=SupElVec[-1][2] and LPvec[-1]>=(LPvec[m]-LPvec[m]*levborder) and LPvec[-1]<=(LPvec[m]+LPvec[m]*levborder):
                                        if (IndexVecL[-1]-IndexVecL[m])>=timerange:           
                                            SupEL=[(LPvec[m]-LPvec[m]*levborder),(LPvec[m]+LPvec[m]*levborder),LPvec[-1]]
                                            SupElVec.append(list(SupEL))        
                        
                        LPvec=list(filter(lambda x: x!= 0, LPvec))                        
                        IndexVecL=list(filter(lambda x: x!= 0, IndexVecL))                        
                                                
                                                
                                                
                                                
    return LPvec, IndexVecL, current_low, SupElVec