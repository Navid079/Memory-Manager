from ..models.Page import Page

def parseFile(fileName):
  with open(fileName, 'r') as file:
    references = file.readline()
    references = [ref.strip(' ') for ref in references.split(',')]
    mem_size = int(file.readline())
    page_labels = list(set(references))
    page_refs = dict.fromkeys(page_labels, [])
    for i, ref in enumerate(references):
      page_refs[ref].append(i)
    pages = [Page(label, page_refs[label]) for label in page_labels]

    return pages, mem_size