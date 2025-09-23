def load_nav_obj(request):
    nav_obj = NavigationObject.objects.all()
    return {'nav_obj': nav_obj}
