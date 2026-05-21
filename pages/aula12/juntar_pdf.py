# --- Importar biblioteca de pdf
from pypdf import PdfWriter

# --- Funcao para juntar os arquivos pdf em um unico arquivo
def juntar_pdfs(pdfs: list) -> object:
    pdf_writer = PdfWriter()
    for pdf in pdfs:
        pdf_writer.append(pdf)
    pdf_writer.write("pdfs_juntos.pdf")
    pdf_writer.close()

    # --- Ler os bytes de forma legivel
    with open("pdfs_juntos.pdf", "rb") as arquivo:
        pdf_bytes = arquivo.read()
    return pdf_bytes    
