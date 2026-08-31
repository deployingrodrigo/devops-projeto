from flask import Flask, jsonify #import do motor flask e jsonify, conversão de dicionários pythjon em respostas JSON

app = Flask(__name__) #variável especial utilizada para procurar arquivos relacionados ao projeto

@app.route("/") #quando acessado o / via GET, execute a função abaixo
def home(): #nome da função
    return jsonify({"mensagem": "API rodando com sucesso!"}) #transforma o dicionário em um JSON formatado e já configura os cabeçalhos HTTP

@app.route("/health") #utilizado por aplicações para saber se o serviço ainda está ativo, consultado de tempos em tempos
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000) #debug mostra erros detalhados no navegador, não recomendado em produção
    #host faz o servidor aceitar conexões de qualquer rede
    #porta 5000 é onde o servidor irá escutar, padrão do flask