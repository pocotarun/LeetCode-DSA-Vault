class FirstStack:
    def __init__(self):
        self.listt = []

    def find_length(self):
        return len(self.listt)

    def add_element_in_stack(self, value):
        self.listt.insert(0, value)

    def watch_top_element(self):
        if not self.listt:  # चेक कर रहा है कि क्या लिस्ट खाली है
            print("Stack is empty")
        else:
            print(len(self.listt), self.listt[0])      

    def dell(self):
        if not self.listt:  # चेक कर रहा है कि क्या लिस्ट खाली है
            return "Stack is empty"
        else:
            return self.listt.pop(0)  # टॉप एलिमेंट को हटाएगा और रिटर्न करेगा

# ============= टेस्टिंग ============
stack = FirstStack()
print(stack.dell())  # आउटपुट: Stack is empty

stack.add_element_in_stack("Book A")
stack.add_element_in_stack("Book B")

stack.watch_top_element()  # आउटपुट: 2 Book B
print(stack.dell())        # आउटपुट: Book B
stack.watch_top_element()  # आउटपुट: 1 Book A