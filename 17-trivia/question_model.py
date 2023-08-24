class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer


new_q = Question("1+3=5",False)

print(new_q.text)
print(new_q.answer)
