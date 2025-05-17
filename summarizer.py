import openai

def summarize_text(text_block: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert in analyzing game strategy discussions."},
            {"role": "user", "content": f"Summarize this Reddit thread:\n\n{text_block}"}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()
