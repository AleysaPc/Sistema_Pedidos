from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):

    model = User

    # Campos que se muestran en la tabla
    list_display = (
        'id',
        'username',
        'email',
        'rol',
        'is_staff',
        'is_active',
    )

    # Campos editables al entrar al usuario
    fieldsets = UserAdmin.fieldsets + (
        (
            'Información adicional',
            {
                'fields': (
                    'telefono',
                    'direccion',
                    'ci',
                    'rol',
                )
            },
        ),
    )

    # Campos al crear usuario
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Información adicional',
            {
                'fields': (
                    'email',
                    'telefono',
                    'direccion',
                    'ci',
                    'rol',
                )
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)