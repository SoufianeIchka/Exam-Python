base_score = 1000
coins_collected_str = input("Combien de pièces avez-vous collectées ? ")
coins_collected = int(coins_collected_str)

no_damage_input = input("Avez-vous terminé le niveau sans subir de dégâts ? (oui/non) : ")
no_damage_bonus = (no_damage_input.lower() == "oui")
coin_bonus = coins_collected * 50
damage_multiplier = 2 if no_damage_bonus else 1
final_score = (base_score + coin_bonus) * damage_multiplier
print("\n*** NIVEAU TERMINÉ ! ***")
print(f"Score de base : {base_score}")
print(f"Bonus (pièces) : +{coin_bonus}")
print(f"Multiplicateur (sans dégâts) : x{damage_multiplier}")
print(f"\nSCORE FINAL : {final_score}")
input("\nAppuyez sur Entrée pour fermer...")