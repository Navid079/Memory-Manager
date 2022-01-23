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
    index = -1
    while index == -1:
      index = memory.get_frame_on_pointer()
    memory.insert_page(page)
  #print memory trace