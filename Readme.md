# ShoPen app
Шо? Pen?

## Readme
English version of this readme is available [here](Readme_en.md).

## Опис
Цей застосунок призначений для використання як система під тестування (SUT) для автоматизації тестування API.  
Це простий застосунок для електронної комерції, який дозволяє користувачам створювати обліковий запис, входити в систему та купувати ручки.  
Є 2 ролі користувачів: `admin` та `customer`.  
Адміністратор може створювати, видаляти, редагувати ручки в магазині, а також керувати іншими користувачами.  
Клієнти можуть купувати ручки.  

## Особливості
- ✅ Stateful API
- ✅ Swagger документація
- ✅ Аутентифікація за допомогою сесійного токена на бекенді
- ✅ sqlite база даних, яка не потребує встановлення
- ✅ покрито юніт-тестами

## Випадки використання
- Користувачі можуть реєструватися, входити в систему та виходити з неї.
- Користувачі можуть отримувати та редагувати інформацію про себе.
- Адміністратори можуть отримувати та редагувати інформацію про будь-якого користувача.
- Адміністратор може підвищити клієнта до адміністратора.
- Адміністратор може встановити суму кредиту клієнта для покупки ручок.
- Адміністратор може додавати, видаляти та змінювати кількість ручок на складі.
- Будь-який користувач (навіть без аутентифікації) може отримати список ручок.
- Клієнт може замовити ручки для покупки.
- Клієнт може завершити операцію покупки протягом короткого періоду часу (за замовчуванням 5 хвилин).
- Клієнт може скасувати операцію покупки.
- Клієнт може запросити повернення коштів протягом короткого періоду часу (за замовчуванням 20 хвилин).
- У разі, якщо клієнт замовляє ручки на велику суму грошей (за замовчуванням 5000), він отримує оптову знижку (за замовчуванням 10%).
- Адміністратор може отримати знижку 20% за замовчуванням на будь-які покупки.
- Є сервісний API для скидання налаштувань до заводських: створюється лише 1 користувач та кілька стандартних ручок.

## Запуск локально
1. Клонувати репозиторій
2. `pip install -r requirements.txt`
3. `python -m local`