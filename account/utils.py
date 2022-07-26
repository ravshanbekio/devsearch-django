from django.db.models import Q
from account.models import Account

def searchDevelopers(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    get_developers = Account.objects.distinct().filter(
        Q(full_name__icontains=search_query) |
        Q(username__icontains=search_query) |
        Q(email__icontains=search_query) |
        Q(direction__icontains=search_query)
    )

    return get_developers, search_query
    