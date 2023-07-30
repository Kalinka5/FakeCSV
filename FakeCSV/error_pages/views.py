from django.shortcuts import render


def handler404(request, exception):
    return render(request, "errors/error404.html", {})


def handler500(request):
    return render(request, "errors/error500.html", {})


def handler403(request, exception):
    return render(request, "errors/error403.html", {})


def handler400(request, exception):
    return render(request, "errors/error400.html", {})
