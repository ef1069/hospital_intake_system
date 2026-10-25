class Patient:
    '''
        A class to represent a node in the MinHeap.
        Attributes:
            name (str): the name of the patient
            urgency (int): urgency of the patient's needs 1-10 (1 being the highest priority)
        '''
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

class MinHeap:
    '''
    A class to represent a MinHeap for managing patient intake
    Attributes:
        self.name (str): the name of the patient
        self.urgency (int): urgency of the patient's needs 1-10 (1 being the highest priority)
    Methods:
        print_heap(): Prints the current heap with name and urgency of each patient
        heapify_up(): Resorts the list when a new patient is added
        insert(): Inserts a new patient
        heapify_down(): Removes the most urgent patient and resorts the list
        remove_min(): Starts the recursive process of heapify_down()
        peek(): Allows user to see the next patient in the list without removing the patient
    '''
    def __init__(self):
        self.data = []

    def print_heap(self):
        print("\nCurrent Patients")
        for patient in self.data:
            print(f"-{patient.name} (Urgency: {patient.urgency})")

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            current_patient = self.data[index]
            parent_patient = self.data [parent_index]

            if current_patient.urgency < parent_patient.urgency:
                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp
                index = parent_index

            else:
                break

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left

        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            temp = self.data[index]
            self.data[index] = self.data[smallest]
            self.data[smallest] = temp

            self.heapify_down(smallest)

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        min_value = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_value 

    def peek(self):
        if self.data != None:

            return self.data[0]


# Test your MinHeap class here including edge cases
def main():
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.insert(Patient("Jacob", 3))
    heap.print_heap()

    next_up = heap.peek()
    print(next_up.name, next_up.urgency)

    served = heap.remove_min()
    print(served.name)
    heap.print_heap()

    heap.insert(Patient("David", 2))
    next_up = heap.peek()
    print(next_up.name, next_up.urgency)


main()