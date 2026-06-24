function trocarTela(nomeTela) {
    document.getElementById("controle").classList.add("oculto");
    document.getElementById("bnt_controle").classList.add("Inativo");
    document.getElementById("bnt_controle").classList.remove("Ativo");

    document.getElementById("agenda").classList.add("oculto");
    document.getElementById("bnt_agenda").classList.add("Inativo");
    document.getElementById("bnt_agenda").classList.remove("Ativo");

    document.getElementById("estatisticas").classList.add("oculto");
    document.getElementById("bnt_estatisticas").classList.add("Inativo");
    document.getElementById("bnt_estatisticas").classList.remove("Ativo");

    document.getElementById(nomeTela).classList.remove("oculto");
    document.getElementById("bnt_" + nomeTela).classList.add("Ativo");
    document.getElementById("bnt_" + nomeTela).classList.remove("Inativo");
}

let ultimoMinutoProcessado = "";
let monitoramentoIniciado = false;
let modo_popup = "";
let id_editando = null;
let listaAgenda = [];
let estadoAnteriorAlimentacaoAgendada = null;

if (!document.getElementById("estilo-status-piscando")) {
    const style = document.createElement("style");
    style.id = "estilo-status-piscando";
    style.innerHTML = `
        .piscando-amarelo {
            animation: piscarStatusSuave 1s infinite alternate;
        }
        @keyframes piscarStatusSuave {
            from { opacity: 1; }
            to { opacity: 0.5; }
        }
    `;
    document.head.appendChild(style);
}

function iniciarMonitoramentoHorarios() {
    setInterval(async () => {
        const agora = new Date();
        const horas = String(agora.getHours()).padStart(2, "0");
        const minutos = String(agora.getMinutes()).padStart(2, "0");
        const horarioAtual = `${horas}:${minutos}`;

        if (horarioAtual === ultimoMinutoProcessado) return;

        const temRefeicaoAgora = listaAgenda.some(item => {
            if (!item || !item.hora) return false;
            const horaFormatada = item.hora.slice(0, 5);
            return horaFormatada === horarioAtual;
        });

        if (temRefeicaoAgora) {
            ultimoMinutoProcessado = horarioAtual;
            await dispararRefeicaoAgendada();
        }
    }, 1000);
}

async function dispararRefeicaoAgendada() {
    try {
        const inputPeso = document.getElementById("qtd_porcao");
        const quantidadeAtual = inputPeso ? parseInt(inputPeso.value.replace(/[^0-9]/g, "")) || 400 : 400;

        console.log(`⏰ Horário correspondente encontrado! Iniciando refeição automática de ${quantidadeAtual}g...`);

        const { error: erroComando } = await supabaseClient
            .from("comando_alimentador")
            .update({ alimentacao_agendada: true })
            .eq("id", 0);

        if (erroComando) throw erroComando;
        console.log("✅ Coluna alimentacao_agendada alterada para true com sucesso!");

        const { error: erroAgendada } = await supabaseClient
            .from("alimentacao_agendada")
            .insert([{ quantidade: quantidadeAtual }]);

        if (erroAgendada) {
            console.warn("Erro ao inserir na tabela alimentacao_agendada:", erroAgendada.message);
        } else {
            console.log("✅ Registro adicionado à tabela alimentacao_agendada!");
        }

        await carregarQuantidadeAtual();

    } catch (error) {
        console.error("Erro crítico na execução da rotina agendada:", error);
    }
}

