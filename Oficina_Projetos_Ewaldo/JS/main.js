function trocarTela(nomeTela) {
    document
        .getElementById("controle")
        .classList.add("oculto");
    document
        .getElementById("bnt_controle")
        .classList.add("Inativo");
    document
        .getElementById("bnt_controle")
        .classList.remove("Ativo");


    document
        .getElementById("agenda")
        .classList.add("oculto");
    document
        .getElementById("bnt_agenda")
        .classList.add("Inativo");
    document
        .getElementById("bnt_agenda")
        .classList.remove("Ativo");


    document
        .getElementById("estatisticas")
        .classList.add("oculto");
    document
        .getElementById("bnt_estatisticas")
        .classList.add("Inativo");
    document
        .getElementById("bnt_estatisticas")
        .classList.remove("Ativo");


    document
        .getElementById(nomeTela)
        .classList.remove("oculto");
    document
        .getElementById("bnt_" + nomeTela)
        .classList.add("Ativo");
    document
        .getElementById("bnt_" + nomeTela)
        .classList.remove("Inativo");
}