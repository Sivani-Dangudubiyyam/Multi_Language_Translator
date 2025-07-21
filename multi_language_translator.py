import streamlit as st
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# Load model and tokenizer
@st.cache_resource
def load_model():
    model_name = "facebook/m2m100_418M"
    tokenizer = M2M100Tokenizer.from_pretrained(model_name)
    model = M2M100ForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# Supported language codes (can be extended)
LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh",
    "Arabic": "ar",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Portuguese": "pt",
    "Italian": "it"
}


# Streamlit UI
st.set_page_config(page_title="Multi-language Translator", layout="centered")
st.title("🌐 Multi-language Machine Translator")
st.markdown("Powered by Facebook M2M100 model (418M)")

# Inputs
text = st.text_area("Enter text to translate", height=150)
src_lang = st.selectbox("From Language", list(LANGUAGES.keys()), index=0)
tgt_lang = st.selectbox("To Language", list(LANGUAGES.keys()), index=1)

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text to translate.")
    else:
        src_lang_code = LANGUAGES[src_lang]
        tgt_lang_code = LANGUAGES[tgt_lang]

        tokenizer.src_lang = src_lang_code
        encoded = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**encoded, forced_bos_token_id=tokenizer.get_lang_id(tgt_lang_code))
        translated = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

        st.markdown("### 📝 Translated Text:")
        st.success(translated)
