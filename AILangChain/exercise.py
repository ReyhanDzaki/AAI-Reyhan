from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import gradio as gr
openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="Empty"
)

def bot(InputBelow):
    temp = """Question: {question}
    please lay out step by step answer:
    """
    prompt = PromptTemplate(template=temp, input_variables=["question"])
    formated_prompt =prompt.format(question=str(InputBelow))
    return openai.invoke(formated_prompt).content

demo = gr.Interface(fn=bot, inputs="text", outputs="text")

demo.launch(share=True)