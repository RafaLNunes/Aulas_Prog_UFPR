const SUPABASE_URL = "https://zibmdgkchmfobfbkmbcr.supabase.co";
const SUPABASE_KEY = "sb_publishable_QyQ-qXNIZ_CUlJDzrhGlXA_fjAxjnPM";

const supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_KEY);

function statusSupabase(estado) {
    let elemento = document.getElementById("status_supabase");
    if (!elemento) return;

    elemento.classList.remove("supabase_offline", "supabase_connecting", "supabase_online");
    elemento.classList.add("supabase_" + estado);
}

async function testarSupabase() {
    statusSupabase("connecting");

    const { error } = await supabaseClient
        .from("agenda_refeicoes")
        .select("id")
        .limit(1);

    if (error) {
        console.log("Erro Supabase:", error);
        statusSupabase("offline");
        return false;
    }

    console.log("Supabase conectado");
    statusSupabase("online");
    return true;
}

async function buscarAgenda() {
    const { data, error } = await supabaseClient
        .from("agenda_refeicoes")
        .select("*")
        .order("hora", { ascending: true });

    if (error) {
        console.log("Erro agenda:", error);
        return [];
    }

    return data;
}

async function adicionarAgenda(hora, quantidade) {
    const { data, error } = await supabaseClient
        .from("agenda_refeicoes")
        .insert({
            hora: hora,
            quantidade: Number(quantidade)
        })
        .select();

    if (error) {
        console.log("Erro adicionando agenda:", error);
        return false;
    }

    return true;
}

async function atualizarAgenda(id, hora, quantidade) {
    const { error } = await supabaseClient
        .from("agenda_refeicoes")
        .update({
            hora: hora,
            quantidade: Number(quantidade)
        })
        .eq("id", id);

    if (error) {
        console.log("Erro ao atualizar agenda:", error);
        return false;
    }

    return true;
}

async function excluirAgenda(id) {
    const { error } = await supabaseClient
        .from("agenda_refeicoes")
        .delete()
        .eq("id", id);

    if (error) {
        console.log("Erro excluir:", error);
        return false;
    }

    return true;
}

async function registrarRefeicao(quantidade) {
    let agora = new Date();

    const { error } = await supabaseClient
        .from("historico_refeicoes")
        .insert({
            data: agora.toISOString().split("T")[0],
            hora: agora.toTimeString().slice(0, 8),
            quantidade: Number(quantidade)
        });

    if (error) {
        console.log("Erro ao registrar no histórico de refeições:", error);
        return false;
    }

    return true;
}

async function buscarHistorico() {
    const { data, error } = await supabaseClient
        .from("historico_refeicoes")
        .select("*")
        .order("criado_em", { ascending: false });

    if (error) {
        console.log(error);
        return [];
    }

    return data;
}

async function mandarAlimentar(quantidade) {
    const { error } = await supabaseClient
        .from("comando_alimentador")
        .update({
            alimentar_agora: true,
            quantidade: Number(quantidade),
            Executando: false
        })
        .eq("id", 0);

    if (error) {
        console.log("Erro mandar comando:", error);
        return false;
    }

    const { error: erroAgendada } = await supabaseClient
        .from("alimentacao_agendada")
        .insert([{ quantidade: Number(quantidade) }]);

    if (erroAgendada) {
        console.warn("Aviso ao salvar log na tabela alimentacao_agendada:", erroAgendada.message);
    }

    return true;
}

async function buscarComandoAlimentador() {
    const { data, error } = await supabaseClient
        .from("comando_alimentador")
        .select("*");

    if (error) {
        console.log("Erro comando:", error);
        return null;
    }

    return data;
}

async function finalizarAlimentacao() {
    const { error } = await supabaseClient
        .from("comando_alimentador")
        .update({
            alimentar_agora: false,
            alimentacao_agendada: false,
            Executando: false
        })
        .eq("id", 0);

    if (error) {
        console.log("Erro finalizar:", error);
        return false;
    }

    return true;
}

async function buscarQuantidadeAtual() {
    const { data, error } = await supabaseClient
        .from("comando_alimentador")
        .select("*")
        .eq("id", 0)
        .maybeSingle();

    if (error) {
        console.log("Erro quantidade atual:", error);
        return null;
    }

    return data;
}

async function salvarQuantidadeNoBanco(quantidade) {
    try {
        const { data, error } = await supabaseClient
            .from("comando_alimentador")
            .update({ quantidade: quantidade })
            .eq("id", 0)
            .select();

        if (error) throw error;

        if (!data || data.length === 0) {
            console.warn("⚠️ O banco rejeitou a atualização. Verifique as RLS Policies.");
            return;
        }

        console.log(`[Supabase] Sucesso! Banco atualizado para: ${quantidade}g`);
    } catch (erro) {
        console.error("Erro crítico ao salvar quantidade na database:", erro);
    }
}

async function buscarStatusESP() {
    const { data, error } = await supabaseClient
        .from("comando_alimentador")
        .select("Executando")
        .eq("id", 0)
        .maybeSingle();

    if (error) {
        console.log(error);
        return null;
    }

    return data;
}