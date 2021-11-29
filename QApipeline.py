import math
import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
import sentencepiece

max_answer_length = 20

def QApipeline(question,paragraph,model,tokenizer):
  encoding = tokenizer.encode_plus(text=question,text_pair=paragraph)
  inputs = encoding['input_ids']
  sentence_embedding = encoding['token_type_ids']
  tokens = tokenizer.convert_ids_to_tokens(inputs)
  output = model(input_ids=torch.tensor([inputs]),token_type_ids=torch.tensor([sentence_embedding]))
  start_scores = output['start_logits']
  end_scores = output['end_logits']
  skip = tokens.index('[SEP]')
  start_index,end_index,confidence = span_calculator(skip,start_scores,end_scores)
  answer = ' '.join(tokens[start_index:end_index+1])
  corrected_answer = ''
  for word in answer.split():
    if word[0:2] == '##':
        corrected_answer += word[2:]
    else:
        corrected_answer += ' ' + word
  return corrected_answer, confidence


def span_calculator(skip,start_logits,end_logits):
  score_check = float('-inf');
  for start_index in range(skip+1,len(start_logits[0])):
    for end_index in range(start_index+1,min(start_index+max_answer_length,len(end_logits[0]))):
      if(start_logits[0][start_index]+end_logits[0][end_index]>score_check):
        score_check = start_logits[0][start_index]+end_logits[0][end_index]
        answer_start_point = start_index
        answer_end_point = end_index
  confidence = math.exp(score_check)/(1+math.exp(score_check))
  return answer_start_point,answer_end_point,confidence
