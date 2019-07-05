import os

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name, likes):
    c = Category.objects.get_or_create(name=name, likes = likes)[0]
    return c

def populate():
    python_cat = add_cat('Python', 10)
    add_page(cat=python_cat, title="Official Python Tutorial", url="http://docs.python.org/2/tutorial/")
    add_page(cat=python_cat, title="Learn Python in 10 Minutes", url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("Django", 20)
    add_page(cat=django_cat, title="Official Django Tutorial", url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
    add_page(cat=django_cat, title="Django Rocks", url="http://www.djangorocks.com/")

    frame_cat = add_cat("Other Frameworks", 30)
    add_page(cat=frame_cat, title="Bottle", url="http://bottlepy.org/docs/dev/")
    add_page(cat=frame_cat, title="Flask", url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print ("- ",str(c)," - ",str(p))

if __name__ == '__main__':
    print("Starting helloApp population script")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Helloworld.settings')
    import django
    django.setup()
    from helloApp.models import Category, Page
    populate()