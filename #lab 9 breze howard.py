#lab 9 breze howard

#program 1
#define the Queue class
class Queue():
    def __init__(self):
        self.queue = [] #initialize an empty list to store queue items

    #add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    #remove and return the item from the queue if it's not empty
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        return None  #if the queue is empty, return None

    #return True if the stack is empty, otherwise False
    def is_empty(self):
        return len(self.queue) == 0
    
#function to check if the parenthesis are balanced
def is_balanced(expression):
    q = Queue() #creates instance of the queue class to manage parenthesis

    #a dictionary matching opening and closing parenthesis
    matching_pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    #loop through each character in the expression
    for char in expression:
        if char in matching_pairs: #if character is an open parenthesis
            q.enqueue(char) #enqueue it into the queue
        elif char in matching_pairs.values(): #if character is a closed parenthesis
            if q.is_empty(): #checks if the queue is empty if it is then the opening parenthsis doesn't match the closing parenthesis
                return False  #queue is unbalanced so return False
            
            #dequeues an opening parenthesis and checks if it matches a closing parenthesis
            open_parenthsis = q.dequeue()

            #if the open parenthesis doesn't match the closed one it's unbalanced
            if matching_pairs.get(open_parenthsis) != char:
                return False #mismatched parentheses returns false 
            
    #if queue is empty, all parentheses were matched
    return q.is_empty()

#test cases
test_expressions = [
    "()", #balanced
    "{[()()]}", #balanced 
    "({[})", #unbalanced missing ']'
    "((())", #unbalanced missing ')'
    "[{()}]", #balanced
    "(([[{}}]))", #unbalanced missing ']'
]

#loop through each test expression and check if it's balanced
for expr in test_expressions:
    print(f"expression: {expr} -> balanced: {is_balanced(expr)}")

#program 2
#define the Queue class
class Queue():
    def __init__(self):
        self.queue = [] #initialize an empty list to store queue items

    #add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    #remove and return the item from the queue if it's not empty
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        return None  #if the queue is empty, return None

    #return True if the stack is empty, otherwise False
    def is_empty(self):
        return len(self.queue) == 0

def simulate_print_queue(jobs):
    print_queue = Queue() #creates new queue instance

    #enque all print jobs
    for job in jobs:
        print_queue.enqueue(job)
        print(f"job '{job}' added to the print queue")

    #process the jobs in the order they were written
    while not print_queue.is_empty():
        #dequeue the next job and simulate processing
        job = print_queue.dequeue()
        print(f"processing job: {job}")

#list of print jobs to test
jobs = ["Document1.pdf", "Image2.png", "Report3.docx", "Presentation4.pptx", "Resume5.pdf"]

#simulate the print queue processing
simulate_print_queue(jobs)