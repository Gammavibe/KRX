from webIo import Post


class DataKrxIo(Post):
    def read(self, **params):
        params.update(bld=self.bld)
        resp = super().read(**params)
        return resp.json()

    @property
    def url(self):
        return 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'

    @property
    def bld(self):
        raise NotImplementedError

    @bld.setter
    def bld(self, val):
        pass


class ETFPDF(DataKrxIo):
    @property
    def bld(self):
        return 'dbms/MDC/STAT/standard/MDCSTAT05001'

    def fetch(self, date, isin):
        result = self.read(trdDd=date, isuCd=isin)
        return result['output']


class ETFLIST(DataKrxIo):
    @property
    def bld(self):
        return 'dbms/MDC/STAT/standard/MDCSTAT04601'

    def fetch(self):
        result = self.read()
        return result['output']


class STKBULK(DataKrxIo):
    @property
    def bld(self):
        return 'dbms/MDC/STAT/standard/MDCSTAT01501'

    # 전체:ALL, 코스피:STK, 코스닥:KSQ, 코넥스:KNX
    def fetch(self, date, mktId):
        result = self.read(trdDd=date, mktId=mktId)
        return result['OutBlock_1']


class IDX(DataKrxIo):
    @property
    def bld(self):
        return 'dbms/MDC/STAT/standard/MDCSTAT00301'

    # K200: 1
    def fetch(self, strDd, endDd, indIdx):
        result = self.read(strDd=strDd, endDd=endDd, indIdx=indIdx)
        return result['output']
