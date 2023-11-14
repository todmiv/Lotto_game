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
    def __init__(self, player_types):
        self.players = []
        for i, player_type in enumerate(player_types):
            player_name = f"Player{i+1}"
            self.players.append(self.create_player(player_type, player_name))
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

    def play(self):
        while True:
            number = self.draw_number()
            print(f"\nНовый бочонок: {number} (осталось {len(self.remaining_numbers)})")
            for player in self.players:
                player.print_card()

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
                            return
                    elif user_choice == 'n':
                        if number in [num for row in player.card.rows for num in row]:
                            print("Вы проиграли! Цифра есть в вашей карточке.")
                            return
                    else:
                        print("Некорректный ввод. Введите 'y' (да) или 'n' (нет).")
                        return
                else:
                    if number in [num for row in player.card.rows for num in row]:
                        for row in player.card.rows:
                            if number in row:
                                row[row.index(number)] = 0
                                break

                if self.check_winner(player):
                    print(f"Выиграл {player.name}! Он закрыл все числа на своей карточке.")
                    return


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
    num_players = int(input("Введите количество игроков (от 2 до 6): "))
    if num_players < 2 or num_players > 6:
        print("Некорректное количество игроков.")
    else:
        player_types = []
        for i in range(num_players):
            player_type = input(f"Выберите тип игрока {i+1} (human/computer): ")
            player_types.append(player_type)
        game = Game(player_types)
        game.play()
