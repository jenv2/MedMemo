# MedMemo

# Proof of concept
To compile and run the code in proof_of_concept.py, download the file and open it in a IDE with Python to run it. Packages such as dash, transformers, openai, tensorflow, and langchain must be installed on your device using "pip install [package name]" in your system's shell.

The operating system used to build this project is Windows 11 Home edition, 23H2 version. The system type is a 64-bit operating system and x64-based processor.

IDLE IDE was used to initially compile and run the code. The compiler used to build this project is Python 3.9.6 64-bit.


# Abstract
This document proposes a web application called MedMemo that allows a user to copy and paste a transcript of their healthcare provider visit into a text box. MedMemo will then utilize a deep learning model and a large language model to give the user a structured notes document of their visit with some additional information. This will allow patients to have a summary of all information shared during a healthcare visit, including their own specific personal questions that are typically not shared on a traditional healthcare visit record. 

# Conceptual Design
There exists a public deep learning model titled Bio_ClinicalBERT on Hugging Face that is used to identify and label medical related information in a piece of text. For example, it will label “high blood pressure” as a condition, “shortness of breath” as a symptom, “morphine” as a prescribed medication, etc. This model will be hosted using Render to make it available via API. Tensorflow will be used as a deep learning backend. 

Then, using prompt engineering, the output of the deep learning model will be used to fill in a specific input for the OpenAI API, which will then print to the user a specifically formatted healthcare visit summary. The deep learning model API endpoint and the OpenAI API will be connected using LangChain. 

Finally, the web application will be built using Plotly Dash with Python for the machine learning aspects and HTML to build the frontend. 