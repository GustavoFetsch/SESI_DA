function multiplicacao(){
  var campo1 = document.getElementById("campo1")
  var resultado = document.getElementById("resultado")
  let tijolo = 0.70

    resultado.innerHTML = "resultado:" + (Number(campo1.value) * Number(tijolo))
  }
