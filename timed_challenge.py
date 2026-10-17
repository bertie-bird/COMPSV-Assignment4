# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

"""17. Service Line Simulation
Simulate a line where values are added at one end and removed from the other.
Actions: add("A"), add("B"), serve()
Output: "A"
"""
class ServiceLine_Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add(self, value):
        new_node = Node(value)

        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def serve(self):
        if not self.front:
            print("Service Line is empty.")
            return None
        
        served_node = self.front
        self.front = self.front.next
        
        if not self.front:
            self.rear = None
        print(f"{served_node.value} is being served.")
        return served_node.value

line = ServiceLine_Queue()
line.add("Amanda")
line.add("Bailey")
line.add("Cameron")

print(line.serve())
print(line.serve())
print(line.serve())
print(line.serve())  

"""
Reflection:

    What structure you chose and why
        For this time challenge question, I decided that I should
        use the queue data structure because its principle is the
        first in first out method. In this scenario, a queue will
        remove the top name on the list after they’ve been served 
        and will put an added name to the bottom of the list. This type
        of data structure is what the service line needs in order to run smoothly.
    How the time limit shaped your decision
        I thought that I wouldn't honestly have enough time during the
        question, however, I do think that I did better than I thought
        I would because I answered this question after solving the problems
        within the practice_problems.py so that really helped in getting
        me into the mind set. 
    What trade-offs or compromises you made under time pressure
        I think because I was given resources that helped explain when
        to choose certain data structures over others I don’t feel like
        many trade-offs were given when trying to figure out what to do.
        Another point I want to add as well is that I started this part
        of the assignment at a point where my mind was already in the zone
        so time pressure didn’t affect me as much compared to if I had no
        resources beforehand or practice problems.
"""