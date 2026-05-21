# --- Importar biblioteca pdf
from pypdf import PdfReader

# -- Funcao para obter os arquivos pdf
def obter_pdfs(arquivos: list) -> list:
    pdfs = []
    for arquivo in arquivos:
        reader = PdfReader(arquivo)
        pdfs.append(reader)
    return pdfs

