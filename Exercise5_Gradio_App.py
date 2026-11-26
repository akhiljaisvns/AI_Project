import gradio as gr

def respond(message, history):
    text = message.lower().strip()
    if any(w in text for w in ["hello", "hi", "namaste"]):
        return "Hello! Ask me about Python, Machine Learning, Generative AI or RAG."
    if "machine learning" in text or text == "ml":
        return "Machine Learning learns patterns from examples, such as classifying a new complaint using previously labelled complaints."
    if "generative ai" in text or "genai" in text:
        return "Generative AI creates new content such as text, images, audio or video."
    if "rag" in text:
        return "RAG retrieves relevant information from trusted documents and supplies it to a language model as context."
    if "python" in text:
        return "Python is used for data analysis, machine learning, image processing and web applications."
    return "I can explain Python, Machine Learning, Generative AI and RAG."

demo = gr.ChatInterface(
    fn=respond,
    title="GOT-A AI Learning Assistant",
    description="Welcome! Ask about Python, Machine Learning, Generative AI or RAG.",
    examples=["What is Machine Learning?", "Explain Generative AI.", "What is RAG?"]
)
demo.launch(share=False)
