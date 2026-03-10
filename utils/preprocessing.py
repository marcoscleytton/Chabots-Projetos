import re
import string

def clean_text(text):
    """Remove pontuação, coloca em minúsculas e normaliza espaços."""
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def tokenize(text):
    """Divide o texto em tokens simples."""
    return text.split()