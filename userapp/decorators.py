from django.contrib.auth.decorators import user_passes_test

def admin_required(function=None, login_url='login'):
    """
    Decorador para verificar si el usuario es un administrador.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.tipo_de_usuario == 'administrador',
        login_url=login_url
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
