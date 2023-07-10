import pandas as pd
import trendln
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
from fmp_python.fmp import FMP

# signal 

def signal_de_resistance_line(values, condition ):
    return resistance(values, condition )-values

def signal_de_support_line(values, condition ):
    return support(values, condition )-values



def resistance(values, condition ) :
    
    # values = le  data 
    # condition = valeur de  r^2 minimal de la droite 
    
    h = pd.Series(values)
    
   # maximaIdxs  = les maximums  local
    mins, maxs = trendln.calc_support_resistance(h, accuracy= 2)
    (minimaIdxs, pmin, mintrend, minwindows), (maximaIdxs, pmax, maxtrend, maxwindows) = mins, maxs

    
    n0 = 0
    y_out = []  
    
    list= np.arange(0,maximaIdxs[n0],1)
    y_out.append(1+1*list)  
    # valeur du debut  qui sont non representative 
    
    
    for i in range(2,len(maximaIdxs)+1): 

        n1 =i

        #recherche de droite 
        x= maximaIdxs[n0:n1]   
        y= h[maximaIdxs[n0:n1]]
        
        
        z = np.polyfit(x, y, 1)
        c = np.poly1d(z)
        
        r2 = r2_score(y,c(x))
       
        #obtention de la droite
        if r2 < condition/100:
            list= np.arange(maximaIdxs[n0],maximaIdxs[pt-1],1)
            y_out.append(droite[1]+droite[0]*list)
            n0=pt-1
              
        droite = z
        pt = n1
    #projection de la derniere droite  jusqu'a la dernier
    list= np.arange(maximaIdxs[n0],len(h),1)
    y_out.append(droite[1]+droite[0]*list)   
   
    return pd.Series(np.concatenate(y_out))

def support(values, condition ) :
    # values = le  data 
    # condition = valeur de  r^2 minimal de la droite 
    h = pd.Series(values)
    
   # maximaIdxs  = les minimums  local
    mins, maxs = trendln.calc_support_resistance(h, accuracy= 2)
    (minimaIdxs, pmin, mintrend, minwindows), (maximaIdxs, pmax, maxtrend, maxwindows) = mins, maxs

    
    n0 = 0
    y_out = []  
    
    list= np.arange(0,minimaIdxs[n0],1)
    y_out.append(1+1*list)  
    
    for i in range(2,len(minimaIdxs)+1): 
        #recherche de droite 
        n1 =i

    
        x= minimaIdxs[n0:n1]   
        y= h[minimaIdxs[n0:n1]]
        
        
        z = np.polyfit(x, y, 1)
        c = np.poly1d(z)
        
        r2 = r2_score(y,c(x))
        
        #obtention de la droite
        if r2 < condition/100:
            list= np.arange(minimaIdxs[n0],minimaIdxs[pt-1],1)
            y_out.append(droite[1]+droite[0]*list)
            n0=pt-1
              
        droite = z
        pt = n1
    #projection de la derniere droite  jusqu'a la dernier
    list= np.arange(minimaIdxs[n0],len(h),1)
    y_out.append(droite[1]+droite[0]*list)   
   
    return pd.Series(np.concatenate(y_out))
