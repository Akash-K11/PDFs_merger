from PyPDF2 import PdfMerger
from glob import glob
merger = PdfMerger()

merged_file = input("Enter name of merged pdf file to be created: ")
all_pdfs = [pdf for pdf in glob("*.pdf")]

way = int(input("For merging all pdf files in current directory, enter 0.\n"
                "For selecting pdf files one by one manually to merge, enter 1.\n"
                "Enter choice: "))

match way:
    case 0:
        [merger.append(pdf) for pdf in all_pdfs]

    case 1:
        selected_pdfs = list()

        print("Available PDFs in current directory:")
        [print(f"Index = {index_pdf}:", pdf) for index_pdf, pdf in enumerate(all_pdfs)]
        print("When list is over, enter -1.\n")

        while True:
            index_pdf = int(input("Enter index of pdf from above list: "))
            if index_pdf == -1:
                break
            else:
                selected_pdfs.append(index_pdf)

        [merger.append(all_pdfs[index_pdf]) for index_pdf in selected_pdfs]

merger.write(f"{merged_file}.pdf")
merger.close()
