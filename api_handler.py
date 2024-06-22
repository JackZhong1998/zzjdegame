import openai

def generate_code(description):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Generate code for: {description}",
        max_tokens=150
    )
    return response.choices[0].text.strip()