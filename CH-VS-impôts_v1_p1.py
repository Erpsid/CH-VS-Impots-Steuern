from decimal import Decimal
import math

# FR: Calcul d'impôts partie 1: impôts cantonal et communal pour les personnes physiques pour une taux d'indexation donnée (variable tauxIndexation).
# DE: Steuerberechnung Teil 1: Kantons- und Gemeindesteuern für natürliche Personen  für einen gegebenen Indexierungssatz (Variable tauxIndexation).
# Sources/Quellen: https://www.vs.ch/web/scc/baremes-canton-communes#c177630770, https://www.vs.ch/web/scc/baremes-canton-communes#c177630771

# FR: Calculer le taux d'imposition cantonal à partir d'un revenu indexé.
# DE: Den kantonalen Steuersatz anhand eines indexierten Einkommens berechnen.
def calculTauxCt(montantTemp1):
    if montantTemp1 <= 5000:
        return (2)
    elif montantTemp1 <= 10000:
        return (2 + (montantTemp1 - 5000) / 100 * 0.016)
    elif montantTemp1 <= 20000:
        return (2.8 + (montantTemp1 - 10000) / 100 * 0.018)        
    elif montantTemp1 <= 30000:
        return (4.6 + (montantTemp1 - 20000) / 100 * 0.017)        
    elif montantTemp1 <= 40000:
        return (6.3 + (montantTemp1 - 30000) / 100 * 0.014)        
    elif montantTemp1 <= 50000:
        return (7.7 + (montantTemp1 - 40000) / 100 * 0.013)        
    elif montantTemp1 <= 60000:
        return (9 + (montantTemp1 - 50000) / 100 * 0.015)        
    elif montantTemp1 <= 70000:
        return (10.5 + (montantTemp1 - 60000) / 100 * 0.013)        
    elif montantTemp1 <= 80000:
        return (11.8 + (montantTemp1 - 70000) / 100 * 0.012)        
    elif montantTemp1 <= 90000:
        return (13 + (montantTemp1 - 80000) / 100 * 0.003)        
    elif montantTemp1 <= 100000:
        return (13.3 + (montantTemp1 - 90000) / 100 * 0.002)
    elif montantTemp1 <= 200000:
        return (13.5 + (montantTemp1 - 100000) / 100 * 0.0005)        
    else:
        return (14)

# FR: Calculer le taux d'imposition communal à partir d'un revenu indexé.
# DE: Den Gemeindesteuersatz anhand eines indexierten Einkommens berechnen.
def calculTauxCo(montantTemp2):
    if montantTemp2 <= 5000:
        return (2)
    elif montantTemp2 <= 10000:
        return (2 + (montantTemp2 - 5000) / 100 * 0.014)
    elif montantTemp2 <= 20000:
        return (2.7 + (montantTemp2 - 10000) / 100 * 0.018)        
    elif montantTemp2 <= 30000:
        return (3.6 + (montantTemp2 - 20000) / 100 * 0.016)        
    elif montantTemp2 <= 40000:
        return (4.4 + (montantTemp2 - 30000) / 100 * 0.014)        
    elif montantTemp2 <= 50000:
        return (5.8 + (montantTemp2 - 40000) / 100 * 0.010)        
    elif montantTemp2 <= 60000:
        return (6.8 + (montantTemp2 - 50000) / 100 * 0.007)        
    elif montantTemp2 <= 70000:
        return (7.5 + (montantTemp2 - 60000) / 100 * 0.005)        
    elif montantTemp2 <= 80000:
        return (8 + (montantTemp2 - 70000) / 100 * 0.004)        
    elif montantTemp2 <= 90000:
        return (8.8 + (montantTemp2 - 80000) / 100 * 0.002)        
    elif montantTemp2 <= 180000:
        return (9 + (montantTemp2 - 90000) / 100 * 0.001)
    elif montantTemp2 <= 200000:
        return (9.9 + (montantTemp2 - 180000) / 100 * 0.0005)        
    else:
        return (10)

# FR: Calculer la valeur indexée d'un revenu. Attention, il faut appeler cette fonction plusieurs fois.
# DE: Den indexierten Wert eines Einkommens berechnen. Achtung, diese Funktion muss mehrmals aufgerufen werden.
def revenuDeterminantLeTaux(montantTemp3, diviseur):
    return round(montantTemp3 / diviseur, 0)

for montantRevenuBrut in range(0, 400000, 100):
    # FR: Attention, changer pour l'indexation souhaitée.
    # DE: Achtung, auf die gewünschte Indexierung wechseln.
    tauxIndexation = 164 #
    montantRevenuIndexeCt = montantRevenuBrut
    montantRevenuIndexeCo = montantRevenuBrut    
    nbBoucles10pc = math.floor((tauxIndexation - 100)/10)
    boucleResidu = 1 + (tauxIndexation % 10)/100
    compteur = 0
    # FR: Réduire le revenu par étapes pour atteindre le revenu indexé selon le taux d'indexation tauxIndexation pour l'impôt cantonal.
    # DE: Das Einkommen schrittweise reduzieren, um das indexierte Einkommen gemäss dem Indexierungssatz tauxIndexation für die Kantonssteuer zu erreichen.
    while compteur < nbBoucles10pc:
        montantRevenuIndexeCt = revenuDeterminantLeTaux(montantRevenuIndexeCt, 1.10)
        compteur += 1
    montantRevenuIndexeCt = revenuDeterminantLeTaux(montantRevenuIndexeCt, boucleResidu)
    # FR: Réduire le revenu par étapes pour atteindre le revenu indexé selon le taux d'indexation tauxIndexation pour l'impôt communal.
    # DE: Das Einkommen schrittweise reduzieren, um das indexierte Einkommen gemäss dem Indexierungssatz tauxIndexation für die Gemeindesteuer zu erreichen.
    compteur = 0
    while compteur < nbBoucles10pc:
        montantRevenuIndexeCo = revenuDeterminantLeTaux(montantRevenuIndexeCo, 1.10)
        compteur += 1
    montantRevenuIndexeCo = revenuDeterminantLeTaux(montantRevenuIndexeCo, boucleResidu)
    # FR: Impôt cantonal / DE: Kantonalsteuer
    montantImpotCantonal = round(montantRevenuBrut / 100 * calculTauxCt(montantRevenuIndexeCt), 2)
    # FR: Impôt communal / DE: Gemeindesteuer    
    montantImpotCommunal = round(montantRevenuBrut / 100 * calculTauxCo(montantRevenuIndexeCo), 2)
    # FR: Créer une table (facultatif). Attention, dans les documents officiels, toutes les valeurs sauf l'indexation sont multipliées par 10'000.
    # DE: Eine Tabelle erstellen (optional). Achtung: In offiziellen Dokumenten werden alle Werte ausser der Indexierung mit 10'000 multipliziert.
    print(str(tauxIndexation) + ';' + str(montantRevenuBrut) + ';' + str(calculTauxCt(montantRevenuIndexeCt)) + ';' + str(montantImpotCantonal) + ';' + str(calculTauxCo(montantRevenuIndexeCo)) + ';' + str(montantImpotCommunal))