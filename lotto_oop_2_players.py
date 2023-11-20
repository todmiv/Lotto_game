import random

class Card:
    def __init__(self):
        self.rows = []
        self.digits = list(range(1, 91))
        for _ in range(3):
            row = [0] * 9
            positions = sorted(random.sample(range(9), 5))
            nums = sorted(random.sample(self.digits, 5))
            [self.digits.remove(digit) if digit in nums else None for digit in nums]
            for j in range(5):
                row[positions[j]] = nums[j]
            self.rows.append(row)


    def print_card(self):
        print("--------------------------")
        self.print_card_format()
        print("--------------------------")

    def print_card_format(self):
        for row in self.rows:
            for num in row:
                if num == 0:
                    print("- ", end=" ")
                else:
                    print(f"{num:2d}", end=" ")
            print()


class Game:
    def __init__(self):
        self.player_card = Card()
        self.computer_card = Card()
        self.remaining_numbers = list(range(1, 91))

    def draw_number(self):
        number = random.choice(self.remaining_numbers)
        self.remaining_numbers.remove(number)
        return number

    def check_winner(self, card):
        for row in card.rows:
            if any(num != 0 for num in row):
                return False
        return True

    def play(self):
        while True:
            number = self.draw_number()
            print(f"\nНовый бочонок: {number} (осталось {len(self.remaining_numbers)})")
            print("------ Ваша карточка -----")
            self.player_card.print_card()
            print("--- Карточка компьютера --")
            self.computer_card.print_card()

            user_choice = input("Зачеркнуть цифру? (y/n): ").lower()

            if user_choice == 'y':
                if number in [num for row in self.player_card.rows for num in row]:
                    for row in self.player_card.rows:
                        if number in row:
                            row[row.index(number)] = 0
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
