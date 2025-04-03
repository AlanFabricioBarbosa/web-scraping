# Script de Web Scraping para Baixar e Compactar PDFs

Este script faz **web scraping** na página da ANS para baixar anexos em PDF relacionados à atualização do **Rol de Procedimentos**. Os arquivos baixados são armazenados localmente e depois compactados em um **arquivo ZIP**.

---

## Como Funciona?
1. **Acessa a página da ANS** e obtém todos os links disponíveis.
2. **Filtra os links** que contêm "Anexo_I" ou "Anexo_II" e terminam com `.pdf`.
3. **Baixa os arquivos PDF** para a pasta `pdfs/`.
4. **Compacta os arquivos** em um ZIP chamado `anexos.zip`.
---

## Criando o `requirements.txt`
Se ainda não criou o `requirements.txt`, execute:
``` bash
pip freeze > requirements.txt
```
## Como Executar
### Criar um ambiente virtual
```
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
venv\Scripts\activate     # No Windows

```
## Rodar o script
```
python3 main.py

```
## Explicação do Código

### Coletando Links
#### O BeautifulSoup é usado para extrair todos os links <a> da página e encontrar aqueles que contêm "Anexo_I" ou "Anexo_II" e terminam com .pdf.
### Baixando os PDFs
#### Para cada link válido, o código faz um requests.get(url) e salva o conteúdo na pasta pdfs/.
### Compactando os Arquivos
####Depois de baixar todos os PDFs, o script cria um anexos.zip contendo todos os arquivos da pasta


