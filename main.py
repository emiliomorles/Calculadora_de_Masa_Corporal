print("Calcule su índice de masa corporal (IMC)")
altura = float(input("Ingrese su altura en metros (ejemplo: 1.83): \n"))
peso = float(input("Ingrese su peso en kilogramos (ejemplo: 70): \n"))
# índice de masa corporal
imc = (peso / (altura ** 2))
imc_resultado = float(("%.2f" % imc))
if imc_resultado < 18.5:
   print(f"Tu IMC es {imc_resultado}\nTienes bajo peso.")
elif imc_resultado >= 18.5 and imc_resultado < 25:
   print(f"Su IMC es {imc_resultado}\n¡Felicitaciones!, tiene un peso normal.")
elif imc_resultado >= 25 and imc_resultado < 30:
   print(f"Tu IMC es {imc_resultado}\nTienes sobrepeso.")
elif imc_resultado >= 30 and imc_resultado < 35:
   print(f"Tu IMC es {imc_resultado}\nEres obeso.")
else:
   print("Eres clínicamente obeso.")