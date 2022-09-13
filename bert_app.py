
import streamlit as st

import deepl
auth_key = "9d5d6377-86f6-5862-90e2-783b691526a2:fx" 
translator = deepl.Translator(auth_key)

from summarizer import Summarizer
#from transformers import pipeline



@st.cache #decorator
def translate(text):
  new_text = translator.translate_text(text, target_lang="EN-GB")
  body = new_text.text
  model = Summarizer('distilbert-base-uncased', hidden=[-1,-2], hidden_concat=True)
  result = model(body, num_sentences=3)
  final_text = translator.translate_text(result, target_lang="IT")
  return final_text.text




#@st.cache
#def translate3(text):
  #new_text = translator.translate_text(text, target_lang="EN-GB")
  #body = new_text.text
  #model = pipeline("summarization")
  #result = model(body, min_length=25, max_length=60)
  #final_text = translator.translate_text(result, target_lang="IT")
  #return final_text.text

#@st.cache
#def translate4(text):
  #new_text = translator.translate_text(text, target_lang="EN-GB")
  #body = new_text.text
  #model = pipeline("summarization", model="t5-large", tokenizer="t5-large", framework="tf")
  #result = model(body, min_length=25, max_length=60)
  #final_text = translator.translate_text(result, target_lang="IT")
  #return final_text.text



  

def main():
	

	# Title
	st.title("Demo di News Summarizer")
	st.subheader("Riassumere testi in pochi semplici click")
	

	# Summarization
	if st.checkbox("Get the summary of your text"):
		st.subheader("Sto lavorando anche con altri modelli, per il momento condivido questa demo con BERT ")

		message = st.text_area("Enter Text","Type Here....")
		summary_options = st.selectbox("Choose Summarizer",['bert','cercherò in settimana di caricare anche altri modelli per avere più confronti su performance'])
		if st.button("Summarize"):
			if summary_options == 'bert':
				st.text("Using Bert Summarizer ..")
				summary_result = translate(message)
				
			elif summary_options == 'cercherò in settimana di caricare anche altri modelli per avere più confronti su performance':
				st.text("Using Bert Summarizer ..")
				summary_result = translate(message)
			
			#elif summary_options == 'pipeline api':
				#st.text("Using Pipeline API Summarizer ..")
				#summary_result = translate3(message)
				
			#elif summary_options == 't-5 large':
				#st.text("Using t-5 Summarizer ..")
				#summary_result = translate4(message)
				
			#else:
				#st.warning("Using Default Summarizer")
				#st.text("Using Gensim Summarizer ..")
				#summary_result = translate(message)
			st.success(summary_result)

if __name__ == '__main__':
	main()
	
