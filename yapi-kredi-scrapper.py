import requests
from bs4 import BeautifulSoup
import time

request_mig = "https://www.yapikredi.com.tr/yatirimci-kosesi/doviz-bilgileri"

old_curr = {"us": 0.0, "eur": 0.0, "gbp": 0.0}

while True:
    res = requests.get(request_mig)
    html_content = BeautifulSoup(res.content, "lxml")
    tr_tag = html_content.find("tbody", {"id": "currencyResultContent"})
    curr_list = tr_tag.text.split()
    us_alis = float(curr_list[3].replace(",", "."))
    us_satis = float(curr_list[4].replace(",", "."))
    eu_alis = float(curr_list[13].replace(",", "."))
    eu_satis = float(curr_list[14].replace(",", "."))
    gbp_alis = float(curr_list[27].replace(",", "."))
    gbp_satis = float(curr_list[28].replace(",", "."))
    if old_curr['us'] != us_alis or old_curr['eur'] != eu_alis or old_curr['gbp'] != gbp_alis:
        old_curr['us'] = us_alis
        old_curr['eur'] = eu_alis
        old_curr['gbp'] = gbp_alis
        print("USD Amerikan Doları {} {} diff: {:.3f}".format(us_alis, us_satis, us_alis-us_satis))
        print("EUR Avrupa Para Birimi {} {} diff: {:.3f}".format(eu_alis, eu_satis, eu_alis-eu_satis))
        print("GBP İngiliz Sterlini {} {} diff: {:.3f}".format(gbp_alis, gbp_satis, gbp_alis-gbp_satis))
        print("------------------")
    time.sleep(2.5)
