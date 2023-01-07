import pandas as pd

def perf_backtest(df, colRet='Fut_return_period', colPos='PosStop', colPred='yPredBacktest'):
    listPerf = []
    lenD = len(df)
    i = 0
    while i < lenD:
        pred = df.iloc[i][colPred]
        ret = df.iloc[i][colRet]
        if pred == 1:  # If the model predicts to INVEST (1)
            listPerf.append(ret)
            pos = df.iloc[i][colPos]
            i += int(pos)
        else:
            i += 1

    df_return = pd.DataFrame(listPerf, columns=['return'])
    df_return['cumulative_return_in_Period'] = (1 + df_return['return']).cumprod() - 1

    df_return.to_csv(f'datasets/dfBacktestJustYlabel1.csv')

    print(f'How many predictions = 1: {len(listPerf)}\n')

    return listPerf, df_return
