from queue import Queue

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
    else:
        print("All requests we handled successfully.")


while True:
    command = input("Enter the command: ")
    if command == "generate": 
        for _ in range(5):
            generate_request()
    elif command == "solve": 
        process_request()
    elif command == "stop": 
        break