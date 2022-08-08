from celery import shared_task
# from django_celery_test.celery import app
from django.apps import apps


list_of_bad_words = ['arse', 'ass', 'asshole', 'bastard', 'bitch', 'bollocks', 'brotherfucker',
                     'bugger', 'bullshit', 'child-fucker', 'Christ on a bike', 'Christ on a cracker',
                     'cocksucker', 'crap', 'cunt', 'damn', 'fatherfucker', 'frigger', 'fuck', 'goddamn',
                     'godsdamn', 'holy shit', 'horseshit', 'in shit', 'Jesus Christ', 'Jesus fuck',
                     'Jesus H. Christ', 'Jesus Harold Christ', 'Jesus wept', 'Jesus, Mary and Joseph',
                     'motherfucker', 'nigga', 'nigger', 'piss', 'prick', 'shit', 'shit ass', 'sisterfucker',
                     'slut', 'son of a bitch', 'son of a whore', 'sweet Jesus', 'tit', 'twat', 'whore',
                     ]

@shared_task
def clear_books():
    Book = apps.get_model("read_book.Book")
    books = Book.objects.all()
    for book in books:
        for word in list_of_bad_words:
            if word in book.name:
                book.delete()

@shared_task
def clear_comments():
    Comment = apps.get_model("read_book.MyComments")
    comments = Comment.objects.all()
    for comment in comments:
        for word in list_of_bad_words:
            if word in comment.text:
                comment.delete()
