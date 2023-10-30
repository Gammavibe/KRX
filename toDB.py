from wrap import *
import pandas as pd
import pymysql as ms
from sqlalchemy import create_engine
from urllib.parse import quote as q
#
a = Krx_Gics_Cgr()

GICSLIST = {'10': '에너지', '15': '소재', '20': '산업재', '25': '자유소비재',
            '30': '필수소비재', '35': '건강관리', '40': '금융', '45': '정보기술',
            '50': '커뮤니케이션서비스', '55': '유틸리티', '60': '부동산'}
MKTLIST = ['STK','KSQ']
TYPELIST = {'prsnt_prc': 'float', 'cmpprevdd_prc': 'float', 'fluc_rt': 'float', 'askord': 'float', 'bidord': 'float','opnprc': 'float', 'hgprc': 'float', 'lwprc': 'float',
            'trdvol': 'int64', 'trdval': 'int64','listshr_cnt':'int64', 'list_mktcap': 'int64'}
df=pd.DataFrame()
dt='20230811'

for gics in GICSLIST:
    for mkt in MKTLIST:
        df2 = pd.DataFrame(a.fetch(mkt, gics, dt))
        df2['mkt_td_cd'] = mkt
        df2['gics_ind_grp_cd'] = gics
        df2['gics_ind_grp_nm'] = GICSLIST[gics]
        df2['dt'] = a.date
        df = pd.concat([df, df2])
a = df.columns[-1:].to_list() + df.columns[:-1].to_list()
df = df[a]

df=df.replace('[^-\w.]', '', regex=True)
for k in TYPELIST:
    df[k]=df[k].astype(TYPELIST[k])

try:
    db=ms.connect(host='192.168.219.121',user='65279',db='test', passwd='blash@12')
    cs=db.cursor()
except Exception as e:
    print(e)

#sql='select * from KRX_GICS_CGR'
#sql='INSERT INTO krxstk '
sql=sql='INSERT INTO krx_stk_cgr VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
sql='SHOW DATABASES'
result=pd.read_sql(sql,db)

engine=create_engine('mysql+pymysql://65279:%s@192.168.219.121/test' % q('blash@12',), encoding='euc-kr')
con=engine.connect()
df.to_sql(name='krx_gics_cgr', con=engine, if_exists='append', index=False)