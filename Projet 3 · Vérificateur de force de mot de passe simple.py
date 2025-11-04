password = input("Entrez votre mot de passe : ")
password_length = len(password)

# Vérifier la présence d’un chiffre
has_digit = (
    '0' in password or '1' in password or '2' in password or
    '3' in password or '4' in password or '5' in password or
    '6' in password or '7' in password or '8' in password or '9' in password
)
is_long_enough = password_length >= 8
is_strong = is_long_enough and has_digit
print("\n--- RAPPORT DE FORCE DU MOT DE PASSE ---")
print(f"Longueur d'au moins 8 caractères : {'✅' if is_long_enough else '❌'}")
print(f"Contient au moins un chiffre      : {'✅' if has_digit else '❌'}")

if is_strong:
    print("Conclusion : Votre mot de passe est considéré comme fort ! 💪")
else:
    print("Conclusion : Votre mot de passe peut être amélioré. 🔐")
input("\nAppuyez sur Entrée pour fermer...")