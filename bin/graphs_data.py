import datetime
import pandas as pd
import matplotlib.pyplot as plt
class DataRead:
    def __init__(self, data):
        self.data = {'Mohamed Trfhgx': {'data': {'2022': {'2022-04-30': 4.0, '2022-05-01': 3.0, '2022-05-04': 5.0, '2022-05-05': 3.0, '2022-05-07': 3.0, '2022-05-08': 2.0, '2022-05-09': 5.0, '2022-05-10': 5.0, '2022-05-11': 2.0, '2022-05-14': 7.0, '2022-05-15': 4.1, '2022-05-16': 6.299999999999999, '2022-05-17': 5.5, '2022-05-18': 8.799999999999999, '2022-05-19': 10.0, '2022-05-20': 11.0, '2022-05-21': 10.0, '2022-05-22': 6.0, '2022-05-23': 4.0, '2022-05-24': 7.0, '2022-05-25': 6.2, '2022-05-26': 7.2}}}}
        self.name = 'Mohamed Trfhgx'

    def readable_data(self, year, month=datetime.date.today().month, week=None) -> dict:
        q1_data = self.data[self.name]['data'][year]
        q1_data = {a:b*(50/60) for a,b in q1_data.items()}
        df = pd.DataFrame(q1_data, index=[0])


        print(df)
        print(month)
        idx = pd.date_range(f'{year}-4-01', f'{year}-5-31')
        idx = [d.strftime('%Y-%m-%d') for d in idx]
        print(idx)


        s = pd.Series(q1_data)
        s.index = pd.DatetimeIndex(s.index)

        s = s.reindex(idx, fill_value=0)
        s = pd.DataFrame(s)
        s.plot.bar()
        plt.show()
        print(s)




x = DataRead('hi')
(x.readable_data('2022'))
