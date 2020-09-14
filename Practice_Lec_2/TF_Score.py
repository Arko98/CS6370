import math 
def tokenize(document):
  '''
  Input a single sentence to tokenize, does not handle special characters or numbers
  '''
  tokens = document.lower().split(' ')
  vocab = set(tokens)
  return tokens,vocab

def tf_score(query,document):
  '''
  A simple term frequency matching score function 
  Score = sum of term frequency
  '''
  doc_tokens,doc_vocab = tokenize(document)
  q_tokens,q_vocab = tokenize(query)
  common_terms = list(q_vocab.intersection(doc_vocab))

  tf_dict = {}
  for i in common_terms:
    tf_dict[i] = 0

  for term in common_terms:
    for t in doc_tokens:
      if (term==t):
        tf_dict[term] +=1
  
  score = 0
  for term in tf_dict:
    score += tf_dict[term]

  damped_score = 0
  for term in tf_dict:
    if (tf_dict[term]>0):
      damped_score += (1 + math.log(tf_dict[term]))
  
  return score,damped_score,tf_dict
  
# Test Cases
'''
q = "information on cars"
d = "all you’ve ever wanted to know about cars"
'''
'''
q = "information on cars"
d = "information on trucks, information on planes, information on trains"
'''
'''
q = "red cars and red trucks"
d = "cops stop red cars more often"
'''

score, damped_score, tf_dict = tf_score(q,d)
print("Score: {}".format(score))
print("Log Score: {}".format(damped_score))
print("TF Dictionary: {}".format(tf_dict))
