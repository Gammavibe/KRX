import wrap

import pandas as pd
import pymysql as ms
import numpy as np
MKT_TP='ALL'

try:
    db=ms.connect(host='192.168.219.121',user='65279',db='test', passwd='blash@12')
    cs=db.cursor()
except Exception as e:
    print(e)

a=KRX.STKBULK()
h=['date','ISU_SRT_CD','ISU_ABBRV','MKT_NM','SECT_TP_NM','TDD_CLSPRC','FLUC_TP_CD','CMPPREVDD_PRC','FLUC_RT','TDD_OPNPRC','TDD_HGPRC','TDD_LWPRC','ACC_TRDVOL','ACC_TRDVAL','MKTCAP','LIST_SHRS','MKT_ID']
sql='INSERT INTO krx_stk_cgr VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
TYPES={'TDD_CLSPRC':np.float64,
       'CMPPREVDD_PRC':np.float64,
       'FLUC_RT':np.float64,
       'TDD_OPNPRC':np.float64,
       'TDD_HGPRC':np.float64,
       'TDD_LWPRC':np.float64,
       'ACC_TRDVOL':np.int64,
       'ACC_TRDVAL':np.int64,
       'MKTCAP':np.int64,
       'LIST_SHRS':np.int64}
for d in dt:
    try:
        df=pd.DataFrame(a.fetch(dt,MKT_TP))
        df=df.replace('[^-\w.]','',regex=True)
        df['date']=d
        a = df.columns[-1:].to_list() + df.columns[:-1].to_list()
        df=df[a]
        dft = list(df.itertuples(index=False, name=None))
        cs.executemany(sql,dft)
        db.commit()
    except Exception as e:
        print(dt)

#SQL명령어에서 %s 는 인자의 타입을 지정해주는게 아니다
#즉, int형식이라서 %d, float형식이라서 %f같은걸 쓰면안된다.
url='https://api.booking.naver.com/v3.0/bookings'
q={'bookingStatusCodes': 'RC03,RC08',
'lang': 'ko',
'bizItemId': '3012318',
'page': '0',
'size': '1',
'businessId': '223362',
'lang': 'ko'}