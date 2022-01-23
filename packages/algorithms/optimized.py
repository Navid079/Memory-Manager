from packages.models.Memory import Memory

def optimized(pages, mem_size):
  memory = Memory(mem_size)
  page_faults = 0
  while True:
    needed_page = None
    for page in pages:
      if page.is_referenced(memory.time):
        needed_page = page
        break
    if needed_page is None: break
    page_fault = memory.get_page(needed_page)
    if page_fault:
      page_faults += 1
      index = memory.get_empty_frame()
      if index == -1:
        ref = 0
        for i, frame in enumerate(memory.frames):
          if frame.get_next_reference(memory.time) == -1:
            index = i
            break
          if frame.get_next_reference(memory.time) > ref:
            ref = frame.get_next_reference(memory.time)
            index = i
      memory.insert_page(needed_page, index)
    memory.save_history()
  
  return memory, page_faults