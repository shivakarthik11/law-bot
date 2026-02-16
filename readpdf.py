from pypdf import PdfReader
reader=PdfReader("data/constitution.pdf") 
fulltext = ""
for page in reader.pages:
    text= page.extract_text()
    fulltext += text + "\n"
    print("total character :",len(fulltext))
chunks=[]
chunksize=1000
for i in range(0,len(fulltext),chunksize):
    chunk=fulltext[i:i+chunksize]
    chunks.append(chunk)
print("first chunk :",chunks[0])
