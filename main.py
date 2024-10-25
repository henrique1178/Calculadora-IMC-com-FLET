import flet as ft

def main(page: ft.Page):
  
  def Imc(e):
    imc = float(peso.value)/ (float(altura.value) ** 2)
    if imc <= 18.5:
      resultado.value = f"IMC: {imc:.2f} - Abaixo do Peso"
      resultado.bgcolor = "#e0151d"
      resultado.color = "white"
    elif imc <= 24.9:
      resultado.value = f"IMC: {imc:.2f} - Peso Normal"
      resultado.bgcolor = "#009f2b"
      resultado.color = "white"
    elif imc <= 29.9:
      resultado.value = f"IMC: {imc:.2f} - Sobrepeso"
      resultado.bgcolor = "#b50b0f"
      resultado.color = "white"
    elif imc <= 34.9:
      resultado.value = f"IMC: {imc:.2f} - Obesidade grau I"
      resultado.bgcolor = "#9f0507"
      resultado.color = "white"
    elif imc <= 39.9:
      resultado.value = f"IMC: {imc:.2f} - Obesidade grau II"
      resultado.bgcolor = "#890000"
      resultado.color = "white"
    elif imc >= 40:
      resultado.value = f"IMC: {imc:.2f} - Obesidade grau III"
      resultado.bgcolor = "#660000"
      resultado.color = "white"
    else:
      resultado.value = "Erro"
    resultado.size = 20
    resultado.update()
    
  
  page.title = "Calculo de IMC"
  txt = ft.Text(value="Calcular o IMC abaixo",size=40)
  
  peso = ft.TextField(label="Seu Peso: ", keyboard_type=ft.KeyboardType.NUMBER)
  altura = ft.TextField(label="Sua Altura: ", keyboard_type=ft.KeyboardType.NUMBER)
  botao = ft.ElevatedButton(text="Calcular", on_click=Imc)
  resultado = ft.Text(value="", size=25, color="white")
  
  page.add(txt,peso,altura,botao,resultado)

  
ft.app(target=main)