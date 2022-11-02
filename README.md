# Desafio-Edesoft


![GitHub repo size](https://img.shields.io/github/repo-size/alehkiz/teste_edesoft_backend?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alehkiz/teste_edesoft_backend?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alehkiz/teste_edesoft_backend?style=for-the-badge)
![Github open issues](https://img.shields.io/github/issues/alehkiz/teste_edesoft_backend?style=for-the-badge)


> Ferramenta WEB que faz o upload de um arquivo CSV, trata os dados e em seguida salva todos os dados da planilha, conforme modelo em banco de dados, sendo:
> Desenvolvimento: `SQLite` Produção: `PostgreSQL`

### Melhorias futuras:

- [x] Tratar arquivo CSV
- [x] Permitr mediante configuração a inclusão de arquivos XLS
- [x] Validar o Mimetype do arquivo
- [x] Criar página com tabela, as colunas são informadas de acordo com informado na planilha depara.xlsx em `app/support/depara.xlsx`


## 💻 Pré-requisitos

* `python 3.9.7`
* Utilize um ambiente virtual: https://docs.python.org/3/tutorial/venv.html

## ☕ Usando o sistema local

1. Ative o ambiente virtual;
2. No ambiente virtual, instale as bibliotecas necessárias: `pip install -r requirements.txt`;
3. Configure o arquivo `.env`, o arquivo está configurado para produção. Não esqueça de alterar os dados para o banco de dados PostgreSQL, caso esteja em desenvolvimento, o banco será salvo localmente;
4. Rode o comando `flask db-init` para criar e iniciaro banco de dados;
5. Por fim, rode `flask run` e acesse o seu servidor local;

## ☕ Usando o sistema docker

```
docker-compose -f docker-compose.yml up -d --build
```

Se você estiver no Linux, altere o fim da linha para `LF` no arquivo `entrypoint.sh`

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE) para mais detalhes.

[⬆ Voltar ao topo](#teste_edesoft_backend)<br>
