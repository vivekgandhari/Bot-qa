from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.exceptions import SessionClosedException
import pandas  as pd
import pickle
import warnings
import argparse
from extract_answer import *

warnings.filterwarnings("ignore")

# with open('./pickledFiles/random_forest_model.pkl', 'rb') as f:
#    random_forest_model = pickle.load(f)

# with open('./pickledFiles/columns.pkl', 'rb') as f:
#    model_columns = pickle.load(f)

# def prediction(prediction_df):
#     query_ = pd.get_dummies(pd.DataFrame(prediction_df, index = [0]), prefix=['Sector','job_sim'], columns=['Sector','job_sim'])
#     query = query_.reindex(columns = model_columns, fill_value= 0)
#     result = list(random_forest_model.predict(query))
#     final_result = round(result[0], 3)

#     return final_result

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
   put_text(extract_answer(querry))
   put_button("Try another question",onclick=main)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(main, port=args.port)
