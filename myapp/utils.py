def calculate_emission(quantity, factor):
    return quantity * factor


def detect_suspicious(quantity):

    if quantity > 5000:
        return True

    return False