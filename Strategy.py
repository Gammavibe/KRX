import pandas as pd

from Wrap import *

def getSelfTradeDetails(arrCorpCodes, bgn_de, end_de):
    df=pd.DataFrame()
    cntRows=len(arrCorpCodes)
    for i in range(0,cntRows):
        if arrCorpCodes.loc[i,'tp_dit']=='S':
            df=pd.concat([df,getSelfTradeDetail(arrCorpCodes.loc[i,'corp_code'], bgn_de, end_de)])
        elif arrCorpCodes.loc[i,'tp_dit']=='T':
            df=pd.concat([df,getSelfTradeCtrDetail(arrCorpCodes.loc[i,'corp_code'], bgn_de, end_de)])

    #df=df.sort_values(by=['aq_dd'])
    df.reset_index(drop=True, inplace=True)

    return df


def getSelfTradeDecisionList(bgn_de, end_de):
    dartList=pd.DataFrame()
    #자기주식취득결정
    tempList=get_dart_list(bgn_de, end_de, pblntf_ty='B', filter_kwg='자기주식취득결정')
    tempList['tp_dit']='S'
    dartList=pd.concat([dartList,tempList])
    #자기주식취득신탁계약체결결정
    tempList=get_dart_list(bgn_de, end_de, pblntf_ty='B', filter_kwg='자기주식취득신탁계약체결결정')
    tempList['tp_dit']='T'
    dartList=pd.concat([dartList,tempList])

    #코스피, 코스닥 종목만 추리기
    bInKSEKDQ=dartList['corp_cls'].isin(['Y','K'])
    corpList=dartList[bInKSEKDQ]

    #어차피 getSelfTradeDetail 함수는 해당 회사의 특정기간 데이터를 모두 가져옴. 따라서 기업코드 1개만 있으면 됨
    corpList=corpList.drop_duplicates(subset=['corp_code','tp_dit'])
    corpList.reset_index(drop=True, inplace=True)
    return corpList

