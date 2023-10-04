import multiprocessing


def producer(sequence,input_p):
    for item in sequence:
        input_p.send(item)

def consumer(pipe):
    output_p,input_p = pipe
    input_p.close()
    while True :
        try:
            item = output_p.recv()
            print(item)
        except EOFError:
            break
if __name__=="__main__":
    (input_p, output_p) = multiprocessing.Pipe(True)
    con_s = multiprocessing.Process(target=consumer,args=((output_p,input_p),))
    con_s.start()

    output_p.close()
    print("sheng chan guan bi")

    sequence=[1,2,3,4]
    producer(sequence,input_p)

    input_p.close()
    con_s.join()
