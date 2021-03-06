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
    res = requests.get(request_mig)
    update = False
    for key, curr_item in curr_dict.items():
        html_content = BeautifulSoup(res.content, "lxml")
        tr_tag = html_content.find("tr", {"id": curr_item})
        split_list = tr_tag.text.split()
        curr_alis = float(split_list[-1].replace(',', '.'))
        curr_satis = float(split_list[-2].replace(',', '.'))
        if old_curr[key] != curr_alis:
            old_curr[key] = curr_alis
            update = True
        if update:
            print("{} diff: {:.3f}".format(" ".join(tr_tag.text.split()), curr_satis-curr_alis))
    if update:
        print("-------------------")

    time.sleep(2.5)