from frask import Flask, render_template
import pandas as pd
BodyTemp=pd.read_csv('static/BodyTemp_data.csv',index_col=0)

while True:
    try:
        Jcode= int(input('従業員コードは？'))
    except ValueError:
        print('[エラー]　半角数字じゃなかったので、もっかいお願いします！')
    else:
        if not len(str(Jcode)) ==7:
            print('[エラー]　7ケタじゃなかったので、もっかいお願いします！')
        else:
            break
while True:
    try:
        TodayTemp= int(input('今朝の体温は？'))
    except ValueError:
        print('[エラー]　半角数字じゃなかったので、もっかいお願いします！')
    else:
        if TodayTemp <= 34.0 or TodayTemp >= 40.0:
            print('[エラー]　人間の体温じゃなかったので、もっかいお願いします！')
        else:
            break

import datetime
Datetime= datetime.datetime.utcnow() + datetime.timedelta(hours=9)
Date=Datetime.date()

BodyTemp.loc[str(Date),str(Jcode)]=round(float(TodayTemp),1)
BodyTemp.to_csv('static/BodyTemp_data.csv')
BodyTemp
