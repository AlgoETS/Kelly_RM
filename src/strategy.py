
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas_ta as ta
import pandas as pd

class Ema(Strategy):
    n1=20
    n2=80
    n3=150
    def init(self):
        close = self.data.Close
        self.ema20 = self.I(ta.ema, close.s, self.n1)
        self.ema80 = self.I(ta.ema, close.s, self.n2)
        self.ema150 = self.I(ta.ema, close.s, self.n2)

    def next(self):
        price = self.data.Close
        if crossover(self.ema20, self.ema80):
            self.position.close()
            self.buy()

        elif crossover(self.ema80, self.ema20):
            self.position.close()
            self.sell()
        pass
    
    def name():
        return " Exponential Moving Average"





class RsiOscillator(Strategy):

    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    # Do as much initial computation as possible
    def init(self):
        self.rsi = self.I(ta.rsi, pd.Series(self.data.Close), self.rsi_window)

    # Step through bars one by one
    # Note that multiple buys are a thing here
    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()

    def name():
        return " "

