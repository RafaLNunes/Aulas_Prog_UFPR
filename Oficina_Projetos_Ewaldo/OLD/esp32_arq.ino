#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <ESP32Servo.h>
#include <AccelStepper.h>
#include <time.h>
#include <math.h>

// Config

const char* WIFI_NOME  = "Net1-Nunes";
const char* WIFI_SENHA = "Net1#t$2&eg%HWF";

const char* SUPABASE_URL = "https://zibmdgkchmfobfbkmbcr.supabase.co";
const char* SUPABASE_KEY = "sb_publishable_QyQ-qXNIZ_CUlJDzrhGlXA_fjAxjnPM";

const char* DT_COMANDO   = "comando_alimentador";
const char* DT_PENDENTE  = "alimentacao_pendente";
const char* DT_HISTORICO = "historico_refeicoes";

const char* COLUNA_AGENDADA = "alimentacao_agendada";

const bool SALVAR_HISTORICO = true;

// Pinagem

const int PIN_SERVO = 18;

const int PIN_MOTOR_P1 = 14;
const int PIN_MOTOR_P2 = 27;
const int PIN_MOTOR_P3 = 26;
const int PIN_MOTOR_P4 = 25;

// transições do servo

const int SERVO_FECHADO = 20;
const int SERVO_ABERTO  = 70;

const int SERVO_MIN_US = 1000;
const int SERVO_MAX_US = 2000;

const unsigned long TEMPO_SERVO_MOV = 700;

const float TEMPO_POR_GRAMA_MS = 15.0;

const unsigned long TEMPO_MIN_ALETA_ABERTA = 500;
const unsigned long TEMPO_MAX_ALETA_ABERTA = 15000;

// Ajustes da balança

const long PASSOS_90_GRAUS = 512;

const int VELOCIDADE_MAX = 700;
const int ACELERACAO = 300;

const unsigned long TEMPO_RACAO_CAIR = 1500;

// Tempos gerais

const unsigned long TEMPO_CONSULTA_DB = 3000;

// Serial

void msg(const char* texto) {
  Serial.println(texto);
}

void msg_val(const char* texto, int valor) {
  Serial.print(texto);
  Serial.print(": ");
  Serial.println(valor);
}

void msg_val(const char* texto, float valor) {
  Serial.print(texto);
  Serial.print(": ");
  Serial.println(valor);
}

void msg_val(const char* texto, unsigned long valor) {
  Serial.print(texto);
  Serial.print(": ");
  Serial.println(valor);
}

// Struct

struct Comando {
  bool alimentar_agora = false;
  bool alimentacao_agendada = false;
  bool executando = false;
  int quantidade = 0;
};

// Motor base

class Motor {
public:
  virtual void iniciar() = 0;
  virtual void executar() = 0;
  virtual void parar() = 0;
};

// Servo

class MotorServo : public Motor {
private:
  Servo servo;
  int pin;
  int fechado;
  int aberto;

public:
  MotorServo(int pin_servo, int ang_fechado, int ang_aberto) {
    pin = pin_servo;
    fechado = ang_fechado;
    aberto = ang_aberto;
  }

  void iniciar() {
    msg("SERVO Iniciado");

    servo.attach(pin, SERVO_MIN_US, SERVO_MAX_US);
    delay(300);

    parar();
  }

  void executar() {
    msg("SERVO Feito");

    servo.write(aberto);
    delay(TEMPO_SERVO_MOV);
  }

  void parar() {
    msg("SERVO Desativado");

    servo.write(fechado);
    delay(TEMPO_SERVO_MOV);
  }
};

// Motor de passo

class MotorPasso : public Motor {
private:
  AccelStepper motor;
  long passos;

public:
  MotorPasso(int p1, int p2, int p3, int p4, long qtd_passos)
  : motor(AccelStepper::FULL4WIRE, p1, p3, p2, p4) {
    passos = qtd_passos;
  }

  void iniciar() {
    msg("PASSO Iniciado");

    motor.setMaxSpeed(VELOCIDADE_MAX);
    motor.setAcceleration(ACELERACAO);

    msg("PASSO Feito");
  }

  void mover(long qtd) {
    msg_val("PASSOS", (int)qtd);

    motor.move(qtd);

    while (motor.distanceToGo() != 0) {
      motor.run();
      delay(1);
    }

    msg("MOVE Feito");
  }

  void executar() {
    msg("PASSO Ligado");

    mover(passos);

    msg("CAI");
    delay(TEMPO_RACAO_CAIR);

    mover(-passos);

    msg("PASSO Desligado");
  }

  void parar() {
    msg("PASSO Parado");
    motor.stop();
  }
};

// Supabase

class BancoSupabase {
private:
  String url;
  String key;

public:
  BancoSupabase(const char* supa_url, const char* supa_key) {
    url = String(supa_url);
    key = String(supa_key);
  }

  void conectar_wifi() {
    msg("WIFI");

    WiFi.mode(WIFI_STA);
    WiFi.disconnect();
    delay(100);

    WiFi.begin(WIFI_NOME, WIFI_SENHA);

    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }

