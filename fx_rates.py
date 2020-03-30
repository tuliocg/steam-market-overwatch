__author__ = 'https://github.com/tuliocg'

import requests
import os
from datetime import datetime, timedelta
from queries import get_last_fxdate
from utils import string_to_date

api_key = os.environ.get('APIKEY_ALPHA_ADVANTAGE')

class FXRate():

    fx_rate = {}
    fx_rate['value'] = []
    fx_rate['date'] = []
    fx_rate['source'] = []

    def _get_fxrate_historical(self, starting_date='2010-01-01', max_date=None):
        '''
        function used to read fx_historical data from api and populate table fx_rate
        '''   
        print(starting_date)
        print(max_date)

        url = 'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=USD&to_symbol=BRL&apikey='+api_key

        r_json = requests.get(url).json()
        r_timeseries = r_json['Time Series FX (Monthly)']

        for key in r_timeseries:
            print('key {key} start {start} max {maxd}'.format(key=key, start=starting_date, maxd=max_date))
            print(key > starting_date and key <= max_date)
            if key > starting_date and key <= max_date:
                self.fx_rate['value'].append((float(r_timeseries[key]['4. close']) +float(r_timeseries[key]['1. open']) + \
                                            float(r_timeseries[key]['2. high']) + float(r_timeseries[key]['3. low']))/4)
                self.fx_rate['date'].append(key)
                self.fx_rate['source'].append('historical')

    def get_fxrate_current(self):
        '''
        function used to read fx current date data from api and populate table fx_rate
        '''   

        last_date = '2020-01-03' #later change this date do get_last_fxdate()
        yesterday = datetime.today() - timedelta(days=1)
        yesterday = yesterday.strftime('%Y-%m-%d')


        if last_date < yesterday:
            self._get_fxrate_historical(last_date, yesterday)

        print('Historical FX Retrieved:')
        print(self.fx_rate)

        url = 'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=USD&to_symbol=BRL&apikey='+api_key

        r_json = requests.get(url).json()
        r_timeseries = r_json['Time Series FX (Monthly)']
        '''
        fx historical working, but for now i'm going to implement on local currency (BRL)
        '''

if __name__ == '__main__':
    fx = FXRate()
    print(fx.get_fxrate_current())
