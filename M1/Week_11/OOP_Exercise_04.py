class Head():
    def __init__(self):
        pass


class Torso():
    def __init__(self, head, right_arm, left_arm, left_leg, right_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


class Arm():
    def __init__(self, hand):
        self.hand


class Hand():
    def __init__(self):
        pass


class Leg():
    def __init__(self, feet):
        self.feet


class Feet():
    def __init__(self):
        pass


class Human():
    def __init__(self, head, torso, left_arm, right_arm, left_hand, right_hand, left_leg, right_leg, left_foot, right_foot):
        self.head = head
        self.torso = torso
        self.left_arm = left_arm
        self.left_hand = left_hand
        self.right_arm = right_arm
        self.right_hand = right_hand
        self.left_leg = left_leg
        self.left_foot = left_foot
        self.right_leg = right_leg
        self.right_foot = right_foot

right_hand = Hand()
left_hand = Hand()
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
right_foot = Feet()
left_foot = Feet()
left_leg = Leg(left_foot)
right_leg = Leg(right_foot)
head = Head()
torso = Torso(head, right_arm, left_arm, left_leg, right_leg)
human = Human(head, torso, left_arm, right_arm, left_hand, right_hand, left_leg, right_leg, left_foot, right_foot)