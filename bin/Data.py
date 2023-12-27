import json
import os
import datetime
import base64


class Data:
    def __init__(self, name: str):
        self.data_file = 'data/data.datc'
        self.name = name
        self.year = str(datetime.date.today().year)
        
    def start_checks(self) -> dict:
        if not os.path.exists(self.data_file):
            self.create_file()
            return self.load_data()
        else:
            data = self.load_data()
            if not self.name in data:
                self.add_user(data=data)
            return self.check_year(data)

    def add_user(self, data):
        data[self.name] = {'data': {self.year: {}}}
        self.save_data(data)
        
    def save_data(self, data) -> None:
        with open(self.data_file, "w") as file:
            data = self.encode(json.dumps(data,indent=4, sort_keys=True)).decode()
            file.write(data)
            #json.dump(data, file, indent=4, sort_keys=True)

    def load_data(self) -> dict:
        try:
            with open(self.data_file, 'r') as file:
                data = self.decode(file.read())
                return json.loads(data)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            self.fix_data()
            return self.load_data()

    def create_file(self, error=False) -> None:
        if not error:
            data = self.load_data()
        else:
            data = {}
        data[self.name] = {'data': {self.year:{}}}


        #data[name]['data'][year] = {} to add a year
        #data[name]['data'][2022]['year/xx/xx'] = 8 to add a day with the hours studied
        self.save_data(data)
        
    

    def fix_data(self) -> None:
        if os.path.exists(self.data_file):
            choice = input(f'Data corruption Error! please undo any changes on {self.data_file} or type y to completely '
            'reset and erase your data: ')
            if choice == 'y':
                print('Your data is being resetted and erased...')
                os.remove(self.data_file)
                self.create_file(error=True)
            else:
                print(f'The program will without changing anything and the data file({self.data_file}) is still broken')
                quit()
        else:
            print('Data file has not been found creating a new one for you...')
            self.create_file(error=True)
            
    def check_year(self, data):
        year = str(datetime.date.today().year)
        if not year in data[self.name]['data']:
            data[self.name]['data'][year] = {}
        return data

    def set_data(self, data, date, amount):
        year = str(datetime.date.today().year)
        if not date in data[self.name]['data'][year]:
            data[self.name]['data'][year][date] = amount
        else:
            data[self.name]['data'][year][date] += amount

        self.save_data(data)


    @staticmethod
    def encode(data):
        return base64.b64encode(data.encode('utf-8'))

    @staticmethod
    def decode(base64_data):
        return base64.b64decode(base64_data).decode('utf-8')


