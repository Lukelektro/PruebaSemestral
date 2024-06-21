from django import template

register = template.Library()

@register.filter
def comma_to_dot(value):
    # Asegurarse de que el valor es un flotante o decimal para formatearlo correctamente
    try:
        # Convertir el valor a flotante
        value = float(value)
        # Formatear el número con puntos como separadores decimales
        formatted_value = f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return formatted_value
    except ValueError:
        # En caso de error, retornar el valor original
        return value