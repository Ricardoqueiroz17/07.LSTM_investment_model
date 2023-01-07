# Stop loss function
def stopLossFutRet(df, col, period=21, stopLimit=-0.01, highLimit=0.04):
    a = df[col].tolist()  # Turn the column into a list
    lena = len(a)
    list_futret = [0] * lena
    list_futpos = [0] * lena

    for i in range(lena):
        if lena - i - 1 < period:
            break
        for futi in range(i + 1, i + period + 1):
            retWind = a[futi] / a[i] - 1
            if retWind <= stopLimit: #If return reached the stop loss threshold
                list_futret[i] = retWind
                list_futpos[i] = futi - i
                break
            elif retWind >= highLimit: #If reached the high limit threshold
                list_futret[i] = retWind
                list_futpos[i] = futi - i
                break
        #In case that it didnt reach any of the limits, thus we carry the asset untill the end of the period
        list_futret[i] = retWind
        list_futpos[i] = futi - i

    df['Fut_return_period'] = list_futret
    df['PosStop'] = list_futpos