function atualizarMuralStatus(dadosComando) {
    if (!dadosComando) return;

    const isAgendada = dadosComando.alimentacao_agendada === true || dadosComando.alimentacao_agendada === "true";
    const isAgora = dadosComando.alimentar_agora === true || dadosComando.alimentar_agora === "true";
    const isExecutando = dadosComando.Executando === true || dadosComando.Executando === "true";
    const isAtualizadoSite = dadosComando.Atualizado_site === true || dadosComando.Atualizado_site === "true";
    const isConectadoEsp = dadosComando.Conectado_esp === true || dadosComando.Conectado_esp === "true";

    const statusElement = document.getElementById("status_atual");
    if (statusElement) {
        const divConexao = statusElement.closest(".conex_atual");
        const iconeElement = divConexao ? divConexao.querySelector("i") : null;

        const aplicarCorStatus = (cor) => {
            statusElement.style.color = color = cor;
            if (iconeElement) iconeElement.style.color = cor;
        };

        if (isAgendada) {
            statusElement.innerHTML = "DANDO RAÇÃO<br>AGENDADA";
            statusElement.style.textAlign = "center";
            aplicarCorStatus("#3498db");
            statusElement.classList.remove("piscando-amarelo");
            if (divConexao) divConexao.classList.remove("piscando-amarelo");
        } else if (isAgora) {
            statusElement.innerHTML = "DANDO RAÇÃO<br>AGORA";
            statusElement.style.textAlign = "center";
            aplicarCorStatus("#3498db");
            statusElement.classList.remove("piscando-amarelo");
            if (divConexao) divConexao.classList.remove("piscando-amarelo");
        } else {
            if (!isAtualizadoSite) {
                statusElement.textContent = "OFFLINE";
                statusElement.style.textAlign = "center";
                aplicarCorStatus("#ffcc00");
                statusElement.classList.add("piscando-amarelo");
                if (divConexao) divConexao.classList.add("piscando-amarelo");
            } else {
                statusElement.textContent = "ATUALIZADO";
                statusElement.style.textAlign = "center";
                aplicarCorStatus("#2ecc71");
                statusElement.classList.remove("piscando-amarelo");
                if (divConexao) divConexao.classList.remove("piscando-amarelo");
            }
        }
    }

    const espElement = document.getElementById("status_esp");
    if (espElement) {
        const iconeEsp = espElement.querySelector("i");
        const tituloEsp = espElement.querySelector("h3") || espElement.querySelector(".Titulo_h");

        const aplicarCorEsp = (cor) => {
            if (iconeEsp) iconeEsp.style.color = cor;
            if (tituloEsp) tituloEsp.style.color = cor;
        };

        if (isExecutando) {
            if (tituloEsp) {
                tituloEsp.innerHTML = "ESP32<br><span style='font-size: 0.75em; display: block; margin-top: 2px;'>EM ATIVIDADE</span>";
                tituloEsp.style.textAlign = "center";
            }
            aplicarCorEsp("#3498db");
            espElement.classList.remove("piscando-amarelo");
        } else {
            if (tituloEsp) {
                tituloEsp.textContent = "ESP32";
                tituloEsp.style.textAlign = "center";
            }

            if (isConectadoEsp) {
                aplicarCorEsp("#2ecc71");
                espElement.classList.remove("piscando-amarelo");
            } else {
                aplicarCorEsp("#ffcc00");
                espElement.classList.add("piscando-amarelo");
            }
        }
    }
}

async function carregarAgenda() {
    listaAgenda = await buscarAgenda();
    console.log("Agenda carregada:", listaAgenda);
    mostrarAgenda();

    atualizarResumosDashboard();
    atualizarProximaRefeicao();

    if (!monitoramentoIniciado) {
        iniciarMonitoramentoHorarios();
        monitoramentoIniciado = true;
    }
}

function mostrarAgenda() {
    let area = document.getElementById("lista_refeicoes");
    if (!area) return;

    area.innerHTML = "";

    if (!listaAgenda || listaAgenda.length == 0) {
        area.innerHTML = `<p>Nenhuma refeição programada</p>`;
        return;
    }

    let contador = 1;

    for (let refeicao of listaAgenda) {
        area.innerHTML += `
        <section class="cada_list">
            <div class="index_cada_list"><p>${contador}</p></div>
            <div class="hora_cada_list"><p>${refeicao.hora.slice(0, 5)}</p></div>
            <div class="qtd_cada_list"><p>${refeicao.quantidade}g</p></div>
            <button class="config_cada_list" onclick="abrirPopupEditar(${refeicao.id})">
                <i class="fa-solid fa-ellipsis-vertical"></i>
            </button>
        </section>
        `;
        contador++;
    }
}

