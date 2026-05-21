function calcularOrcamento() {
    
    var inputNome = document.getElementById("nomeUsuario");
    var inputQuantidade = document.getElementById("quantidadeTijolos");
    var exibirNome = document.getElementById("exibirNome");
    var exibirResultado = document.getElementById("exibirResultado");
    

    let tijolo = 0.70;
    
  
    let quantidade = Number(inputQuantidade.value);
    let total = quantidade * tijolo;
    
   
    exibirNome.innerHTML = "Nome do Cliente: " + inputNome.value;
    exibirResultado.innerHTML = "O valor é: R$ " + total.toFixed(2);
}
