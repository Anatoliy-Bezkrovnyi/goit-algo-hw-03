from queue import Queue
import random
import time

#Створити чергу заявок
requests_queue = Queue()
counter = 1

#Створити заявку та додати в чергу
def generate_request():
    global counter      
    new_request = f"Request {counter}"
    requests_queue.put(new_request)
    print(f"{new_request} was registered for processing.")    
    counter += 1

#Видалити заявку із черги, якщо черга не порожня
def process_request():
    while not requests_queue.empty():
        handled_request = requests_queue.get()
        print(f"{handled_request} was taken for processing.")
        time.sleep(1)
    else:
        print("All requests we handled, there are no items in queue to process.")    


while True:
    try:
        requests_to_generate = random.randint(1, 5)
        for _ in range(requests_to_generate):
            generate_request()
            time.sleep(1)
        
        requests_to_process = random.randint(1, 5)
        for _ in range(requests_to_process):
            process_request()
            time.sleep(1)
            
        
    except KeyboardInterrupt:
        print("Execution was interrupted by pressing ctrl-c combination.")
        break