async function carregarQuantidadeAtual() {
    let controle = await buscarQuantidadeAtual();

    if (!controle) {
        console.log("Não foi possível renderizar a quantidade atual.");
        return;
    }

    if (estadoAnteriorAlimentacaoAgendada !== null) {
        const eraTrue = estadoAnteriorAlimentacaoAgendada === true || estadoAnteriorAlimentacaoAgendada === "true";
        const agoraFalse = controle.alimentacao_agendada === false || controle.alimentacao_agendada === "false";

        if (eraTrue && agoraFalse) {
            console.log("🟢 O ESP32 terminou de alimentar e limpou o sinal! Salvando no histórico...");
            await registrarRefeicao(controle.quantidade);
            await carregarAgenda();
        }
    }
    estadoAnteriorAlimentacaoAgendada = controle.alimentacao_agendada;

    if (controle.Atualizado_site === false || controle.Atualizado_site === "false") {
        const campoPeso = document.getElementById("qtd_porcao");
        if (campoPeso) {
            const quantidadeNoSite = parseInt(campoPeso.value.replace(/[^0-9]/g, "")) || 0;

            if (controle.quantidade === quantidadeNoSite) {
                console.log("🔄 Reconciliação: Informações batem. Atualizando Atualizado_site para true...");
                await supabaseClient
                    .from("comando_alimentador")
                    .update({ Atualizado_site: true })
                    .eq("id", 0);
            } else {
                console.log(`🔄 Reconciliação: Divergência encontrada (${controle.quantidade}g no banco vs ${quantidadeNoSite}g no site). Forçando update da tabela...`);
                await supabaseClient
                    .from("comando_alimentador")
                    .update({
                        quantidade: quantidadeNoSite,
                        Atualizado_site: true
                    })
                    .eq("id", 0);
            }

            controle = await buscarQuantidadeAtual();
            if (!controle) return;
        }
    }

    let campo = document.getElementById("qtd_porcao");
    if (campo && document.activeElement !== campo) {
        campo.value = controle.quantidade + "g";
    }

    let label = document.getElementById("label_porcao_atual");
    if (label) {
        label.innerHTML = "será servido uma porção de " + controle.quantidade + "g";
    }

    atualizarMuralStatus(controle);
}

function abrirPopupNovo() {
    modo_popup = "novo";
    id_editando = null;

    document.getElementById("titulo_popup").innerText = "NOVA REFEIÇÃO";
    document.getElementById("btn_excluir").classList.add("oculto");
    document.getElementById("input_peso").value = "";
    document.getElementById("input_hora").value = "";

    let elMin = document.getElementById("input_min");
    if (elMin) elMin.value = "";

    document.getElementById("popup_agenda").classList.remove("oculto");
}

function abrirPopupEditar(id) {
    let agenda = listaAgenda.find(item => item.id == id);

    if (!agenda) {
        console.error("Não foi possível encontrar o agendamento com ID:", id);
        return;
    }

    modo_popup = "editar";
    id_editando = id;

    document.getElementById("titulo_popup").innerText = "EDITAR REFEIÇÃO";

    let btnExcluir = document.getElementById("btn_excluir");
    if (btnExcluir) btnExcluir.classList.remove("oculto");

    let elPeso = document.getElementById("input_peso");
    if (elPeso) {
        let pesoPuro = parseInt(agenda.quantidade || agenda.peso || 0);
        elPeso.value = pesoPuro;
    }

    let elHora = document.getElementById("input_hora");
    let elMin = document.getElementById("input_min");

    if (agenda.hora) {
        let partesHora = agenda.hora.split(":");
        let h = partesHora[0].padStart(2, "0");
        let m = (partesHora[1] || "00").padStart(2, "0");

        if (elMin) {
            if (elHora) elHora.value = h;
            elMin.value = m;
        } else if (elHora) {
            elHora.value = `${h}:${m}`;
        }
    }

    let popup = document.getElementById("popup_agenda");
    if (popup) popup.classList.remove("oculto");
}

