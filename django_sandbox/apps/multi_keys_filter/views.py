from django.db.models import Value, TextField
from django.db.models.functions import Concat
from django.http import HttpResponse
from django_sandbox.apps.multi_keys_filter.models import MultiKey


def search(request):
    # Ref: http://stackoverflow.com/questions/38025530/how-to-filter-multiple-fields-with-list-of-objects

    MultiKey.objects.all().delete()

    MultiKey.objects.bulk_create([
        MultiKey(actor_type_id=1, actor_id=100),
        MultiKey(actor_type_id=1, actor_id=101),
        MultiKey(actor_type_id=2, actor_id=102),
        MultiKey(actor_type_id=2, actor_id=103),
    ])

    following_actor = [
        # actor_type, actor
        (1, 100),
        (2, 102),
    ]
    searchable_keys = [str(at) + "__" + str(actor) for at, actor in following_actor]

    result = MultiKey.objects.annotate(key=Concat('actor_type', Value('__'), 'actor_id',
                                                  output_field=TextField()))\
        .filter(key__in=searchable_keys)

    print(list(result))

    return HttpResponse("Done")