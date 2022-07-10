
from tabnanny import check
from unittest import result
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore, Back, Style
import csv
from csv import DictWriter

from pkg_resources import resource_listdir

reaultsDict = {}
resultsarr =[]
field_names = ['checkout value','total gain']
max_checkout=0
max_total_gain = -100000000000

def main():
        
    #import csv and convert it to list
    df = pd.read_csv (r'outputs.csv')
    df = df.to_numpy()


    #create array from 0 to len(df) with step 1
    y = np.arange(0,len(df),1)


    #plt.figure(figsize =(200,200))


    #plt.plot(df , y , linewidth=2.0)
    

    plt.figure(figsize=(9, 3))




    #calulate stats


    #how much money spent on a bet
  

    #the minimum value and the value i am going to checkout
    #max_total_gain = 0
    max_total_checkout=0
    max_total_gain = -100000000000

    best_best_value =0
    bet_val = 1.02

    for x in np.arange(0.1,10.1,5):
        #calc_total_gain(minvalue,2.352,5)
        for i in np.arange(1.01 , 3 , 0.01):
            max_temp,max_chk_temp,best_bet_value_temp = calc_total_gain(i,x,max_total_gain)
            if ( max_temp > max_total_gain):
                max_total_gain = max_temp
                max_total_checkout = max_chk_temp
                best_bet_value = best_bet_value_temp
    
    print("FINAL RESULTS:",  max_total_gain, "at this checkout: " , max_total_checkout,"and this bet value: ",best_bet_value)
    #print(max_total_gain)

def calc_total_gain(bet_val,bet_value,max_total_gain):
    minvalue = 1.0

    df = pd.read_csv (r'outputs.csv')
    df = df.to_numpy()

    #max_total_gain = 0
    max_checkout = 0
    best_bet_value = 0


    loss_count = 0 
    win_count = 0 
    t2count = 0
    t3count = 0 
    topcount = 0

    total_gain = 0
    counter = 0
    round_earnings = 0
    prev_total_gain = 0


    int_arr = []
    total_arr = []
    round_gain = []

    for x in range(len(df)):
        counter +=1
        int  = float(df[x])
        #print("int: " , int )
        int_arr.append(int)

        total_gain -=bet_value
        #loss_case
        if int >= minvalue  and int <=bet_val:
            total_gain = total_gain - bet_value
            loss_count+=1
        else:
            total_gain = (bet_value*bet_val) + total_gain   
            win_count+=1
        

        #print (" TOTAL GAIN: ", total_gain)
        total_arr.append(total_gain)

        round_earnings = total_gain- prev_total_gain
        round_gain.append(round_earnings)

        # if round_earnings>0:
        #     print(Fore.GREEN + str(round_earnings))
        # else:
        #     print(Fore.RED + str(round_earnings))
        # print(Style.RESET_ALL)
        # print("round_earnings = " ,round_earnings)
        prev_total_gain = total_gain   
        
       
        
        

    #print("win_count: ",win_count," t2count: ",t2count," top count: ",topcount,"losscount: ",loss_count)
    print("bet_value: ",bet_value,"checkout_value: " , bet_val," total gain: ", total_gain)
    reaultsDict.update({bet_val:total_gain})
    
    if(total_gain > max_total_gain):
            max_total_gain = total_gain
            max_checkout = bet_val 
            best_bet_value = bet_value

    return max_total_gain,max_checkout,best_bet_value






if __name__ == "__main__":
    main()




