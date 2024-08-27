from pypdf import PdfMerger
pdfs: list[str] = []
while 1:
    pdf_input: str = input("Write name of pdf file (leave empty, if you want to end adding pdf's): ")
    if not pdf_input:
        break
    else:
        splited_pdf: list[str] = pdf_input.split(".")
        if splited_pdf[len(splited_pdf)-1] == "pdf":
            result_pdf_name: str = ".".join(splited_pdf)
        else:
            result_pdf_name: str = ".".join(splited_pdf)+".pdf"
        pdfs.append(result_pdf_name)
        
merger: PdfMerger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)
    
merger.write("result.pdf")
merger.close()