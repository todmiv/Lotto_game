# Lotto_game

Игра Лото на Python с различными реализациями: функциональной и объектно-ориентированной.

## Версии игры

### lotto_function_2_players.py
Функциональная версия для 2 игроков (человек и компьютер).

### lotto_oop_2_players.py
ООП версия для 2 игроков (человек и компьютер) с классами Card и Game.

### lotto_oop_2any_players.py
ООП версия для 2 игроков любого типа (human/computer), использует наследование.

### lotto_oop_any_num_players.py
ООП версия для любого числа игроков (от 2 до 6), гибкая настройка типов игроков.

## Правила игры

- Каждый игрок получает карточку 3x9 с уникальными числами от 1 до 90.
- В каждой строке 5 чисел, остальные - пустые клетки.
- Вытягиваются случайные числа (бочонки).
- Игроки зачеркивают числа на своих карточках, если они есть.
- Побеждает тот, кто первым зачеркнет все числа на своей карточке.

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/todmiv/Lotto_game.git
   cd Lotto_game
   ```

2. Установите зависимости (если есть):
   ```
   pip install -r requirements.txt
   ```

## Запуск

Выберите нужную версию и запустите:
```
python lotto_function_2_players.py
python lotto_oop_2_players.py
python lotto_oop_2any_players.py
python lotto_oop_any_num_players.py
```

## Требования

- Python 3.6+

## Лицензия

MIT License - см. файл LICENSE.

## Автор

[todmiv](https://github.com/todmiv)
