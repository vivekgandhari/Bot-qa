import pickle
import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
import sentencepiece
from filter_paragraphs import *
from QApipeline import *


def extract_answer(question):
  model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
  tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

  with open("paragraphs.txt","rb") as f:
    paragraphs = pickle.load(f)

  best_paragraphs = filter_paragraphs(paragraphs,question,10)

  n_best = 3
  score = float('-inf')
  element_count = 0;
  answers_group = []
  score_group = []
  elements_number = []
  for element in best_paragraphs:
    try:
      possible_answer,check_score  = pipeline(question,element,model,tokenizer)
      if(len(answers_group)<n_best):
        for k in range(len(answers_group)-1,-2,-1):
          if((k==-1) or (score_group[k]>check_score)):
            score_group.insert(k+1,check_score)
            answers_group.insert(k+1,possible_answer)
            elements_number.insert(k+1,element_count)
            break
      else:
        if(check_score>score_group[n_best-1]):
          answers_group.pop()
          score_group.pop()
          elements_number.pop()
          for k in range(len(answers_group)-1,-2,-1):
            if((k==-1) or (score_group[k]>check_score)):
              score_group.insert(k+1,check_score)
              answers_group.insert(k+1,possible_answer)
              elements_number.insert(k+1,element_count)
              break
    except:
        pass
    element_count += 1

  output = ""
  for i in range(n_best):
    output += str(i+1)+". Answer: "+ answers_group[i] + "\n" + "  Paragraph: "+best_paragraphs[elements_number[i]] + "\n\n"

  return output
