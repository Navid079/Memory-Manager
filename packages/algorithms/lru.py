from packages.models.Memory import Memory

def lru(pages, mem_size):
  memory = Memory(mem_size)
  page_faults = 0
  while True:
    needed_page = None
    for page in pages:
      if page.is_referenced(memory.time):
        needed_page = page
        break
    if needed_page is None: break
    page_fault = memory.get_page(page)
    if page_fault:
      page_faults += 1
      index = memory.get_empty_frame()
      if index == -1:
        ref = -1
        for i, frame in enumerate(memory.frames):
          if ref == -1 or frame.get_last_reference() < ref:
            ref = frame.get_last_reference()
            index = i
      memory.insert_page(page, index)
  
  return memory, page_faults