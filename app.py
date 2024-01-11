
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

# 12/08/2023
# I copied this code from ChatGPT. It was generated with the prompt:
# How can I "chunk" a large block of context so that it fits in the token limit for the OpenAI API?
import openai

def tokenize(text):
    return openai.GPT3Tokenizer.encode(text)

def chunk_text(text, max_tokens=2048, overlap=50):
    tokens = tokenize(text)
    chunks = []

    start = 0
    while start < len(tokens):
        end = min(start + max_tokens, len(tokens))
        chunk_tokens = tokens[start:end]

        # Ensure we end at a sentence boundary if possible
        if end < len(tokens):
            while not chunk_tokens[-1].endswith(('.', '!', '?')):
                end -= 1
                chunk_tokens = tokens[start:end]

        chunk = openai.GPT3Tokenizer.decode(chunk_tokens)
        chunks.append(chunk)
        start = end - overlap  # Overlap for context

    return chunks

# Example Usage
text = "Your very large text here..."
chunks = chunk_text(text)

# Process each chunk with OpenAI API...


def main():
    pass


if __name__ == '__main__':
    main()