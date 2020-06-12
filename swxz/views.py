from django.shortcuts import render
# 404
def page_not_found(request, exception):
    return render(request, 'front/404.html')

# 500
def page_error(request):
    return render(request, 'front/500.html')