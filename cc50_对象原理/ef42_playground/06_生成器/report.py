import fileparse
from stock import Stock
from portfolio import Portfolio

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as file:
        portdicts = fileparse.parse_csv(file,
                                        select=['name','shares','price'],
                                        types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    return Portfolio(portfolio)