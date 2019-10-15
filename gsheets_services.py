# import modules
import os
from dotenv import load_dotenv
load_dotenv()
from httplib2 import Http
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from random import randint

SPREADHSEET_ID = os.getenv('SPREADSHEET_ID')

def authorize_sheet():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    # connect to google sheets
    gc = gspread.authorize(credentials)
    # open Daily Quote Email workbook
    wks = gc.open_by_key(SPREADHSEET_ID)
    #wks = gc.open("Daily Quote Email")
    # Open sheet by title
    sheet = wks.worksheet("Quotes")
    return sheet

def get_random_row(sheet):
    # Get length of column to use in random
    x = len(sheet.col_values(1))
    # get random number
    randomRow = randint(0,x)
    return randomRow

def get_book(sheet, randomRow):
    book = sheet.cell(randomRow, 2).value
    return book

def get_quote(sheet, randomRow):
    quote = sheet.cell(randomRow, 3).value
    return quote

def get_kt(sheet, randomRow):
    kt = sheet.cell(randomRow, 4).value
    return kt
