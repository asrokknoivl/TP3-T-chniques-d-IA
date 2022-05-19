import logging
import threading
import time


list_agent = []

def thread_agent(id):
    logging.info("Thread %s: starting", id)
    agent = list_agent[id]
    agent.next_move()
    logging.info("Thread %s: finishing", id)




def main():
    for i in range(25):
        list_agent[i] = threading.Thread(target=thread_agent, args=(i,))
        list_agent[i].start()


if __name__ == '__main__':
    main()

