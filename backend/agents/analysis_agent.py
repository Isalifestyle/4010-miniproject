from utils.nlp_utils import call_groq_api

def analyze_data(data):
    summary = ""
    for question, content in data.items():
        summarized_text = call_groq_api(content, question)
        summary += f"Question: {question}\nAnswer: {summarized_text}\n\n"
    return summary
