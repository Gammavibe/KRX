from webIo import Get
import datetime

class KrxOTP(Get):

    def __init__(self, bld=None, name=None):
        super().__init__()
        self.__bld=bld
        self.__name=name

    def read(self, **params):
        params.update(bld=self.bld, name=self.name, _=self.timeNumeric)
        resp = super().read(**params)
        return resp.text

    @property
    def url(self):
        return 'https://index.krx.co.kr/contents/COM/GenerateOTP.jspx'

    @property
    def timeNumeric(self):
        return int(datetime.datetime.now().timestamp() * 1000)

    @property
    def bld(self):
        return self.__bld

    @property
    def name(self, ):
        return self.__name

    @property
    def otp(self):
        result = self.read()
        return result
