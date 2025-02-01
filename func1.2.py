def fahrenheit_to_celsius(fahrenheit):
    celsius=(5 / 9) * (fahrenheit - 32)
    return celsius
fahrenheit=float(input("введите температуру в фарегнейтах:"))
celsius=fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} градусов фаренгейта={celsius} градусов цельсия")