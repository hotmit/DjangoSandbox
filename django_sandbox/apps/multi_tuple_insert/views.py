from collections import defaultdict
from datetime import datetime
from random import choice, randint
from string import ascii_uppercase
from django.db import transaction, connection
from django.http import HttpResponse
from django.shortcuts import render
from os import path
from django_sandbox.apps.multi_tuple_insert.models import Book, Author


MAX_AUTHOR = 2000
BATCH_SIZE = 10000

def truncate_model(model):
    cursor = connection.cursor()
    table_name = model._meta.db_table
    sql = 'DELETE FROM %s;' % table_name
    cursor.execute(sql)

def gen_samples(request):
    start_time = datetime.now()

    # these delete cause error in sqlite (too many SQL variables)
    # Book.objects.all().delete()
    # Author.objects.all().delete()       # this is after to prevent having to cascade
    truncate_model(Book)
    truncate_model(Author)

    author_list = []
    data_file = path.join(path.dirname(__file__), 'data', 'author_lists.txt')

    with open(data_file, 'r') as fp:
        for line in fp:
            if len(line.strip()) > 0:
                index = (len(author_list) + 1)
                author_list.append(
                    Author(name=line, age=17+index, website='http://my.author.com/%d/' % index, notes='blah x%d' % index)
                )

                if len(author_list) >= MAX_AUTHOR:
                    break

    Author.objects.bulk_create(author_list, batch_size=BATCH_SIZE)


    # book_list = []
    # sample_space = ascii_uppercase + '     '
    # for i in range(1000):   # do this to mix the result so they don't line up sequentially
    #     for auth in Author.objects.all():
    #         random_title_name = ''.join(choice(sample_space) for i in range(randint(7,20)))
    #         book_list.append(
    #             Book(author_id=auth.id, title=random_title_name, published=datetime.now())
    #         )
    #
    # Book.objects.bulk_create(book_list, batch_size=BATCH_SIZE)

    end_time = datetime.now()

    duration = end_time - start_time
    return HttpResponse('Authors: %d, Books: %d, Duration: %ds' % (Author.objects.count(), Book.objects.count(), duration.total_seconds()))


def run_multi_tuple_insert(request):
    MAX_BOOK_COUNT = 500000

    Book.objects.all().delete()

    record_count = 0
    tuple_list = []

    # region [ Generate The list ]
    target_authors = list(Author.objects.all())
    sample_space = ascii_uppercase + '     '
    for auth in target_authors:
        for i in range(250):
            title = ''.join(choice(sample_space) for i in range(randint(7,20)))
            tuple_list.append(
                (auth.name, auth.age, auth.website, title)
            )
    # endregion


    start_time = datetime.now()

    book_list = []
    index_list = defaultdict(list)
    first_keys = []

    for t in tuple_list:
        first_keys.append(t[0])
        key =t[0:3]
        index_list[key].append(t)

    unique_first_keys = {}.fromkeys(first_keys).keys()
    target_authors = Author.objects.filter(name__in=unique_first_keys)

    for auth in target_authors:
        key = (auth.name, auth.age, auth.website)
        for row in index_list[key]:
            book_list.append(
                Book(author_id=auth.id, title=row[3], published=datetime.now(), summary=auth.notes)
            )

            list_count = len(book_list)
            if list_count >= BATCH_SIZE:
                Book.objects.bulk_create(book_list)
                record_count += list_count
                book_list = []

            if record_count + list_count >= MAX_BOOK_COUNT:
                break

    if book_list:
        Book.objects.bulk_create(book_list)
        record_count += len(book_list)

    end_time = datetime.now()

    duration = end_time - start_time
    return HttpResponse('Authors: %d, Books: %d, Duration: %ds' % (Author.objects.count(), Book.objects.count(), duration.total_seconds()))

