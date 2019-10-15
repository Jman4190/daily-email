import os
from dotenv import load_dotenv
load_dotenv()
import math
from gsheets_services import authorize_sheet, get_random_row, get_book, get_quote, get_kt
from email_services import send_email

EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SPREADHSEET_ID = os.getenv('SPREADSHEET_ID')

sheet = authorize_sheet()
randomRow = get_random_row(sheet)
book = get_book(sheet, randomRow)
quote = get_quote(sheet, randomRow)
kt = get_kt(sheet, randomRow)
send_email(book, quote, kt)
print('Done.')
