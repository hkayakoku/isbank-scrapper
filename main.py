import requests
from bs4 import BeautifulSoup
import time

request_mig = "https://www.isbank.com.tr/doviz-kurlari"

us = "ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73_ctl00_FxRatesRepeater_ctl00_fxItem"
eur = "ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73_ctl00_FxRatesRepeater_ctl01_fxItem"
gbp = "ctl00_ctl18_g_1e38731d_affa_44fc_85c6_ae10fda79f73_ctl00_FxRatesRepeater_ctl02_fxItem"

curr_dict = {'us': us, 'eur': eur, 'gbp': gbp}
old_curr = {"us": 0.0, "eur": 0.0, "gbp": 0.0}

while True:
    for key, curr_item in curr_dict.items():
        res = requests.get(request_mig)
        html_content = BeautifulSoup(res.content, "lxml")
        tr_tag = html_content.find("tr", {"id": curr_item})
        split_list = tr_tag.text.split()
        curr_alis = float(split_list[-1].replace(',', '.'))
        update = False
        if old_curr[key] != curr_alis:
            old_curr[key] = curr_alis
            update = True
        if update:
            print(" ".join(tr_tag.text.split()))

    time.sleep(2.5)
    print("----------------------")