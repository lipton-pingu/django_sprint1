from django.shortcuts import render
from django.http import HttpResponseNotFound


posts = [{
    'id': 0,
    'location': 'Остров отчаянья',
    'date': '30 сентября 1659 года',
            'category': 'travel',
            'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
},
    {
    'id': 1,
    'location': 'Остров отчаянья',
    'date': '1 октября 1659 года',
            'category': 'not-my-day',
            'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
},
    {
    'id': 2,
    'location': 'Остров отчаянья',
    'date': '25 октября 1659 года',
            'category': 'not-my-day',
            'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
}
]


def index(request):
    reversed_posts = sorted(posts, key=lambda x: x['id'], reverse=True)
    return render(request, 'blog/index.html', {'posts': reversed_posts})


def post_detail(request, id):
    post = next((p for p in posts if p["id"] == id), None)
    if post:
        return render(request, 'blog/detail.html', {'post': post})
    return HttpResponseNotFound("Пост не найден")


def category_posts(request, category_slug):
    posts_in_category = [
        p for p in posts if p['category'] == category_slug]
    return render(request, 'blog/category.html', {
        'category': category_slug,
        'posts': posts_in_category
    })
