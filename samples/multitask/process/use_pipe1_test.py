#!/usr/bin/python3
# -*- coding: utf-8 -*-

# How to use pipe correctly in multiple processes(>2)?
# eg.   one producer sevral several consumer

import multiprocessing, time

def consumer(pipe,id):
    output_p, input_p = pipe
    input_p.close()                    
    while True:
        try:
            item = output_p.recv()
        except EOFError:
            break
        print("%s consume：%s" % (id,item))
        #time.sleep(3)      # if no sleep  these code will fault in Linux environment
                            # but windows environment is well
    print('Consumer done')
        
def producer(sequence, input_p):
    for item in sequence:
        print('produce：',item)
        input_p.send(item) 
        time.sleep(1)

if __name__ == '__main__':
    (output_p, input_p) = multiprocessing.Pipe()

    # create two consumer process
    cons_p1 = multiprocessing.Process(target=consumer,args=((output_p,input_p),1)) 
    cons_p1.start() 
    cons_p2 = multiprocessing.Process(target=consumer,args=((output_p,input_p),2))
    cons_p2.start() 

    output_p.close()
    
    sequence = [i for i in range(10)]
    producer(sequence, input_p)
    input_p.close()

    cons_p1.join()
    cons_p2.join()

