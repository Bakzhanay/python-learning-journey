from weather_logic import get_weather, get_coordinates, get_weather_description

def main():
    print("Прогноз погоды")

    while True:
        city = input("Введите название города (например, Астана ('q'- выход)): ").strip()
        if city == "q":
            break

        try:
            lat, lon  = get_coordinates(city)
            weather = get_weather(lat, lon)

            temp = weather.get("temperature")
            winspeed = weather.get("windspeed")
            w_code = get_weather_description(weather.get("weathercode"))

            print(f"\nПогода в городе {city}:")
            print(f"\nТекущая температура: {temp}C")
            print(f"Скорость ветра: {winspeed} км/ч")
            print(f"Код погоды: {w_code}")

        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")
        except ConnectionError as e:
            print(f"Ошибка сети: {e}")
        except Exception as e: 
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()