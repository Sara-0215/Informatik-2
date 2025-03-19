from datetime import datetime

def calculate_co2(transportmittel, km_pro_tag):
    """
    Berechnet den jährlichen CO₂-Ausstoß basierend auf dem Transportmittel und der täglichen Strecke.
    Gibt ein Dictionary mit den Eingaben und der Berechnung zurück.
    """
    CO2_WERTE = {
        "Auto (Benzin)": 120,
        "Auto (Diesel)": 135,
        "Bus": 80,
        "Zug": 14,
        "Flugzeug": 250,
        "Fahrrad": 0,
        "Zu Fuß": 0,
        "E-Bus": 50,
        "Tram": 30
    }

    # Prüfen, ob das Transportmittel existiert
    if transportmittel not in CO2_WERTE:
        raise ValueError("Ungültiges Transportmittel!")

    # Berechnung des jährlichen CO₂-Ausstoßes (in kg)
    co2_jahr = (CO2_WERTE[transportmittel] * km_pro_tag * 365) / 1000

    # Ergebnisse in einem Dictionary speichern
    result_dict = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Transportmittel": transportmittel,
        "Kilometer pro Tag": km_pro_tag,
        "Jährlicher CO₂-Ausstoß (kg)": round(co2_jahr, 2)
    }
    
    return result_dict
