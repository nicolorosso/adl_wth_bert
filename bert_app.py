
import streamlit as st

import deepl
auth_key = "9d5d6377-86f6-5862-90e2-783b691526a2:fx" 
translator = deepl.Translator(auth_key)

from summarizer import Summarizer,TransformerSummarizer
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("google/pegasus-multi_news")

model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-multi_news")

@st.cache #decorator
def translate(text):
  new_text = translator.translate_text(text, target_lang="EN-GB")
  body = new_text.text
  model = Summarizer('distilbert-base-uncased', hidden=[-1,-2], hidden_concat=True)
  result = model(body, num_sentences=3)
  final_text = translator.translate_text(result, target_lang="IT")
  return final_text.text

@st.cache
def translate2(text):
  new_text = translator.translate_text(text, target_lang="EN-GB")
  body = new_text.text
  model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-multi_news")
  result = model(body, min_lenghts=80)
  final_text = translator.translate_text(result, target_lang="IT")
  return final_text.text



  

def main():
	

	# Title
	st.title("News Summarizer")
	st.subheader("Riassumere testi in pochi semplici click")
	

	# Summarization
	if st.checkbox("Get the summary of your text"):
		st.subheader("Summarize Your Text")

		message = st.text_area("Enter Text","Type Here....")
		summary_options = st.selectbox("Choose Summarizer",['bert','pegasus'])
		if st.button("Summarize"):
			if summary_options == 'bert':
				st.text("Using Bert Summarizer ..")
				summary_result = translate(message)
			elif summary_options == 'pegasus':
				st.text("Using Pegasus Summarizer ..")
				summary_result = translate2(message)
			else:
				st.warning("Using Default Summarizer")
				st.text("Using Gensim Summarizer ..")
				summary_result = translate(message)
			st.success(summary_result)

if __name__ == '__main__':
	main()
	
