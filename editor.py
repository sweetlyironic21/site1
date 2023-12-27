import os
import random
from bs4 import BeautifulSoup

def edit_html_file(file_path, new_folder_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the main 'p' tag containing all sentences
    main_p_tag = soup.find('p')

    if main_p_tag:
        # Split the content of the main 'p' tag into sentences
        sentences = main_p_tag.get_text().split('. ')

        # Shuffle the list of available HTML files
        html_files = os.listdir(new_folder_path)
        random.shuffle(html_files)

        # Convert 18 random sentences into 'a' tags
        selected_sentences = random.sample(sentences, min(18, len(sentences)))

        for i, sentence in enumerate(selected_sentences):
            # Create a new 'a' tag
            new_a_tag = soup.new_tag("a", href=os.path.join(html_files[i]))
            new_a_tag.string = sentence.strip()  # Use the original sentence as anchor text

            # Append the new 'a' tag within the main 'p' tag
            main_p_tag.append(new_a_tag)

    # Remove all <li> tags
    li_tags = soup.find_all('li')
    for li_tag in li_tags:
        li_tag.decompose()

    # Append Google Tag Manager code
    gtag_code = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-BHLC8B3GE4"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-BHLC8B3GE4');
    </script>
    """

    # Append the gtag_code to the end of the HTML body
    body_tag = soup.body
    if body_tag:
        body_tag.append(BeautifulSoup(gtag_code, 'html.parser'))

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

if __name__ == "__main__":
    # Specify the paths to the "blog" and "new" folders
    blog_folder_path = "blog"
    new_folder_path = "blog"

    for filename in os.listdir(blog_folder_path):
        if filename.endswith(".html"):
            file_path = os.path.join(blog_folder_path, filename)
            edit_html_file(file_path, new_folder_path)
            print(f"Processed: {filename}")
