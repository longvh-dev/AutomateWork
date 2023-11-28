import PyPDF2


# Extract text from PDF file
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return text


# Merge multiple PDF files
def merge_pdfs(input_paths, output_path):
    pdf_merger = PyPDF2.PdfMerger()
    for path in input_paths:
        pdf_merger.append(path)
    pdf_merger.write(output_path)
    pdf_merger.close()


# Adding Password Protection to PDF
def add_password_protection(input_path, output_path, password):
    with open(input_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        pdf_writer = PyPDF2.PdfFileWriter()

        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)
        pdf_writer.write(output_path)