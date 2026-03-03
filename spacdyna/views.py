from django.shortcuts import render


def home(request):
    my_name = "Haaris Saifi"
    my_address = "Gangoh, Saharanpur"
    my_age = 55

    # ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    students_names = ["Sushant", "Anam", "Rajan", "Fiza",
                      "Arshi", "Anuj", "Anindita", "Mayank", "Akanksha"]

    context = {
        'name': my_name,
        'address': my_address,
        'age': my_age,
        'list': students_names
    }
    return render(request, 'index.html', context)


def about(request):
    # 1 to 500 - all perfect numbers 
    
    perfect_numbers = []
    for i in range(1, 500):
        sum_of_divisors = 0
        for x in range(1, i - 1):
            if i % x == 0:
                sum_of_divisors += x 

        if sum_of_divisors == i:
            perfect_numbers.append(i)
    
    return render(request, 'about.html', {'num': perfect_numbers, } )


# context => Essentially is a dictionary that contains the key-value pairs of all the data that you want to show on the HTML page.

# Database: 