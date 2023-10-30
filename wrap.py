from idxKrxIo import *

#index.krx.com에서 GCIS별 구성종목
class Krx_Gics_Cgr(Idx_Krx_Io):
    def __init__(self):
        super().__init__()
        self.mOTP = KrxOTP('IDX/03/0303/03030204/mkd03030204_03', 'form')
        # 전체:ALL, 코스피:STK, 코스닥:KSQ
        # 에너지:10, 소재:15, 산업재:20, 자유소비재:25, 필수소비재:30, 건강관리:35, 금융:40, 정보기술:45, 커뮤니케이션서비스:50, 유틸리티:55, 부동산:60

    def fetch(self, mkt_tp_cd=None, gics_cd=None, date=None):
        if mkt_tp_cd is None: mkt_tp_cd = self.mkt_tp_cd
        if date is None: date = self.date
        resp = self.read(mkt_tp_cd=mkt_tp_cd, gics_ind_grp_cd=gics_cd, date=date)
        return resp['block1']

    @property
    def otp(self):
        return self.mOTP.otp

    @property
    def pagePath(self):
        return '/contents/MKD/03/0303/03030204/MKD03030204.jsp'


#index.krx.com에서 GCIS별 구분 코드
class Krx_Gics_Dit(Idx_Krx_Io):
    def __init__(self):
        super().__init__()
        self.mOTP = KrxOTP('MKD/03/0303/03030204/mkd03030204_01', 'selectbox')

    def fetch(self, mkt_tp_cd=None, date=None):
        if mkt_tp_cd is None: mkt_tp_cd = self.mkt_tp_cd
        if date is None: date = self.date
        resp = self.read(mkt_tp_cd=mkt_tp_cd, date=date)
        return resp['block1']

    @property
    def otp(self):
        return self.mOTP.otp

    @property
    def pagePath(self):
        return '/contents/MKD/03/0303/03030204/MKD03030204.jsp'

class Krx_Idx_Cgr(Idx_Krx_Io):
    def __init__(self):
        super().__init__()
        self.mOTP = KrxOTP('MKD/03/0304/03040101/mkd03040101T3_01', 'form')

    def fetch(self, ind_tp_cd=None, idx_ind_cd=None, date=None):
        # ind_tp_cd = KOSPI:1, KOSDAQ:2
        # idx_ind_cd = K200:028, KOSDAQ150:203
        if ind_tp_cd is None: ind_tp_cd='1'
        if idx_ind_cd is None: idx_ind_cd = '028'
        if date is None: date = self.date
        resp = self.read(ind_tp_cd=ind_tp_cd, idx_ind_cd=idx_ind_cd, schdate=date)
        return resp['output']

    @property
    def otp(self):
        return self.mOTP.otp

    @property
    def pagePath(self):
        return '/contents/MKD/03/0304/03040101/MKD03040101T3.jsp'