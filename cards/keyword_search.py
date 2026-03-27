from __future__ import annotations
from django.db.models import Q


def apply_keyword_search(queryset, keyword: str):
    terms = keyword.split()
    q = Q()
    for term in terms:
        q |= (
            Q(title__icontains=term)      |
            Q(summary__icontains=term)     |
            Q(description__icontains=term) |
            Q(tags__icontains=term)        |
            Q(keywords__icontains=term)
        )
    return queryset.filter(q)
