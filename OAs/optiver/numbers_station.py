import heapq
class Printer:
    def on_message_complete(self, message):
        print(message)


class Decoder:
    def __init__(self, printer):
        self.printer = printer
        self.seq = []
        self.hypens = []
        self.minHeap = []

    def process_sample(self, sequence, character):
        self.seq.append(sequence)
        heapq.heappush(self.minHeap, (sequence, character))
        if character == '-' and len(self.seq) >0 and self.seq[-1] != '1':
            res = ''
            ids = ''
            if (self.minHeap[-1][0] - (self.hypens[-1] if self.hypens else -1) == self.minHeap[-2][0]):
                while self.minHeap:
                    popped = heapq.heappop(self.minHeap)
                    res += popped[1] 
                    ids += popped[0]
                temp = res.split['-'][-1]
                self.printer.on_message_complete(temp)
                               
        if character == '-':
            self.hypens.append(sequence)
                            
if __name__ == "__main__":
    import sys

    read_line = lambda: sys.stdin.readline().split()

    printer = Printer()
    decoder = Decoder(printer)

    while True:
        line = read_line()
        if len(line) == 0:
            break
        decoder.process_sample(int(line[0]), line[1])
        