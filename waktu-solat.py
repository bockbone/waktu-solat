import urllib.request
import json

zoneCode = [
    "JHR01",
    "JHR02",
    "JHR03",
    "JHR04",
    "KDH01",
    "KDH02",
    "KDH03",
    "KDH04",
    "KDH05",
    "KDH06",
    "KDH07",
    "KTN01",
    "KTN03",
    "MLK01",
    "NGS01",
    "NGS02",
    "PHG01",
    "PHG02",
    "PHG03",
    "PHG04",
    "PHG05",
    "PHG06",
    "PLS01",
    "PNG01",
    "PRK01",
    "PRK02",
    "PRK03",
    "PRK04",
    "PRK05",
    "PRK06",
    "PRK07",
    "SBH01",
    "SBH02",
    "SBH03",
    "SBH04",
    "SBH05",
    "SBH06",
    "SBH07",
    "SBH08",
    "SBH09",
    "SWK01",
    "SWK02",
    "SWK03",
    "SWK04",
    "SWK05",
    "SWK06",
    "SWK07",
    "SWK08",
    "SWK09",
    "SGR01",
    "SGR02",
    "SGR03",
    "TRG01",
    "TRG02",
    "TRG03",
    "TRG04",
    "WLY01",
    "WLY02",
]


url = "https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=year&zone="

for index in range(len(zoneCode)):
    response = urllib.request.urlopen(url + zoneCode[index])

    data = json.loads(response.read())

    with open('Jadual Waktu Solat' + zoneCode[index] + '.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
