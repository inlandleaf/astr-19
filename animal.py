class Animal:
    def __init__(self, arm_len, leg_len, num_eyes, tail, furry):
        self.arm_len = arm_len
        self.leg_len = leg_len
        self.num_eyes = num_eyes
        self.tail = tail
        self.furry = furry

    def describe(self):
        print(f"Physical Characteristics of My Favorite Animal:")
        print(f"Arm Length: {self.arm_len} units")
        print(f"Leg Length: {self.leg_len} units")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has a Tail: {'Yes' if self.tail else 'No'}")
        print(f"Is it Furry: {'Yes' if self.furry else 'No'}")

lion = Animal(1.2, 1.8, 2, True, True) # Creating instance of Animal class for a lion
lion.describe() # Calling describe function
