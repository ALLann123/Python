#!/usr/bin/python3
import pdfplumber

#open the pdf and pass its contents to pdfplumber
with pdfplumber.open("output.pdf") as pdf:
    all_text = ""
    for page in pdf.pages:
        all_text += page.extract_text() + "\n"


print(all_text)




"""
python .\extract_text_from_pdf.py
Generative AI in Research
Generative AI- Refers to the class of AI that can generate new content based on patterns learned
from existing data. Relies on Large Language Models
Large Language Models- Is a type of AI model trained on massive amounts of text data to
understand and generate human like language. Example Chat GPT, Deepseek, Claude, Gemini.        
Prompts- Refers to instructions we give to a large language model to tell it what to do.        
A key concept that we can build using Gen AI to help in research is Retrieval Augmented
Generation.
Retrieval-Augmented Generation (RAG)
RAG combines:
 Retriever → Searches your custom database (papers, datasets, reports). Database can be        
made from pdf’s, text files or CSV files from our research.
 Generator → Uses GenAI (GPT) to answer your question only based on retrieved
material from your database of PDFs.
Why RAG?
 Idea Generation from your own work.(Knowledge of the large language model Is based
on all your work)
 Chat GPT platform the large language model has been taught a lot of different things
leading to for it to hallucinate information. Using RAG helps in reducing hallucination
and answer is real from the provided sources. (RAG system adds citations where it got
the answer from all your documents )
 Keeps unpublished research private and no sending sensitive data to external AI.
 N/B -With RAG you have a personal AI research Assistant that reasons only from your
chosen literature.
Frameworks to build RAG include:
NO-Code Tools:
1. N8N- Drag and drop automation tool, open-source and self-hostable.
2. Flowise AI
3. LangFlow
4. Zapier
How will you use Gen AI as a researcher?
"I’ll use Generative AI to save time on routine parts of
research so I can focus on deeper thinking.
It will help me quickly find and summarize relevant studies,
suggest new ideas, and improve the clarity of my writing. I’ll
always double-check the information it gives me and be open
about when I’ve used it. For me, AI is a support tool, not a
replacement for my own analysis and judgment."

"""
