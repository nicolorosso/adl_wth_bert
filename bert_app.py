
import streamlit as st

import deepl
auth_key = "9d5d6377-86f6-5862-90e2-783b691526a2:fx" 
translator = deepl.Translator(auth_key)

from summarizer import Summarizer,TransformerSummarizer
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("google/pegasus-multi_news")



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


@st.cache
def translate3(text):
  new_text = translator.translate_text(text, target_lang="EN-GB")
  body = new_text.text
  model = summarizer("pipeline")
  result = model(body, min_length=25, max_length=60)
  final_text = translator.translate_text(result, target_lang="IT")
  return final_text.text

@st.cache
def translate4(text):
  new_text = translator.translate_text(text, target_lang="EN-GB")
  body = new_text.text
  model = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
  result = model(body, min_length=25, max_length=60)
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
		summary_options = st.selectbox("Choose Summarizer",['bert','pegasus', 'pipeline api', 't-5 large'])
		if st.button("Summarize"):
			if summary_options == 'bert':
				st.text("Using Bert Summarizer ..")
				summary_result = translate(message)
			elif summary_options == 'pegasus':
				st.text("Using Pegasus Summarizer ..")
				summary_result = translate2(message)
			elif summary_options == 'pipeline api':
				st.text("Using Pipeline API Summarizer ..")
				summary_result = translate3(message)
			elif summary_options == 't-5 large':
				st.text("Using t-5 Summarizer ..")
				summary_result = translate4(message)
			else:
				st.warning("Using Default Summarizer")
				st.text("Using Gensim Summarizer ..")
				summary_result = translate(message)
			st.success(summary_result)

if __name__ == '__main__':
	main()
	
