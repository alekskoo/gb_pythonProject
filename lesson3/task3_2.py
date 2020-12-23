def my_func(name, surname, year, city, email, phone):
    return f"{name} {surname} year:{year} city:{city} email:{email} phone:{phone}"


print(my_func(name="Ivan", surname="Petrov", year="1991", city="Moscow",
              email="test@gmail.com", phone="+79990002112"))
