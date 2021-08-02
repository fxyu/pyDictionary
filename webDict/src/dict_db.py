import yaml
import pickle
import os

from .dict_func import yahoo, howjsay

class Config(dict):
    def __init__(self, fname):
        self.fname = fname

        with open(fname, 'r') as f:
            self._yaml = f.read()
            self._dict = yaml.load(self._yaml, Loader=yaml.FullLoader)
 
    def __getattr__(self, name):
        if self._dict.get(name) is not None:
            return self._dict[name]
        return None

    def save(self):
        with open(self.fname,'w') as file:
            sort_file = yaml.dump(self._dict, sort_keys=True)


    def print(self):
        print('Model configurations:')
        print('---------------------------------')
        print(self._yaml)
        print('')
        print('---------------------------------')
        print('')


class dict_db(dict):
    def __init__(self, fname='db.pkl'):
        # import pudb; pudb.set_trace()
        dirPath = os.path.dirname(__file__)
        self.fname = os.path.join(dirPath, fname)
        if os.path.isfile(self.fname):
            with open(self.fname, 'rb') as f:
                data = pickle.load(f)
                self._dict = data['dict']
                self._history = data['hist']
        else:
            self._dict = {}
            self._history = []


    def add(self, k, v):
        self._dict[k.lower()] = v

    def get(self, k):
        k = k.lower()
        if self._dict.get(k) is not None:
            data = self._dict[k]
            self.add(k, data)
        else:
            data = {
                'yahoo' : yahoo(k),
                'audio' : howjsay(k)
                }
        self.history_add(k)
        self.save()
        return data
        
    def getHistory(self):
        return self._history
        
    def history_add(self, k):
        if k in self._history:
            idx = self._history.index(k)
            self._history.pop(idx)
        
        self._history.append(k)
        
        if len(self._history) > 20:
            self._history.pop(0) 

    def __getattr__(self, name):
        if self._dict.get(name) is not None:
            return self._dict[name]
        return None

    def save(self):
        with open(self.fname, 'wb+') as f:
            data = {'dict':self._dict, 'hist': self._history}
            pickle.dump(data, f)
    
