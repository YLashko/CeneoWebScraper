class Opinion():
    def __init__(self):
        self.data = {}

    def set_data(self, key = '', data = ''):
        self.data[key] = data
    
    def get_data_key(self, key = ''):
        return self.data[key]

    def get_data(self):
        return self.data