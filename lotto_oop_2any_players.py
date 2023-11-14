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
        print("------------------------------")
        self.print_card_format()
        print("------------------------------")

    def print_card_format(self):
        for row in self.rows:
            for num in row:
                if num == 0:
                    print("  ", end=" ")
                else:
                    print(f"{num:2d}", end=" ")
            print()


class Player:
    def __init__(self, name):
        self.name = name
        self.card = Card()

    def print_card(self):
        print(f"---- Карточка {self.name} ----")
        self.card.print_card()


class Game:
    def __init__(self, player1_type, player2_type):
        self.player1 = self.create_player(player1_type, "Player1")
        self.player2 = self.create_player(player2_type, "Player2")
        self.remaining_numbers = list(range(1, 91))

    def create_player(self, player_type, name):
        if player_type == "human":
            return HumanPlayer(name)
        elif player_type == "computer":
            return ComputerPlayer(name)

    def draw_number(self):
        number = random.choice(self.remaining_numbers)
        self.remaining_numbers.remove(number)
        return number

    def check_winner(self, player):
        for row in player.card.rows:
            if any(num != 0 for num in row):
                return False
        return True

    def handle_choice(self, player, number):
        if isinstance(player, HumanPlayer):
            user_choice = input("Зачеркнуть цифру? (y/n): ").lower()
            if user_choice == 'y':
                if number in [num for row in player.card.rows for num in row]:
                    for row in player.card.rows:
                        if number in row:
                            row[row.index(number)] = 0
                            break
                else:
                    print("Вы проиграли! Цифры нет в вашей карточке.")
                    return False
            elif user_choice == 'n':
                if number in [num for row in player.card.rows for num in row]:
                    print("Вы проиграли! Цифра есть в вашей карточке.")
                    return False
            else:
                print("Некорректный ввод. Введите 'y' (да) или 'n' (нет).")
                return False
        else:
            if number in [num for row in player.card.rows for num in row]:
                for row in player.card.rows:
                    if number in row:
                        row[row.index(number)] = 0
                        break
        return True

    def play(self):
        while True:
            number = self.draw_number()
            print(f"\nНовый бочонок: {number} (осталось {len(self.remaining_numbers)})")
            self.player1.print_card()
            self.player2.print_card()

            if not self.handle_choice(self.player1, number):
                break

            if not self.handle_choice(self.player2, number):
                break

            if self.check_winner(self.player1):
                print("Выиграл Player1! Он закрыл все числа на своей карточке.")
                break
            elif self.check_winner(self.player2):
                print("Выиграл Player2! Он закрыл все числа на своей карточке.")
                break


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_choice(self, number):
        if number in [num for row in self.card.rows for num in row]:
            for row in self.card.rows:
                if number in row:
                    row[row.index(number)] = 0
                    break


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_choice(self, number):
        user_choice = input("Зачеркнуть цифру? (y/n): ").lower()
        if user_choice == 'y':
            if number in [num for row in self.card.rows for num in row]:
                for row in self.card.rows:
                    if number in row:
                        row[row.index(number)] = 0
                        break
            else:
                print("Вы проиграли! Цифры нет в вашей карточке.")
                return False
        elif user_choice == 'n':
            if number in [num for row in self.card.rows for num in row]:
                print("Вы проиграли! Цифра есть в вашей карточке.")
                return False
        else:
            print("Некорректный ввод. Введите 'y' (да) или 'n' (нет).")
            return False
        return True


if __name__ == "__main__":
    player1_type = input("Выберите тип первого игрока (human/computer): ")
    player2_type = input("Выберите тип второго игрока (human/computer): ")
    game = Game(player1_type, player2_type)
    game.play()

