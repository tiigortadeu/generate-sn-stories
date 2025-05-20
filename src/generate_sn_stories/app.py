import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import traceback
import tempfile
import time
from flask import Flask, render_template_string, request

# Carregar variáveis do .env automaticamente
try:
    from dotenv import load_dotenv
    load_dotenv()
    print('✅ Variáveis do .env carregadas com sucesso.')
except ImportError:
    print('⚠️ python-dotenv não instalado. Para suporte a .env, instale com: pip install python-dotenv')

# Garante que o src/check_us_crew está no sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'generate_sn_stories', 'src')
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# Importa a função correta
from generate_sn_stories.main import run

# Configurando diretório de saída
os.makedirs('output', exist_ok=True)

# HTML template
HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Validador de Código ServiceNow</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; max-width: 1200px; margin: 0 auto; padding: 20px; }
        h1 { color: #333; text-align: center; margin-bottom: 30px; }
        textarea { width: 100%; height: 300px; padding: 10px; border: 1px solid #ccc; border-radius: 4px; }
        input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; }
        button { background-color: #4CAF50; color: white; padding: 12px 24px; border: none; border-radius: 4px; 
                 cursor: pointer; font-size: 16px; margin-top: 10px; }
        button:hover { background-color: #45a049; }
        .relatorio { margin-top: 30px; background: #f9f9f9; padding: 20px; border-radius: 8px; border: 1px solid #ddd; }
        .loading { display: none; text-align: center; margin: 20px 0; }
        label { display: block; margin: 10px 0 5px; font-weight: bold; }
        .info { color: #666; font-size: 14px; margin-bottom: 20px; }
        .error { color: #ff0000; background: #ffeeee; padding: 15px; border-radius: 5px; margin: 20px 0; }
        .success { color: #008000; background: #eeffee; padding: 15px; border-radius: 5px; margin: 20px 0; }
        .progress { color: #0066cc; background: #eef8ff; padding: 15px; border-radius: 5px; margin: 20px 0; }
        pre { white-space: pre-wrap; word-wrap: break-word; }
    </style>
</head>
<body>
    <h1>Criador de User Stories</h1>
    
    <div class="info">
       <p>Este é um sistema que cria User Stories para o ServiceNow, a partir de um requisito informado pelo usuário.</p>
    </div>

    <form method="post" id="analysisForm">
        <label for="snippet">Requisito:</label>
        <textarea name="snippet" id="snippet" required>{{ snippet or '' }}</textarea>
        
        <label for="repository">Nome do Repositório (opcional):</label>
        <input type="text" name="repository" id="repository" value="{{ repository or '' }}">
        
        <button type="submit" id="analyzeBtn">Analisar Código</button>
    </form>
    
    <div id="loading" class="loading">
        <p>Analisando código, por favor aguarde... (isso pode demorar alguns minutos)</p>
    </div>
    
    {% if log %}
    <div class="progress">
        <h3>Log de Processamento:</h3>
        <pre>{{ log }}</pre>
    </div>
    {% endif %}
    
    {% if error %}
    <div class="error">
        <h3>Erro durante análise:</h3>
        <pre>{{ error }}</pre>
    </div>
    {% endif %}
    
    {% if relatorio %}
    <div class="relatorio">
        <h2>Relatório de Análise</h2>
        <pre>{{ relatorio }}</pre>
    </div>
    {% endif %}

    <script>
        document.getElementById('analysisForm').addEventListener('submit', function() {
            document.getElementById('analyzeBtn').disabled = true;
            document.getElementById('loading').style.display = 'block';
        });
    </script>
</body>
</html>
"""

def identify_requirements(code_snippet):
    """
    Executa a análise usando a função do main.py
    """
    print(f"🚀 Gerando User Stories...")
    
    result_text, log_messages, error = run(code_snippet)
    
    # Verificar se relatório foi gerado
    try:
        time.sleep(2)  # Pequeno delay para garantir que o arquivo está pronto
        report_path = os.path.join('output', 'stories.md')
        if os.path.exists(report_path):
            with open(report_path, 'r', encoding='utf-8') as f:
                relatorio = f.read()
            print(f"✅ Relatório gerado com sucesso")
            return relatorio, "\n".join(log_messages), None
        else:
            # Retornar o resultado bruto se o arquivo não existir
            print(f"⚠️ Arquivo de relatório não encontrado, usando resultado bruto")
            return result_text, "\n".join(log_messages), None
    except Exception as e:
        print(f"❌ Erro ao ler o relatório: {e}")
        return result_text, "\n".join(log_messages), f"Erro ao ler o relatório: {str(e)}"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    relatorio = None
    log = None
    error = None
    snippet = ""
    repository = ""
    
    if request.method == "POST":
        snippet = request.form["snippet"]
        
        
        try:
            print("📊 Iniciando análise do código...")
            relatorio, log, error = identify_requirements(snippet)
            if relatorio:
                print("✅ Análise concluída com sucesso")
        except Exception as e:
            print(f"❌ ERRO durante análise: {str(e)}")
            error = f"Erro durante análise: {str(e)}\n\n{traceback.format_exc()}"
    
    return render_template_string(
        HTML, 
        relatorio=relatorio, 
        snippet=snippet, 
        repository=repository,
        error=error,
        log=log
    )

if __name__ == "__main__":
    print("🚀 Iniciando servidor Flask na porta 5000...")
    app.run(debug=True, port=5000, host='127.0.0.1')
