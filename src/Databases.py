# SERVIDOR DO YFINANCE - Baixando historico de cotacoes e salvando em CSV

#importing libraries
from datetime import datetime
from datetime import timedelta
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import numpy as np


class dataset():
    # ETFs uploaded so far:
    def __init__(self):
        self.descript_dict = {'XLP': 'U.S. Consumer Staples Sector ETF'}

    def list_of_assets(self):
        return list(self.descript_dict.keys())

    def importDatabase(self, asset):

        description = self.descript_dict[asset]  # Dictionary retrieve - getting the description of the asset you want to upload

        print(f'\nAsset to be uploaded: {asset} - {description}\n')
        asset_yfticker = yf.Ticker(asset)
        today = datetime.date(datetime.now())
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)

        # First, retrieve the last CSV dataset from directory
        # Second, update a new dataset from yfinance, check how many days should be uptaded in official dataset (from directory)
        # and merge this missing dates in our official dataset

        # Retrieve OFFICIAL DATASET from folder. If there is none (i.e. is a new stock), create a new one.
        try:
            # INSERT THE NAME OF THE LAST DATABASE YOU DOWNLOADED
            df_last = pd.read_csv(f'datasets/{asset}_historical_max.csv', index_col=0, parse_dates=True, delimiter=',')
            print(f'There is a dataset already')
            lastdate = df_last.iloc[len(df_last) - 1, :].name
            print(f'Last date updated = {lastdate}')
        except FileNotFoundError:
            print(f'Oh Oh! We need to build a new dataset')
            df_last = asset_yfticker.history(period="max",auto_adjust=False)
            df_last['ticker'] = asset
            df_last.to_csv(f'datasets/{asset}_historical_max.csv')
            lastdate = df_last.iloc[len(df_last) - 1, :].name
            print(f'Last date updated = {lastdate}')

        # ----------------------------------------------------------------------------------------------------
        # uploading recent dates from Yfinance database
        print(f'Updating the new daily info from Yfinance')

        now = datetime.now()
        if now.hour > 18: #we already have the data for today, so we will upload it too
            print(f'Since now is after the closing time of the Stock Exchange, we include the todays price')
            df_recent = asset_yfticker.history(start=lastdate, end=tomorrow, interval="1d",auto_adjust=False)
        else:#We dont have the closing price for today
            print(f'New date to be updated until (excluding this day): {today}')
            df_recent = asset_yfticker.history(start=lastdate, end=today, interval="1d", auto_adjust=False)
        df_recent['ticker'] = asset

        ##INTRADAY DATA INSTEAD OF JUST CLOSING DAY
        # df_recent = asset_yfticker.history(start=lastdate, end=yesterday, interval="15m")
        ##EXCLUDING PRE POST TRADING HOURS QUOTES
        # df_recent = df_recent[df_recent['Volume'] != 0]

        # Concatenando o dataframe antigo com o mais recente
        df_recent = df_recent[df_recent.index > lastdate]
        frames = [df_last, df_recent]

        df_new = pd.concat(frames)
        df = df_new
        df.drop_duplicates(keep='first')
        # saving a new csv file
        df.to_csv(f'datasets/{asset}_historical_max.csv')
        print('Done! CSV updated!\n')
#==================================================================================================

#DESCRIPTION OF THE DATASET

def description_dataset(df):
    #Columns names
    print(f'\nColumns List:\n{df.columns.tolist()}\n\n')

    #Check for missing values
    print("\nIs there missing values in columns\n\n")
    print(df.isnull().sum())

    #Dataset info (columns types, etc)
    print('\n\nColumns types\n\n')
    print(df.info(verbose=True, show_counts=True))
    print("\n")

    #Dataset descriptive
    print('\n\nDataset description\n\n')
    print(df.describe())

#==================================================================================================


if __name__ == "__main__":

    c = dataset()
    print(f'\n\n Dictionary of assets already in the database: \n{c.descript_dict}\n\n')

    c.importDatabase('KO')


