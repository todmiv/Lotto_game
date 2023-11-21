import random


class Card:
    def __init__(self, digits):
        self.rows = []
        self.digits = digits
        for _ in range(3):
            row = [0] * 9
            positions = sorted(random.sample(range(9), 5))
            nums = sorted(random.sample(self.digits, 5))
            self.digits = [digit for digit in self.digits if digit not in nums]
            for j in range(5):
                row[positions[j]] = nums[j]
            self.rows.append(row)

    def __str__(self):
        card_str = "--------------------------\n"
        for row in self.rows:
            for num in row:
                if num == 0:
                    card_str += "-  "
                else:
                    card_str += f"{num:2d} "
            card_str += "\n"
        card_str += "--------------------------"
        return card_str

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rows == other.rows
        return False


class Game:
    def __init__(self):
        digits = list(range(1, 91))
        self.player_card = Card(digits)
        self.computer_card = Card(digits)
        self.remaining_numbers = digits

    def __str__(self):
        return f"Player's Card:\n{self.player_card}\nComputer's Card:\n{self.computer_card}"

    def __eq__(self, other):
        if isinstance(other, Game):
            return self.player_card == other.player_card and self.computer_card == other.computer_card
        return False

    def draw_number(self):
        number = random.choice(self.remaining_numbers)
        self.remaining_numbers.remove(number)
        return number

    def check_winner(self, card):
        return all(num == 0 for row in card.rows for num in row)

    def play(self):
        while True:
            number = self.draw_number()
            print(f"\nНовый бочонок: {number} (осталось {len(self.remaining_numbers)})")
            print("------ Ваша карточка -----")
            print(self.player_card)
            print("--- Карточка компьютера --")
            print(self.computer_card)

            user_choice = input("Зачеркнуть цифру? (y/n): ").lower()

            if user_choice == 'y':
                if number in [num for row in self.player_card.rows for num in row]:
                    for row in self.player_card.rows:
                        if number in row:
                            row[row.index(number)] = 0
                            if number in [num for r in self.computer_card.rows for num in r]:
                                for r in self.computer_card.rows:
                                    if number in r:
                                        r[r.index(number)] = 0
                            break
                elif number in [num for row in self.computer_card.rows for num in row]:
                    for row in self.computer_card.rows:
                        if number in row:
                            row[row.index(number)] = 0
                            break
                else:
                    print("Вы проиграли! Цифры нет в вашей карточке.")
                    break
            elif user_choice == 'n':
                if number in [num for row in self.player_card.rows for num in row]:
                    print("Вы проиграли! Цифра есть в вашей карточке.")
                    break
                elif number in [num for row in self.computer_card.rows for num in row]:
                    for row in self.computer_card.rows:
                        if number in row:
                            row[row.index(number)] = 0
                            break
                else:
                    continue
            else:
                print("Некорректный ввод. Введите 'y' (да) или 'n' (нет).")
                continue

            if self.check_winner(self.player_card):
                print("Вы выиграли! Вы закрыли все числа на вашей карточке.")
                break
            elif self.check_winner(self.computer_card):
                print("Вы проиграли! Компьютер закрыл все числа на своей карточке.")
                break


if __name__ == "__main__":
    game = Game()
    game.play()