function fecharPopupAgenda() {
    document.getElementById("popup_agenda").classList.add("oculto");
}

async function confirmarAgenda() {
    let pesoRaw = document.getElementById("input_peso").value;
    let horaInput = document.getElementById("input_hora").value;
    let elMin = document.getElementById("input_min");

    if (pesoRaw == "" || horaInput == "") {
        alert("Preencha todos os campos");
        return;
    }

    let horaFinal = "";
    if (elMin) {
        let minInput = elMin.value;
        if (minInput == "") {
            alert("Preencha os minutos");
            return;
        }
        horaFinal = `${horaInput.padStart(2, "0")}:${minInput.padStart(2, "0")}:00`;
    } else {
        horaFinal = horaInput.length === 5 ? horaInput + ":00" : horaInput;
    }

    let quantity = parseInt(pesoRaw);

    if (isNaN(quantity)) {
        alert("Por favor, insira um valor numérico válido para o peso.");
        return;
    }

    let resultado;

    if (modo_popup == "novo") {
        resultado = await adicionarAgenda(horaFinal, quantity);
    } else {
        resultado = await atualizarAgenda(id_editando, horaFinal, quantity);
    }

    if (resultado) {
        fecharPopupAgenda();
        carregarAgenda();
    } else {
        alert("Erro ao salvar dados na agenda.");
    }
}

async function excluirAgendaAtual() {
    if (id_editando == null) return;

    let confirmar = confirm("Deseja realmente excluir esta refeição?");
    if (!confirmar) return;

    let resultado = await excluirAgenda(id_editando);

    if (resultado) {
        fecharPopupAgenda();
        carregarAgenda();
    } else {
        alert("Erro ao tentar excluir.");
    }
}

async function alimentarAgora() {
    let qtdRaw = document.getElementById("qtd_porcao").value;
    let qtd = parseInt(qtdRaw);

    if (isNaN(qtd)) {
        alert("Insira uma quantidade válida antes de alimentar.");
        return;
    }

    let resultado = await mandarAlimentar(qtd);

    if (resultado) {
        alert("Comando de alimentação enviado!");
        await carregarQuantidadeAtual();
    } else {
        alert("Falha ao processar comando imediato.");
    }
}

async function atualizarResumosDashboard() {
    let historico = await buscarHistorico();

    let agora = new Date();
    let ano = agora.getFullYear();
    let mes = String(agora.getMonth() + 1).padStart(2, "0");
    let dia = String(agora.getDate()).padStart(2, "0");
    let hoje = `${ano}-${mes}-${dia}`;

    let refeicoesHoje = historico.filter(item => item.data === hoje);

    let elQtdComeu = document.getElementById("valor_qtd_comeu");
    if (elQtdComeu) {
        elQtdComeu.innerText = refeicoesHoje.length;
    }

    let totalGramas = refeicoesHoje.reduce((soma, item) => soma + Number(item.quantidade || 0), 0);
    let textoPeso = "";

    if (totalGramas >= 1000) {
        let totalKg = totalGramas / 1000;
        textoPeso = totalKg.toFixed(2).replace(".", ",") + " kg";
    } else {
        textoPeso = totalGramas + "g";
    }

    let elProxima = document.getElementById("proxima_refeicao");
    let elUltima = document.getElementById("ultima_refeicao");

    if (elProxima) {
        elProxima.innerText = textoPeso;
    }

    if (elUltima) {
        elUltima.innerText = "Total consumido: " + textoPeso;
    }
}

