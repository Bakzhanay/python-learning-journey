from weather_logic_practice import get_weather, get_coordinates, get_weather_description

def main():
    print("Прогноз погоды")

    while True:
        city = input("Введите название города ('q' если хотите выйти.): ").strip()
        if city == 'q':
            break

        try:
            lat, lon = get_coordinates(city)
            weather = get_weather(lat, lon)

            temp = weather.get("temperature")
            windspeed = weather.get("windspeed")
            w_code = get_weather_description(weather.get("weathercode"))

            print(f"\nПрогноз погоды в городе: '{city}'.")
            print(f"Температура: '{temp}'C.")
            print(f"Ветренность: '{windspeed}'.")
            print(f"Осадки: '{w_code}'.")

        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except ConnectionError as e:
            print(f"Ошибка сети: {e}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()