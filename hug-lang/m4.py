from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
import torch

# to avoid seeing warnings
# from transformers.utils.logging import set_verbosity_error
# set_verbosity_error()

print(torch.cuda.is_available()) # print True if GPU is available
print(torch.cuda.get_device_name(0)) # print GPU name

model  = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1",device=0,max_length=100,truncation=True)

# Wrap it inside LangChain
llm = HuggingFacePipeline(pipeline=model)

# Create the prompt template for summarization
template = PromptTemplate.from_template(
    "Explain  {topic } in detail for a {age} year old to understand"
)

chain = template | llm

# Get user input
topic = input("\nEnter Topic :\n")
age = input("Enter target age for the topic to understand :\n")

# Execute the summarization chain
response = chain.invoke({"topic": topic , "age": age})

print("\n🔹 **Print the understanding of topic:**")
print(response)