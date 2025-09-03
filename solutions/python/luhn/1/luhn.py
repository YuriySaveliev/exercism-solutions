class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num
            

    def valid(self):
        self.card_num = self.card_num.replace(' ', '')
        if not self.card_num.isnumeric():
            return False
        card_num_list = [int(item) for item in self.card_num]
        index = -2
        if len(card_num_list) < 2:
            return False
        while index * (-1) <= len(card_num_list):
            if card_num_list[index] * 2 > 9:
                card_num_list[index] = card_num_list[index] * 2 - 9
            else:
                card_num_list[index] = card_num_list[index] * 2
            index = index - 2

        return sum(card_num_list) % 10 == 0
