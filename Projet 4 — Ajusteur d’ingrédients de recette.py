original_amount_str = input("Quantité originale de l'ingrédient (ex: 250) : ")
original_amount = float(original_amount_str)

original_servings_str = input("La recette originale est pour combien de personnes ? ")
original_servings = int(original_servings_str)

desired_servings_str = input("Pour combien de personnes voulez-vous cuisiner ? ")
desired_servings = int(desired_servings_str)
scaling_factor = desired_servings / original_servings
new_amount = round(original_amount * scaling_factor, 1)
print("\n--- RECETTE AJUSTÉE ---")
print(f"La recette originale est pour {original_servings} personnes.")
print(f"Pour cuisiner pour {desired_servings} personnes, vous aurez besoin de {new_amount} unités de votre ingrédient.")
input("\nAppuyez sur Entrée pour fermer...")