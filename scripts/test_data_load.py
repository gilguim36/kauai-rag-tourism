import json
from PyPDF2 import PdfReader
import os

# Caminhos dos arquivos
json_path = os.path.join("data", "kauai.json")
pdf_path = os.path.join("data", "kauai-maps.pdf")

# Teste JSON
print("=== TESTE JSON ===")
try:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        print(f"Arquivo JSON carregado com sucesso! Total de atrações: {len(data)}")
        print("Primeira atração:", data[0])
except Exception as e:
    print("Erro ao carregar JSON:", e)

# Teste PDF
print("\n=== TESTE PDF ===")
try:
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)
    print(f"Arquivo PDF carregado com sucesso! Total de páginas: {num_pages}")
    print("Primeiras 300 letras do PDF:")
    text = reader.pages[0].extract_text()
    print(text[:300])
except Exception as e:
    print("Erro ao carregar PDF:", e)