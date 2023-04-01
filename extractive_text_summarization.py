import pytextrank
import spacy
import streamlit as st
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")
input= st.text_area("Input text to summarize")
user_limit=int(len(input.split("."))/5)
doc=nlp(input)
output=""
if st.button("Summarize"):
    for i in doc._.textrank.summary(limit_sentences=user_limit):
        a=i.text
        output=output+a
    st.markdown(output)
    st.text("Length of Article="+str(len(input.split()))+" words")
    st.text("Length of summary="+str(len(output.split()))+" words")