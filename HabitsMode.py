import time
import random
import pandas as pd
import pyexcel as p

def quotes():
    #Import quotes from file

    list = p.get_array(file_name="Quotes.ods")
    sheet = p.get_sheet(file_name="Quotes.ods")
    del sheet.row[filter_row]
    random_idx = random.randint(1,len(sheet)-1)

    quote = list[random_idx][0]
    quote = str(quote).split('\n')
    num_lines = len(quote)

    return quote, num_lines #as list of lines

def filter_row(row_index, row):
    result = [element for element in row if element != '']
    return len(result)==0

if __name__ == '__main__':
    print(quotes())