from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

from workers.models import Workers


def index(request) -> HttpResponseBadRequest | HttpResponse:
    """Main workers page"""

    if request.GET is None:
        return HttpResponseBadRequest()

    # fucking jinja doesn't want to work
    # I'm writing to her {% for i in range(5) %}
    # ERROR: could not parse the remainder
    workers = Workers.objects.all()
    context = {"posts": workers[:5], "count": len(workers)-5}

    return render(request, 'workers/index.html', context=context)

def show_worker(request, worker_id) -> HttpResponseBadRequest | HttpResponse:
    if request.GET is None:
        return HttpResponseBadRequest()

    context={"worker_id": worker_id, "worker":Workers.objects.get(pk=worker_id)}

    return render(request, 'workers/worker.html', context=context)

# def index(request: HttpRequest, hierarchy_id: int) -> HttpResponse:
#     """Index view for the workers app."""
#     if request.GET is None:
#         return HttpResponseBadRequest()

#     return HttpResponse(
#         f"<h1>Hierarchy by ID {hierarchy_id}:</h1>\n"
#         + "\n".join(
#             f"<p>{i}. Вячеслав Бебрович</p>" for i in map(str, range(hierarchy_id))
#         )
#     )  # type: ignore
