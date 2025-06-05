import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

# Download required punkt tokenizer if not already downloaded
nltk.download('punkt')

def summarize_text(text, num_sentences):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return ' '.join(str(sentence) for sentence in summary)

def main():
    st.set_page_config(page_title="Text Summarizer", layout="centered")
    st.title("📄 AI Text Summarizer")
    st.write("Summarize any large block of text using extractive summarization (no API keys needed).")

    text_input = st.text_area("Enter text to summarize:", height=300)
    num_sentences = st.slider("Number of summary sentences", 1, 10, value=3)

    if st.button("Generate Summary"):
        if text_input.strip():
            summary = summarize_text(text_input, num_sentences)
            st.subheader("🔍 Summary")
            st.write(summary)
        else:
            st.warning("Please enter some text before summarizing.")

if __name__ == "__main__":
    main()