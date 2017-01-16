import re
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.crypt import Signer

SHEET_ID = '18iBUv_6dLe11qeEtMtM7f5sUIelHUFsALbYBZG2eFQ0'

def get_client():
    scope = ['https://spreadsheets.google.com/feeds']
    s = Signer.from_string(os.environ['GOOGLE_API_PRIVATE_KEY'].replace('\\n', '\n'))
    credentials = ServiceAccountCredentials(
        os.environ['GOOGLE_API_CLIENT_EMAIL'],
        s,
        scope,
    )
    return gspread.authorize(credentials)

def get_chapters_sheet():
    gc = get_client()
    return gc.open_by_key(SHEET_ID).sheet1

def get_lat_long(s):
    match = re.search(r'\((\-?\d+(\.\d+)?),\s*(\-?\d+(\.\d+)?)\)', s)
    if match:  # it's a lat long
        return float(match.group(1)), float(match.group(3))
    else:
        return None, None

def get_chapter_data():
    sheet = get_chapters_sheet()

    records = sheet.get_all_records()

    ret = []
    current_row = 2 # Skip the first row, which are just headers
    for record in records:
        name = record['Chapter']
        if name == '':
            continue

        retrow = {
            'name': name,
        }
        lat, lng = get_lat_long(record['Location'])
        if lat and lng:
            retrow["lat"] = lat
            retrow["long"] = lng
        else:
            continue

        retrow['facebook'] = record['Facebook']
        retrow['email'] = record['Contact Email']
        retrow['youtube'] = record['YouTube Channel']
        retrow['organizers'] = record['Organizers Page']
        retrow['calendar'] = record['Calendar']
        ret.append(retrow)

    return ret

