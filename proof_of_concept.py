# Proof of Concept

# Note:

import dash # to build web application
from dash import html

import transformers # to access Hugging Face model
from transformers import pipeline

import openai

from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

nlp = pipeline("ner", model="emilyalsentzer/Bio_ClinicalBERT")
