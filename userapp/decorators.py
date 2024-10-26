from django.contrib.auth.decorators import user_passes_test


def admin_required(function=None, login_url='access_denied'):
    """
    Decorador para verificar si el usuario es un administrador.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.tipo_de_usuario == 'administrador',
        login_url=login_url,
        redirect_field_name=None  # Evita agregar ?next= en la URL
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
