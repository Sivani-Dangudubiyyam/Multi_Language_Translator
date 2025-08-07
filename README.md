

## 🌍 Multi-language Machine Translator

This is a **Streamlit web app** that translates text between **100+ languages** using **Facebook's M2M100 Transformer model** from HuggingFace 🤗. Unlike many translators that only translate to/from English, M2M100 supports **many-to-many translation** directly between languages.



---

### 🚀 Features

* Translate text between multiple languages
* Powered by **facebook/m2m100\_418M**
* Clean and interactive **Streamlit UI**
* Works locally, fully open-source

---

### 🛠️ Tech Stack

* **Python**
* **Streamlit** for UI
* **Hugging Face Transformers**
* **M2M100 (facebook/m2m100\_418M)** multilingual model

---
### Screenshots
![App Screenshot](https://github.com/Sivani-Dangudubiyyam/Multi_Language_Translator/blob/main/preview1.png)

---
![App Screenshot](https://github.com/Sivani-Dangudubiyyam/Multi_Language_Translator/blob/main/preview.png)

---
![App Screenshot](https://github.com/Sivani-Dangudubiyyam/Multi_Language_Translator/blob/main/preview2.png)

---
![App Screenshot](https://github.com/Sivani-Dangudubiyyam/Multi_Language_Translator/blob/main/preview3.png)



---
### 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/Sivani-Dangudubiyyam/Multi_Language_Translator
cd Multi_Language_Translator
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install streamlit transformers torch sentencepiece
```

---

### ▶️ Run the App

```bash
streamlit run multi_language_translator.py
```

Then open `http://localhost:8501` in your browser.

---

### 🌐 Supported Languages

This app supports **100+ languages**, including:

* English (`en`)
* Hindi (`hi`)
* French (`fr`)
* German (`de`)
* Spanish (`es`)
* Chinese (`zh`)
* Arabic (`ar`)
* Russian (`ru`)
* Japanese (`ja`)
* Korean (`ko`)
* Portuguese (`pt`)
* Italian (`it`)

> For a full list, see: [M2M100 Supported Languages](https://huggingface.co/facebook/m2m100_418M#supported-languages)

---

### 📁 File Structure

```
multi_language_translator.py     # Main Streamlit app
README.md                        # Project readme
requirements.txt                 # Dependencies (optional)
```

---

### 📚 Example

**Input**:

> `"How are you?"` (English → Hindi)

**Output**:

> `"तुम कैसे हो?"`

---

### 🙌 Acknowledgements

* [🤗 Hugging Face Transformers](https://huggingface.co/transformers/)
* [Facebook AI – M2M100 model](https://huggingface.co/facebook/m2m100_418M)
* [Streamlit](https://streamlit.io/)

