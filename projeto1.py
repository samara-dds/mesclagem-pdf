import PyPDF2
import os

merger = PyPDF2.PdfMerger()
lisata_arquivos = os.listdir("arquivos")
lisata_arquivos.sort()
print(lisata_arquivos)

for arquivo  in lisata_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

    merger.write("PDF Final.pdf")