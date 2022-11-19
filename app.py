import pandas as pd
import os
from binance.client import Client
import pandas as pd
import datetime, time
import numpy as np
from datetime import datetime, timedelta
from flask import Flask
from flask import request, render_template
from functions import GetHistoricalData, make_new_col, bootstrap, dataset_for_current_pred



app = Flask(__name__)

@app.route('/', methods = ['GET'])
def serve():
    return render_template('index.html')

@app.route('/interval', methods = ['GET'])
def interval():

    df_current = dataset_for_current_pred(Client)
    # Добавляем новую колонку
    df_current = make_new_col(df_current)
    # требуется для абсолютных значений запомнить текущую
    current_value = df_current['open'].values.astype(float)[-1]
    res_interval = bootstrap(df_current['change'].values, n_forcast=24, intervals_in_hour=60)*current_value
    
    return render_template('index.html', prediction_text='Interval: {} {}'.format(res_interval[0], res_interval[1]))


if __name__ == '__main__':
    app.run(port=3000)
