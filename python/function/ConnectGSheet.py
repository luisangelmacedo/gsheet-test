#imports
import pygsheets
from pygsheets import Spreadsheet

def getDfFromWorkSheet(jsonPath, spreadSheetId, workSheetTitle):
  gClient = pygsheets.authorize(service_account_file = jsonPath)
  spreadSheet = Spreadsheet(gClient, spreadSheetId)
  workSheet = spreadSheet.worksheet_by_title("detalle")
  df = workSheet.get_as_df()

  return df