    Serial.println();
    msg("ONLINE");
    Serial.println(WiFi.localIP());
  }

  void iniciar_horario() {
    msg("HORA");

    configTime(-3 * 3600, 0, "pool.ntp.org", "time.nist.gov");
    delay(1000);
  }

  bool enviar(String metodo, String tabela, String filtro, String corpo, String &resposta) {
    if (WiFi.status() != WL_CONNECTED) {
      msg("WIFI Fora do Ar");
      return false;
    }

    WiFiClientSecure client;
    client.setInsecure();

    HTTPClient http;

    String endpoint = url + "/rest/v1/" + tabela + filtro;

    if (metodo == "GET") {
      msg("DB GET");
    }

    if (metodo == "PATCH") {
      msg("DB PATCH");
    }

    if (metodo == "POST") {
      msg("DB POST");
    }

    http.begin(client, endpoint);
    http.addHeader("Content-Type", "application/json");
    http.addHeader("apikey", key);
    http.addHeader("Authorization", String("Bearer ") + key);
    http.addHeader("Prefer", "return=representation");

    int codigo = 0;

    if (metodo == "GET") {
      codigo = http.GET();
    }

    if (metodo == "PATCH") {
      codigo = http.PATCH(corpo);
    }

    if (metodo == "POST") {
      codigo = http.POST(corpo);
    }

    resposta = http.getString();

    msg_val("HTTP", codigo);

    http.end();

    if (codigo >= 200 && codigo < 300) {
      msg("DB OK");
      return true;
    }

    msg("DB ERRO");

    if (resposta.length() > 0) {
      Serial.println(resposta);
    }

    return false;
  }

  bool atualizar_comando(String corpo) {
    String resposta;

    return enviar(
      "PATCH",
      DT_COMANDO,
      "?id=eq.0",
      corpo,
      resposta
    );
  }

  bool buscar_comando(Comando &cmd) {
    String resposta;

    bool deu_certo = enviar(
      "GET",
      DT_COMANDO,
      "?id=eq.0&select=*",
      "",
      resposta
    );

    if (!deu_certo) {
      return false;
    }

    StaticJsonDocument<1024> doc;

    DeserializationError erro = deserializeJson(doc, resposta);

    if (erro) {
      msg("JSON ERRO");
      return false;
    }

    JsonArray lista = doc.as<JsonArray>();

    if (lista.size() == 0) {
      msg("SEM ROW");
      return false;
    }

    JsonObject linha = lista[0];

    cmd.alimentar_agora = linha["alimentar_agora"] | false;
    cmd.alimentacao_agendada = linha[COLUNA_AGENDADA] | false;
    cmd.executando = linha["Executando"] | false;
    cmd.quantidade = linha["quantidade"] | 0;

    if (cmd.alimentar_agora) {
      msg("AGORA");
    } else if (cmd.alimentacao_agendada) {
      msg("AGENDA");
    } else {
      msg("IDLE");
    }

    return true;
  }

  bool buscar_qtd_pendente(int &qtd) {
    String resposta;

    bool deu_certo = enviar(
      "GET",
      DT_PENDENTE,
      "?select=id,quantidade&order=id.desc&limit=1",
      "",
      resposta
    );

    if (!deu_certo) {
      return false;
    }

    StaticJsonDocument<512> doc;

    DeserializationError erro = deserializeJson(doc, resposta);

    if (erro) {
      msg("JSON ERRO");
      return false;
    }

    JsonArray lista = doc.as<JsonArray>();

    if (lista.size() == 0) {
      msg("SEM QTD");
      return false;
    }

    int id_linha = lista[0]["id"] | 0;
    qtd = lista[0]["quantidade"] | 0;

    msg_val("ID", id_linha);
    msg_val("QTD", qtd);

    return qtd > 0;
  }

  void set_conectado() {
    msg("PING");

    String corpo = "{\"Conectado_esp\":true}";

    atualizar_comando(corpo);
  }

  void set_executando(bool valor) {
    String corpo;

    if (valor) {
      msg("EXEC ON");

      corpo = "{";
      corpo += "\"Executando\":true,";
      corpo += "\"Conectado_esp\":true";
      corpo += "}";
    } else {
      msg("EXEC OFF");

      corpo = "{";
      corpo += "\"Executando\":false,";
      corpo += "\"Conectado_esp\":true";
      corpo += "}";
    }

    atualizar_comando(corpo);
  }

  void finalizar_comando() {
    msg("LIMPA");

    String corpo = "{";
    corpo += "\"alimentar_agora\":false,";
    corpo += "\"";
    corpo += COLUNA_AGENDADA;
    corpo += "\":false,";
    corpo += "\"Executando\":false,";
    corpo += "\"Conectado_esp\":true";
    corpo += "}";

    atualizar_comando(corpo);
  }

  String data_atual() {
    struct tm tempo;

    if (!getLocalTime(&tempo)) {
      return "";
    }

    char buffer[11];
    strftime(buffer, sizeof(buffer), "%Y-%m-%d", &tempo);

    return String(buffer);
  }

  String hora_atual() {
    struct tm tempo;

    if (!getLocalTime(&tempo)) {
      return "";
    }

    char buffer[9];
    strftime(buffer, sizeof(buffer), "%H:%M:%S", &tempo);

    return String(buffer);
  }

  bool salvar_historico(int qtd) {
    if (!SALVAR_HISTORICO) {
      msg("HIST OFF");
      return true;
    }

    msg("HIST");

    String data = data_atual();
    String hora = hora_atual();

    String corpo = "{";

    if (data.length() > 0) {
      corpo += "\"data\":\"" + data + "\",";
    }

    if (hora.length() > 0) {
      corpo += "\"hora\":\"" + hora + "\",";
    }

    corpo += "\"quantidade\":";
    corpo += String(qtd);
    corpo += "}";

    String resposta;

    return enviar(
      "POST",
      DT_HISTORICO,
      "",
      corpo,
      resposta
    );
  }
};

