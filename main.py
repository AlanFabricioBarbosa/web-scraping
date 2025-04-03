import requests
from bs4 import BeautifulSoup
import os
import zipfile

def baixar_pdfs():
   url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
   response = requests.get(url)

   if response.status_code != 200:
      print("Erro ao acessar a página.")
      return

   soup = BeautifulSoup(response.text, 'html.parser')
   links = soup.find_all('a')

   pdf_urls = []

   for link in links:
      href = link.get('href')
      if href and ('Anexo_I' in href or 'Anexo_II' in href) and href.lower().endswith('.pdf'):
            pdf_urls.append(href if href.startswith("http") else f"https://www.gov.br{href}")

   if not pdf_urls:
      print("Nenhum PDF encontrado.")
      return

   os.makedirs("pdfs", exist_ok=True)

   for pdf_url in pdf_urls:
      nome_arquivo = pdf_url.split("/")[-1]
      print(f"Baixando {nome_arquivo}...")
      pdf_response = requests.get(pdf_url)
      with open(f"pdfs/{nome_arquivo}", "wb") as f:
            f.write(pdf_response.content)

   compactar_pdfs()

def compactar_pdfs():
   with zipfile.ZipFile("anexos.zip", "w") as zipf:
      for arquivo in os.listdir("pdfs"):
            zipf.write(os.path.join("pdfs", arquivo), arquivo)
   print("PDFs compactados com sucesso em anexos.zip")

if __name__ == "__main__":
   baixar_pdfs()

