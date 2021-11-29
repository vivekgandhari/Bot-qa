from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.exceptions import SessionClosedException
# import pandas  as pd
import pickle
import warnings
import argparse
from extract_answer import *

warnings.filterwarnings("ignore")

def main():
    put_markdown(
        '''
        # FAWBOT demo
        '''
        , lstrip=True
    )
    querry = input("Question:")
    put_text(extract_answer(querry))
    put_button("Try another question",onclick=next_question)
    
def next_question():
   querry = input("Question:")
#    put_text(extract_answer(querry))
   put_button("Try another question",onclick=main)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(main, port=args.port)
