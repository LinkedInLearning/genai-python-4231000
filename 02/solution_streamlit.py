import streamlit as st
from openai import OpenAI

# Key in .streamlit/secrets.toml
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_image_description(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Du bist ein kreativer Assistent."},
            {"role": "user", "content": f"Erstelle eine kreative Beschreibung für ein Bild, das Folgendes darstellt: {prompt}"}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content

def generate_image(description):
    response = client.images.generate(
        prompt=description,
        n=1,
        size="1024x1024",
        model="dall-e-2"
    )
    image_url = response.data[0].url
    return image_url

def main():
    st.title("Bildgenerator")
    user_input = st.text_input("Geben Sie einen kurzen Text ein für das Bild ein:")
    if st.button("Bild generieren"):
        description = generate_image_description(user_input)
        st.write("Generierte Bildbeschreibung:", description)
        image_url = generate_image(description)
        st.write("Generiertes Bild wird angezeigt ...")
        st.image(image_url, caption="Generiertes Bild")

if __name__ == "__main__":
    main()
