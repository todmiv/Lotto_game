import random

def generate_card():
    card = []
    digits = list(range(1, 91))
    for i in range(3):
        row = [0] * 9
        positions = sorted(random.sample(range(9), 5))
        nums = sorted(random.sample(digits, 5))
        [digits.remove(digit) if digit in nums else None for digit in nums]
        for j in range(5): row[positions[j]] = nums[j]
        card.append(row)
    return card


def print_card(player_card, computer_card):
    print("-------- Ваша карточка -------")
    print_card_format(player_card)
    print("------------------------------")
    print("---- Карточка компьютера -----")
    print_card_format(computer_card)
    print("------------------------------")


def print_card_format(card):
    for row in card:
        for num in row:
            if num == 0:
                print("   ", end=" ")
            else:
                print(f"{num:2d}", end=" ")
        print()


def draw_number(remaining_numbers):
    number = random.choice(remaining_numbers)
    remaining_numbers.remove(number)
    return number


def check_winner(card):
    for row in card:
        if any(num != 0 for num in row):
            return False
    return True


def main():
    player_card = generate_card()
    computer_card = generate_card()

    remaining_numbers = list(range(1, 91))

    while True:
        number = draw_number(remaining_numbers)
        print(f"\nНовый бочонок: {number} (осталось {len(remaining_numbers)})")

        print_card(player_card, computer_card)

        user_choice = input("Зачеркнуть цифру? (y/n): ").lower()

        if user_choice == 'y':
            if number in [num for row in player_card for num in row]:
                for row in player_card:
                    if number in row:
                        row[row.index(number)] = 0
                        break
            elif number in [num for row in computer_card for num in row]:
                for row in computer_card:
                    if number in row:
                        row[row.index(number)] = 0
                        break
            else:
                print("Вы проиграли! Цифры нет в вашей карточке.")
                break
        elif user_choice == 'n':
            if number in [num for row in player_card for num in row]:
                print("Вы проиграли! Цифра есть в вашей карточке.")
                break
            elif number in [num for row in computer_card for num in row]:
                for row in computer_card:
                    if number in row:
                        row[row.index(number)] = 0
                        break
            else:
                continue
        else:
            print("Некорректный ввод. Введите 'y' (да) или 'n' (нет).")
            continue

        if check_winner(player_card):
            print("Вы выиграли! Вы закрыли все числа на вашей карточке.")
            break
        elif check_winner(computer_card):
            print("Вы проиграли! Компьютер закрыл все числа на своей карточке.")
            break


if __name__ == "__main__":
    main()
