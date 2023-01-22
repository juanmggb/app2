from django.shortcuts import render
from django.http import Http404
from datetime import date


my_posts = [
    {
        "title": "First Post",
        "author": "John G",
        "date": date(2019, 7, 21),
        "image": "coding.jpg",
        "excerpt": "dgfgnfhdghdghdhddfd",
        "content": """
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
            Laborum accusamus explicabo quaerat nobis commodi, necessi
            tatibus et reprehenderit officiis. Nemo provident voluptat
            um illo obcaecati aliquam laboriosam ipsum expedita tempor
            e asperiores praesentium ea pariatur deserunt deleniti n
            am suscipit nesciunt optio eveniet dolorem, recusandae n
            obis illum, odit alias. Veniam neque labore dicta ipsum?
        """,
        "slug": "first-post"    
    },{
        "title": "Second Post",
        "author": "Luis P",
        "date": date(2020, 7, 21),
        "image": "mountains.jpg",
        "excerpt": "dgfgnfhdghdghdhddfd",
        "content": """
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
            Laborum accusamus explicabo quaerat nobis commodi, necessi
            tatibus et reprehenderit officiis. Nemo provident voluptat
            um illo obcaecati aliquam laboriosam ipsum expedita tempor
            e asperiores praesentium ea pariatur deserunt deleniti n
            am suscipit nesciunt optio eveniet dolorem, recusandae n
            obis illum, odit alias. Veniam neque labore dicta ipsum?
        """,
        "slug": "second-post"    
    },{
        "title": "Third Post",
        "author": "Gabriel R",
        "date": date(2021, 7, 21),
        "image": "woods.jpg",
        "excerpt": "dgfgnfhdghdghdhddfd",
        "content": """
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
            Laborum accusamus explicabo quaerat nobis commodi, necessi
            tatibus et reprehenderit officiis. Nemo provident voluptat
            um illo obcaecati aliquam laboriosam ipsum expedita tempor
            e asperiores praesentium ea pariatur deserunt deleniti n
            am suscipit nesciunt optio eveniet dolorem, recusandae n
            obis illum, odit alias. Veniam neque labore dicta ipsum?
        """,
        "slug": "third-post"    
    }
]

# Create your views here.
def index(request):
    sorted_post = sorted(my_posts,
                        key=lambda post: post["date"], 
                        reverse=True)
    
    return render(request, "blog/index.html", {
        "posts":sorted_post[:3]
    })


def posts(request):
    
    return render(request, "blog/posts.html", {
        "posts": my_posts
    })


def post(request, slug):

    try: 
        selected_post = next(post for post in my_posts if post["slug"] == slug)

        return render(request, "blog/post.html", {
            "post": selected_post 
        })
        
    except:

        raise Http404()

    