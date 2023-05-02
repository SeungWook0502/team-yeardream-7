# Input user number


class InputNumber:
    def __init__(self):
        self.number = None

    def get_input(self):
        while True:
            self.number = input("Enter a 4-digit number: ")
            if len(self.number) != 4:
                print("Invalid input! Please enter a 4-digit number.")
                continue
            break
        return self.number


print("hi")

