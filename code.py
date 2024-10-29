import gradio as gr
from transformers import pipeline

# Initialize the QA and Summarization pipelines
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# Sample context about Einstein
context = """
Albert Einstein was a theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics. 
His work is also known for its influence on the philosophy of science. He is best known to the general public for his mass–energy 
equivalence formula E = mc², which has been dubbed "the world's most famous equation." He received the 1921 Nobel Prize in Physics 
for his services to theoretical physics and his discovery of the photoelectric effect, a pivotal step in quantum theory. ...
"""

# Function for factoid QA
def answer_factoid_question(question):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Function for summarization
def summarize_text():
    summary = summarization_pipeline(context, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

# Gradio interface with colorful buttons and elements
with gr.Blocks(css=".btn-green {background-color: #4CAF50; color: white;} .btn-orange {background-color: #FF5733; color: white;}") as app:
    gr.Markdown("<h1 style='color: purple; text-align: center;'>🌟 Einstein QA & Summarization Tool 🌟</h1>")
    gr.Markdown("<h2 style='color: teal; text-align: center;'>Ask questions about Albert Einstein or summarize his achievements!</h2>")

    with gr.Row():
        question = gr.Textbox(label="🔍 Ask a question:", placeholder="E.g., What is Einstein famous for?", lines=1)
        answer = gr.Textbox(label="📝 Answer:", interactive=False)

    with gr.Row():
        submit_btn = gr.Button("❓ Get Answer", elem_classes="btn-green")
        summarize_btn = gr.Button("📝 Summarize Context", elem_classes="btn-orange")

    summary = gr.Textbox(label="🗒 Summary:", interactive=False)

    # Set button functionality
    question.submit(fn=answer_factoid_question, inputs=question, outputs=answer)
    submit_btn.click(fn=answer_factoid_question, inputs=question, outputs=answer)
    summarize_btn.click(fn=summarize_text, outputs=summary)

app.launch()
