import requests
import psycopg2

# Conexão com o banco de dados
db_params = {
    'host': 'localhost',
    'database': 'correios',
    'user': 'postgres',
    'password': 'admin12345'
}

# URL da API dos Correios para consultar CEP
api_url = "https://viacep.com.br/ws/{}/json/"


def obter_dados_cep(cep):
    try:
        url = api_url.format(cep)
        response = requests.get(url)
        data = response.json()
        if "erro" in data:
            print(f"CEP {cep} não encontrado na API dos Correios.")
            return None
        return data
    except requests.RequestException as e:
        print(f"Erro na requisição à API dos Correios para o CEP {cep}: {e}")
        return None


def conectar_postgresql():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ceps (
                id SERIAL PRIMARY KEY,
                cep VARCHAR(10) NOT NULL,
                logradouro VARCHAR(255) NOT NULL,
                bairro VARCHAR(100) NOT NULL,
                localidade VARCHAR(100) NOT NULL,
                uf VARCHAR(2) NOT NULL
            )
        """)
        conn.commit()
        return conn, cursor
    except psycopg2.Error as e:
        print("Erro ao conectar ou criar a tabela:", e)
        raise


def fechar_conexao(conn, cursor):
    cursor.close()
    conn.close()


def salvar_todos_ceps(conn, cursor, cep_inicial, cep_final):
    try:
        for cep in range(cep_inicial, cep_final + 1):
            cep_str = str(cep).zfill(8)  # Preenche o CEP com zeros à esquerda
            dados = obter_dados_cep(cep_str)
            if dados:
                cursor.execute("""
                    INSERT INTO ceps (cep, logradouro, bairro, localidade, uf)
                    VALUES (%s, %s, %s, %s, %s)
                """, (dados["cep"], dados["logradouro"], dados["bairro"], dados["localidade"], dados["uf"]))
        conn.commit()
        print("Todos os CEPs foram salvos no banco de dados.")
    except psycopg2.Error as e:
        print("Erro ao inserir dados no PostgreSQL:", e)


def main():
    # Warning: Não insira uma faixa muito grande de CEPs, pois a API dos Correios pode bloquear o seu IP.
    cep_inicial = 0 # Substitua pelo CEP inicial da faixa
    cep_final = 0  # Substitua pelo CEP final da faixa
    conn, cursor = conectar_postgresql()
    salvar_todos_ceps(conn, cursor, cep_inicial, cep_final)
    fechar_conexao(conn, cursor)


if __name__ == "__main__":
    main()
