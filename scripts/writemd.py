from bs4 import BeautifulSoup

def html_to_markdown():
    input_file = "index.html"  # Arquivo HTML de entrada
    output_file = "websites.md"  # Arquivo Markdown de saída

    try:
        # Ler o conteúdo do arquivo HTML
        with open(input_file, "r", encoding="utf-8") as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"O arquivo '{input_file}' não foi encontrado. Certifique-se de que está no diretório correto.")
        return

    # Ler o conteúdo do arquivo Markdown existente (se houver)
    try:
        with open(output_file, "r", encoding="utf-8") as file:
            existing_markdown = file.read()
    except FileNotFoundError:
        existing_markdown = ""  # Se o arquivo não existir, consideramos vazio

    # Usar BeautifulSoup para processar o HTML
    soup = BeautifulSoup(html_content, "html.parser")
    sites = soup.find_all("li")  # Encontrar todos os itens de lista (<li>)

    if not sites:
        print("Nenhum site encontrado no arquivo HTML.")
        return

    # Construir o conteúdo Markdown
    new_sites = ""
    existing_links = [
        line.split("[aqui](")[1].split(")")[0]
        for line in existing_markdown.splitlines()
        if "[aqui](" in line
    ]

    idx = len(existing_links) + 1  # Começa a numeração após os existentes
    for site in sites:
        link_tag = site.find("a", href=True)
        img_tag = site.find("img", src=True)
        info_div = site.find("div", class_="link-info")

        if link_tag and img_tag and info_div:
            # Extração de dados
            site_url = link_tag["href"]
            screenshot_url = img_tag["src"]
            site_name = info_div.find("h2").get_text(strip=True) if info_div.find("h2") else "Sem Nome"
            description = info_div.find("p").get_text(strip=True) if info_div.find("p") else "Sem descrição"

            # Verificar se o site já existe no Markdown
            if site_url not in existing_links:
                # Formatar o conteúdo em Markdown
                new_sites += f"{idx}. **{site_name}**\n\n"
                new_sites += f"   - {description} Clica [aqui]({site_url}).  \n"
                new_sites += f"     ![]({screenshot_url})\n\n"
                idx += 1

    if new_sites:
        # Adicionar novos sites ao Markdown existente
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(new_sites)
        print(f"Novos sites foram adicionados ao arquivo '{output_file}'.")
    else:
        print("Nenhum novo site para adicionar.")

if __name__ == "__main__":
    html_to_markdown()