class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num
            

    def valid(self):
        self.card_num = self.card_num.replace(' ', '')
        
        if not self.card_num.isnumeric() or len(self.card_num) < 2:
            return False
            
        card_num_list = [int(item) for item in reversed(self.card_num)] 

        for index in range(1, len(card_num_list), 2):
            item_double = 2 * card_num_list[index]
            if item_double > 9:
                card_num_list[index] = item_double - 9
            else:
                card_num_list[index] = item_double

        return sum(card_num_list) % 10 == 0
