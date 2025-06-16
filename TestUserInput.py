import numpy as np
from tensorflow.keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import string
import re
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = load_model("spam_detector.h5")

max_len_subject = 20
max_len_message = 200

with open('tokenizer_subj.pkl', 'rb') as f:
    tokenizer_subj = pickle.load(f)
with open('tokenizer_msg.pkl', 'rb') as f:
    tokenizer_msg = pickle.load(f)
    

def calculate_meta_features(message):
    msg_length = len(message)
    special_char_count = sum(1 for c in message if c in string.punctuation)
    digit_count = len(re.findall(r'\d', message))
    word_count = len(message.split())
    return np.array([msg_length, special_char_count, digit_count, word_count]).reshape(1, -1)

def preprocessTextData(subject, message):
    subj_seq = tokenizer_subj.texts_to_sequences([subject])
    msg_seq = tokenizer_msg.texts_to_sequences([message])
    subj_pad = pad_sequences(subj_seq, maxlen=max_len_subject, padding='post', truncating='post')
    msg_pad = pad_sequences(msg_seq, maxlen=max_len_message, padding='post', truncating='post')
    return subj_pad, msg_pad

while True:
    print("\nWpisz temat (Subject) wiadomości (lub wpisz 'exit' aby zakończyć):")
    subject = input().strip()
    if subject.lower() == 'exit':
        break
    
    print("Wpisz treść wiadomości (Message):")
    message = input().strip()
    
    meta = calculate_meta_features(message)
    
    subject, message = preprocessTextData(subject, message)
    
    pred_prob = model.predict([subject, message, meta])[0][0]
    
    label = "SPAM" if pred_prob > 0.5 else "NOT SPAM"
    
    print(f"Model ocenił tę wiadomość jako: {label} (prawdopodobieństwo spamu: {pred_prob:.2f})")
