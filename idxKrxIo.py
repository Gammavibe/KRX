from webIo import Get, Post
from idxKrxOtp import *

class Idx_Krx_Io(Post):
    def __init__(self):
        super().__init__()
        self.headers.update({'Accept-Encoding': 'gzip, deflate, br', 'path': '/contents/IDX/99/IDX99000001.jspx'})
        self.date=datetime.datetime.now().strftime('%Y%m%d')
        self.mkt_tp_cd = 'ALL'
#header에서 path가 중요함
    def read(self, **params):
        params.update(pagePath=self.pagePath, lang=self.lang, code=self.otp)
        result = super().read(**params)
        return result.json()

    @property
    def url(self):
        return 'https://index.krx.co.kr/contents/IDX/99/IDX99000001.jspx'

    @property
    def lang(self):
        return 'ko'

    @property
    def pagePath(self):
        raise NotImplementedError

    @property
    def otp(self):
        raise NotImplementedError


