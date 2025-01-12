import os

def add_website_to_html():
    # Solicitar detalhes do novo site
    site_url = input("Insere o URL do site: ").strip()
    site_name = input("Insere o nome do website: ").strip()
    screenshot_url = input("Insere o link para o screenshot: ").strip()
    description = input("Insere a descrição do website: ").strip()
    file_name = "index.html"  # Nome do ficheiro HTML a atualizar

    # Verificar se o arquivo HTML existe
    if not os.path.exists(file_name):
        print(f"O arquivo '{file_name}' não existe. Certifique-se de que o nome está correto.")
        return

    # Novo bloco de HTML para o site
    new_site_html = f"""
    <li>
        <a href="{site_url}" target="_blank">
            <img src="{screenshot_url}" alt="{site_name.lower()}">
            <div class="link-info">
                <h2>{site_name}</h2>
                <p>{description}</p>
            </div>
        </a>
    </li>
    """

    # Lendo o conteúdo do arquivo HTML
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.readlines()

    # Encontrando o local correto para adicionar o novo site
    try:
        insert_index = next(i for i, line in enumerate(content) if "</ul>" in line)
    except StopIteration:
        print("Não foi possível encontrar a lista de sites no arquivo HTML.")
        return

    # Inserindo o novo bloco HTML
    content.insert(insert_index, new_site_html)

    # Gravando o conteúdo atualizado de volta ao arquivo
    with open(file_name, "w", encoding="utf-8") as file:
        file.writelines(content)

    print(f"O site '{site_name}' foi adicionado com sucesso ao arquivo '{file_name}'!")

if __name__ == "__main__":
    add_website_to_html()