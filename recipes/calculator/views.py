from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipes_views(request, dish_name):
    number = int(request.GET.get("servings", 1))

    dishes_data = DATA
    ingredients = dishes_data[dish_name]
    
    for name, quantaty in ingredients.items():
        ingredients[name] = ingredients[name] * number

    context = {'name': ingredients}

    return render(request, 'index.html', context)
