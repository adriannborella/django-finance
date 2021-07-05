import pandas as pd

class SearchCotizationIntrument(object):

    def __init__(self, url) -> None:
        super().__init__()
        data = pd.read_html(url)
        self.df = data[0]

    def search(self, code):
        search = self.df.where(self.df[0] == code).dropna()
        file = search.to_numpy()
        return float(file[0][1][0:-2].replace('.', '') + '.' + file[0][1][-2:])