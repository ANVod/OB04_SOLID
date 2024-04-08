# Простая Игра: Борьба с Монстрами

## Описание
Этот проект представляет собой простую игровую консольную программу, демонстрирующую концепции объектно-ориентированного программирования и применение одного из SOLID принципов - принципа открытости/закрытости. В игре игрок управляет бойцом, который может использовать различные типы оружия для борьбы с виртуальными монстрами.

## Ключевые Особенности

- **Поддержка Расширения:** Новые типы оружия могут быть легко добавлены в игру без изменения существующего кода бойцов или механизма боя, что соответствует принципу открытости/закрытости.
- **Изменение Оружия на Лету:** Игрок может изменять оружие бойца во время игры, выбирая наиболее подходящий инструмент для борьбы с монстрами.

## Технологии

Проект написан на языке программирования Python, используя принципы объектно-ориентированного проектирования.

## Структура Проекта

- `Weapon`: Абстрактный класс для оружия, определяющий общий интерфейс `attack`.
- `Sword` и `Bow`: Конкретные реализации оружия, наследуемые от `Weapon`.
- `Fighter`: Класс бойца, который может использовать различное оружие для атаки на монстров.
- `demonstrate_battle`: Функция для демонстрации боя между бойцом и монстром.

## Как Играть

1. **Создайте экземпляр бойца** с выбранным оружием.
2. **Используйте метод `attack`** бойца для имитации удара по монстру.
3. **Используйте метод `changeWeapon`**, чтобы сменить оружие бойца и адаптироваться к различным ситуациям боя.
4. **Наблюдайте за результатами боя** в консоли.

## Запуск Проекта

Для запуска проекта у вас должен быть установлен Python. Скопируйте исходный код в файл `.py` и выполните его в вашем любимом среде разработки или напрямую в командной строке Python.

## Вклад в Проект

Этот проект открыт для вашего вклада! Если у вас есть идеи по новому оружию или улучшениям, не стесняйтесь делиться ими через pull-запросы.

## Лицензия

Проект распространяется под лицензией MIT. Ознакомьтесь с файлом `LICENSE` для дополнительной информации.