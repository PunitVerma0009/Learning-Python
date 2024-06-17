from PyPDF2 import PdfWriter
def merge(pdfs,output):
    newmerge=PdfWriter()
    for i in pdfs:
        newmerge.append(i)
    newmerge.write(output) 
    newmerge.close()   
pdfs=["1st.pdf","2nd.pdf"]
output="new.pdf"
merge(pdfs,output)