function atualizarProximaRefeicao() {
    let elProxima = document.getElementById("hora_proxima_refeicao");
    let elCountdown = document.getElementById("tempo_restante");

    if (!elProxima) return;

    if (!listaAgenda || listaAgenda.length === 0) {
        elProxima.innerText = "--:--";
        if (elCountdown) elCountdown.innerText = "Nenhuma programada";
        return;
    }

    let agendaOrdenada = [...listaAgenda].sort((a, b) => a.hora.localeCompare(b.hora));

    let agora = new Date();
    let proximaRefeicao = null;
    let dataProxima = null;

    for (let refeicao of agendaOrdenada) {
        let [h, m, s] = refeicao.hora.split(":").map(Number);
        let dataRefeicao = new Date(agora);
        dataRefeicao.setHours(h, m, s || 0, 0);

        if (dataRefeicao > agora) {
            proximaRefeicao = refeicao;
            dataProxima = dataRefeicao;
            break;
        }
    }

    if (!proximaRefeicao) {
        proximaRefeicao = agendaOrdenada[0];
        let [h, m, s] = proximaRefeicao.hora.split(":").map(Number);
        dataProxima = new Date(agora);
        dataProxima.setDate(agora.getDate() + 1);
        dataProxima.setHours(h, m, s || 0, 0);
    }

    elProxima.innerText = proximaRefeicao.hora.slice(0, 5);

    let diferencaMs = dataProxima - agora;
    let totalMinutos = Math.floor(diferencaMs / 1000 / 60);
    let horasRestantes = Math.floor(totalMinutos / 60);
    let minutesRestantes = totalMinutos % 60;

    if (elCountdown) {
        let hFormatada = String(horasRestantes).padStart(2, "0");
        let mFormatada = String(minutesRestantes).padStart(2, "0");
        elCountdown.innerText = `Faltam ${hFormatada}h ${mFormatada}min`;
    }
}

function configurarControleQuantidade() {
    let btnMenos = document.getElementById("bnt_menos");
    let btnMais = document.getElementById("bnt_mais");
    let inputPeso = document.getElementById("qtd_porcao");

    if (!inputPeso) return;

    function obtenerValorAtual() {
        let valorLimpo = inputPeso.value.replace(/[^0-9]/g, "");
        return parseInt(valorLimpo) || 0;
    }

    async function atualizarESalvar(novoValor) {
        if (novoValor > 900) {
            novoValor = 900;
        } else if (novoValor < 0) {
            novoValor = 0;
        }

        inputPeso.value = novoValor + "g";

        let label = document.getElementById("label_porcao_atual");
        if (label) {
            label.innerHTML = "será servido uma porção de " + novoValor + "g";
        }

        await salvarQuantidadeNoBanco(novoValor);
    }

    if (btnMenos) {
        btnMenos.addEventListener("click", async () => {
            let valorAtual = obtenerValorAtual();
            await atualizarESalvar(valorAtual - 100);
        });
    }

    if (btnMais) {
        btnMais.addEventListener("click", async () => {
            let valorAtual = obtenerValorAtual();
            await atualizarESalvar(valorAtual + 100);
        });
    }

    inputPeso.addEventListener("focus", () => {
        let valorAtual = obtenerValorAtual();
        inputPeso.value = valorAtual === 0 ? "" : valorAtual;
    });

    inputPeso.addEventListener("blur", async () => {
        let valorAtual = obtenerValorAtual();
        await atualizarESalvar(valorAtual);
    });
}

window.addEventListener("load", () => {
    testarSupabase();
    carregarAgenda();
    carregarQuantidadeAtual();
    configurarControleQuantidade();

    setInterval(carregarQuantidadeAtual, 3000);

    setInterval(atualizarProximaRefeicao, 60000);
});