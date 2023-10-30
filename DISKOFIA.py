import requests
import xml.etree.ElementTree as et
import pandas as pd
# 펀드 기준가 뽑기
class KOFIA:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0",'Content-Type': 'text/xml'}

    def read(self, params):
        resp = requests.post(self.url, headers=self.headers, data=params)
        return resp
    @property
    def url(self):
        return "https://dis.kofia.or.kr/proframeWeb/XMLSERVICES/"

    def set_body(self, start, end, fund_Cd):
        self.msg=et.Element("message")
        self.proframeHeader=et.SubElement(self.msg,"proframeHeader")
        self.pfmAppName=et.SubElement(self.proframeHeader,"pfmAppName")
        self.pfmAppName.text="FS-DIS2"
        self.pfmSvcName=et.SubElement(self.proframeHeader,"pfmSvcName")
        self.pfmSvcName.text="DISFundStdPrcStutSO"
        self.pfmFnName=et.SubElement(self.proframeHeader,"pfmFnName")
        self.pfmFnName.text="select"
        self.systemHeader=et.SubElement(self.msg,"systemHeader")
        self.systemHeader.text=""
        self.DISCondFuncDTO=et.SubElement(self.msg,"DISCondFuncDTO")
        self.tmpV30=et.SubElement(self.DISCondFuncDTO,"tmpV30")
        self.tmpV30.text=start
        self.tmpV31=et.SubElement(self.DISCondFuncDTO,"tmpV31")
        self.tmpV31.text=end
        self.tmpV10=et.SubElement(self.DISCondFuncDTO,"tmpV10")
        self.tmpV10.text="0"
        self.tmpV12=et.SubElement(self.DISCondFuncDTO,"tmpV12")
        self.tmpV12.text=fund_Cd
        return et.tostring(self.msg, encoding="utf8", method="xml")

    def fetch(self,str_dt,end_dt,fund_cd):
        pass


dt_start="20150102"
dt_end="20220220"
fund_list=["KR5105AO2723","K55105BA6990"]

f=KOFIA()
root=et.fromstringlist()
data=root.findall(".//selectMeta")
dt=root.findall(".//tmpV1")
prc=root.findall(".//tmpV2")
rows=[]
for fund_cd in fund_list:
    body = f.set_body(dt_start, dt_end, fund_cd)
    resp = f.read(body.decode())
    root = et.fromstring(resp.content)
    data = root.findall(".//selectMeta")
    for i in data:
        i_dt = i.find("tmpV1").text
        i_pr = i.find("tmpV2").text
        i_cd = i.find("tmpV12").text
        rows.append({"date":i_dt,"fund_cd":i_cd,"prc":i_pr})

df=pd.DataFrame(rows)
df.astype({"date":"string"})
a=pd.pivot_table(df,values="prc",columns="fund_cd",index="date",aggfunc='sum')