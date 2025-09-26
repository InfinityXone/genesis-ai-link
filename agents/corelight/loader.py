import json
from openai import OpenAI

def load_persona(path="persona.json"):
    with open(path) as f:
        return json.load(f)

def build_system_prompt(persona):
    return (
        f"You are {persona['name']} – {persona['role']}. "
        f"Speak in a {persona['tone']} tone. "
        f"You know: {persona['knowledge']}. "
        f"Your relationships: {persona['relationships']}. "
        f"Your style: {', '.join(persona['style_examples'])}."
    )

def get_client():
    return OpenAI(api_key="YOUR_OPENAI_KEY")

def chat(user_message, persona_path="persona.json"):
    persona = load_persona(persona_path)
    system_prompt = build_system_prompt(persona)
    client = get_client()
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    return resp.choices[0].message.content
