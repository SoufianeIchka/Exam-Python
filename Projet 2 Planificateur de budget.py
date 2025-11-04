distance_km_str = input("Quelle est la distance totale du voyage (aller-retour) en km ? ")
distance_km = float(distance_km_str)
efficiency_str = input("Quelle est la consommation de votre voiture (litres / 100 km) ? ")
efficiency = float(efficiency_str)
price_per_liter_str = input("Quel est le prix actuel d'un litre de carburant (€) ? ")
price_per_liter = float(price_per_liter_str)
fuel_needed = (distance_km / 100) * efficiency
total_cost = fuel_needed * price_per_liter
total_cost = round(total_cost, 2)
print("\n--- BUDGET CARBURANT ESTIMÉ ---")
print(f"Distance totale du voyage : {distance_km:.1f} km")
print(f"Le coût estimé du carburant pour ce voyage sera de {total_cost:.2f} €")
print(f"Quantité totale de carburant nécessaire : {fuel_needed:.2f} litres")
input("\nAppuyez sur Entrée pour fermer...")
