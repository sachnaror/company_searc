from django.shortcuts import get_object_or_404, render
from elasticsearch_dsl import Search

from .documents import CompanyDocument


def homepage(request):
    query = request.GET.get('q', '')
    if query:
        search = Search(index='companies').query('match', RegisteredName=query)
        search = search[0:10]  # Limit to top 10 results
        results = search.execute()
        companies = [hit.to_dict() for hit in results]
    else:
        companies = []
    return render(request, 'homepage.html', {'companies': companies})

def detailpage(request, company_id):
    search = Search(index='companies').query('match', ID=company_id)
    result = search.execute()
    company = result[0].to_dict() if result else None
    return render(request, 'detailpage.html', {'company': company})
