import requests
import time
# Directly include your Groq API key here
GROQ_API_KEY = "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"


def call_groq_api(text, topic):
    """Handles Groq API call and error handling."""
    prompt = f"""
    Generate a comprehensive research report based on the following content. The report should be structured as follows:

    1. Title: {topic}

    2. Introduction:
       - Provide a brief overview of the research topic.
       - Mention why this topic is important and relevant.

    3. Key Research Questions:
       - What are the key challenges or issues related to {topic}?
       - How has {topic} evolved over the past years?
       - What are the most cited papers or prominent studies on {topic}?

    4. Summarized Insights:
       - Summarize the most significant findings from reliable sources.
       - Present the insights in a concise and informative manner.
       - Highlight any emerging trends or critical viewpoints.

    5. Key Takeaways:
       - Summarize the most important points discussed.
       - Mention any contrasting perspectives or debates.

    6. References:
       - List the most relevant sources used in the report.
       - Include URLs or citations to original sources.

    The report should be written in a professional and academic tone. Keep the language clear and precise. Ensure that the report is factual and backed by credible sources. Provide accurate and up-to-date information.
    """
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json={
                "model": "llama3-groq-70b-8192-tool-use-preview",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            },
            headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
        )
        print("Status Code:", response.status_code)  # Print status code
        print("Response Text:", response.text)  # Print the response text
        response.raise_for_status()
        result = response.json()
        # Extract the completion from the response
        return result['choices'][0]['message']['content']
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Response: {response.text}")
        return f"HTTP error occurred: {http_err} - Response: {response.text}"
    except Exception as e:
        print(f"Error during Groq API call: {str(e)}")
        return f"Error during Groq API call: {str(e)}"



