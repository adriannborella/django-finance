import pandas as pd


class HelperBase(object):

    def __init__(self, url) -> None:
        super().__init__()
        data = pd.read_html(url)
        self.df = data[0]