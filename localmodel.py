from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Create Hugging Face pipeline
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 512,
        "do_sample": False,
        "repetition_penalty": 1.03,
    },
)

# Create chat model
chat_model = ChatHuggingFace(llm=llm)

# Invoke the model
response = chat_model.invoke("What is Generative AI?")

print(response.content)