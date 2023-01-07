"""
INCREASING THE SAMPLE -> OPEN, CLOSE PRICES -> Creating a new dataset 2x bigger than the original: considering Open
and close prices, not only Close as before, increasing our datapoints
"""

# Importing packages needed
import time
import pandas as pd


def increase_dataset(df1):
    start = time.time()

    print(f"*** Important notice: the original df should not have Date as index! ***")
    dfcopy = df1.copy(deep=True)

    listCol = list(df1.columns)  # All the cols that are in our dataset
    listDel = ['Date', 'Open', 'High', 'Low', 'Close',
               'Volume']  # cols that should not be considered in our "Update Loop", since they are updated separately
    listUpdate = [col for col in listCol if col not in listDel]  # Updated list of columns

    # Nested loop running through the original dataframe and repeating what should be repetaded, and updating what should be updated
    newdf = pd.DataFrame(columns=listCol)
    origdf = 1
    for i in range(1, dfcopy.shape[0] * 2 - 1,
                   2):  # Notice that it starts at 1 (we are not able to use the first row, since we need previous data.
        # Also notice that i changes from 2 by 2 steps.

        for j in range(2):
            if j == 0:
                newdf.loc[i + j, 'Date'] = dfcopy.iloc[origdf]['Date'].replace(hour=10, minute=00)  # Updating the date
                newdf.loc[i + j, 'Close'] = dfcopy.iloc[origdf][
                    'Open']  # if we are in the first of the two rows, update OPEN
                newdf.loc[i + j, 'Open'] = dfcopy.iloc[origdf - 1][
                    'Open']  # if we are in the first of the two rows, update Open from previous date
                newdf.loc[i + j, 'High'] = dfcopy.iloc[origdf - 1][
                    'High']  # if we are in the first of the two rows, update High from previous date
                newdf.loc[i + j, 'Low'] = dfcopy.iloc[origdf - 1][
                    'Low']  # if we are in the first of the two rows, update Low from previous date
                newdf.loc[i + j, 'Volume'] = dfcopy.iloc[origdf - 1][
                    'Volume']  # if we are in the first of the two rows, update Volume from previous

                for col in listUpdate:  # Updating all the dataset's cols other than OHLCV
                    newdf.loc[i + j, col] = dfcopy.iloc[origdf - 1][col]

            else:
                newdf.loc[i + j, 'Date'] = dfcopy.iloc[origdf]['Date'].replace(hour=16, minute=00)  # Updating the date
                newdf.loc[i + j, 'Close'] = dfcopy.iloc[origdf][
                    'Close']  # if we are in the second of the two rows, update CLOSE
                newdf.loc[i + j, 'Open'] = dfcopy.iloc[origdf][
                    'Open']  # if we are in the second of the two rows, update Open from current date
                newdf.loc[i + j, 'High'] = dfcopy.iloc[origdf][
                    'High']  # if we are in the second of the two rows, update High from current date
                newdf.loc[i + j, 'Low'] = dfcopy.iloc[origdf][
                    'Low']  # if we are in the second of the two rows, update Low from current date
                newdf.loc[i + j, 'Volume'] = dfcopy.iloc[origdf][
                    'Volume']  # if we are in the second of the two rows, update Volume from current date

                for col in listUpdate:  # Updating all the dataset's cols other than OHLCV
                    newdf.loc[i + j, col] = dfcopy.iloc[origdf][col]

        origdf += 1

    newdf.set_index('Date')
    # newdf.index = pd.to_datetime(newdf.index)
    end = time.time()
    print(f'\n\nTime spent on this task: {end - start} seconds\n')
    return newdf

#========================================================================================================
if __name__ == "__main__":

    df = pd.read_csv(f'datasets/XLP_historical_max.csv', index_col=0, parse_dates=True, delimiter=',') #STAPLES
    df.reset_index(inplace=True)
    print(increase_dataset(df))