// App

class AutoDogFood {
private:
  BancoSupabase &banco;
  MotorServo &servo;
  MotorPasso &passo;

  bool ocupado;
  unsigned long ultima_consulta;

public:
  AutoDogFood(
    BancoSupabase &banco_ref,
    MotorServo &servo_ref,
    MotorPasso &passo_ref
  )
  : banco(banco_ref),
    servo(servo_ref),
    passo(passo_ref) {
      ocupado = false;
      ultima_consulta = 0;
  }

  void iniciar() {
    msg("APP INIT");

    servo.iniciar();
    passo.iniciar();

    banco.set_conectado();
    banco.set_executando(false);

    msg("PRONTO");
  }

  int limitar_qtd(int qtd) {
    if (qtd < 1) {
      msg("QTD MIN");
      return 1;
    }

    if (qtd > 900) {
      msg("QTD MAX");
      return 900;
    }

    return qtd;
  }

  unsigned long calcular_tempo_abertura(int qtd) {
    float tempo = qtd * TEMPO_POR_GRAMA_MS;

    if (tempo < TEMPO_MIN_ALETA_ABERTA) {
      tempo = TEMPO_MIN_ALETA_ABERTA;
    }

    if (tempo > TEMPO_MAX_ALETA_ABERTA) {
      tempo = TEMPO_MAX_ALETA_ABERTA;
    }

    return (unsigned long)tempo;
  }

  int pegar_quantidade(Comando cmd) {
    if (cmd.alimentar_agora) {
      msg("MANUAL");
      return limitar_qtd(cmd.quantidade);
    }

    if (cmd.alimentacao_agendada) {
      msg("PENDENTE");

      int qtd_pendente = 0;

      if (banco.buscar_qtd_pendente(qtd_pendente)) {
        return limitar_qtd(qtd_pendente);
      }

      msg("QTD BACKUP");
      return limitar_qtd(cmd.quantidade);
    }

    return 0;
  }

  void dar_racao(int qtd) {
    msg("COMANDO");

    if (ocupado) {
      msg("OCUPADO");
      return;
    }

    qtd = limitar_qtd(qtd);

    if (qtd <= 0) {
      msg("QTD ERRO");
      banco.finalizar_comando();
      return;
    }

    ocupado = true;

    banco.set_executando(true);

    msg("EXEC");
    msg_val("QTD", qtd);

    unsigned long tempo_abertura = calcular_tempo_abertura(qtd);

    msg_val("TEMPO", tempo_abertura);

    msg("DOSA");
    servo.executar();

    delay(tempo_abertura);

    servo.parar();

    delay(700);

    msg("PASSO");
    passo.executar();

    banco.salvar_historico(qtd);

    banco.finalizar_comando();

    ocupado = false;

    msg("FIM");
  }

  void loop_principal() {
    if (millis() - ultima_consulta < TEMPO_CONSULTA_DB) {
      return;
    }

    ultima_consulta = millis();

    msg("CHECK");

    banco.set_conectado();

    Comando cmd;

    bool leu = banco.buscar_comando(cmd);

    if (!leu) {
      msg("LEIT ERRO");
      return;
    }

    if (cmd.executando || ocupado) {
      msg("OCUPADO");
      return;
    }

    if (cmd.alimentar_agora || cmd.alimentacao_agendada) {
      int qtd = pegar_quantidade(cmd);
      dar_racao(qtd);
    }
  }
};

// Objetos

BancoSupabase banco(SUPABASE_URL, SUPABASE_KEY);

MotorServo motor_servo(
  PIN_SERVO,
  SERVO_FECHADO,
  SERVO_ABERTO
);

MotorPasso motor_passo(
  PIN_MOTOR_P1,
  PIN_MOTOR_P2,
  PIN_MOTOR_P3,
  PIN_MOTOR_P4,
  PASSOS_90_GRAUS
);

AutoDogFood app(
  banco,
  motor_servo,
  motor_passo
);

// Setup / Loop

void setup() {
  Serial.begin(115200);
  delay(1000);

  msg("INIT");

  banco.conectar_wifi();
  banco.iniciar_horario();

  app.iniciar();
}

void loop() {
  app.loop_principal();
  delay(10);
}