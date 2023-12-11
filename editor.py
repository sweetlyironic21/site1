import os
import random
from bs4 import BeautifulSoup

def reshuffle_sentences(text):
    # Split the text into sentences
    sentences = text.split('. ')
    
    # Shuffle the sentences
    random.shuffle(sentences)
    
    # Join the shuffled sentences back into text
    shuffled_text = '. '.join(sentences)
    
    return shuffled_text

def edit_html_file(file_path, new_folder_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Narrow down the search to specific elements (adjust as needed)
    p_tags = soup.find_all('p')

    for p_tag in p_tags:
        # Check if p_tag.string is not None before manipulating it
        if p_tag.string:
            p_tag.string.replace_with(reshuffle_sentences(p_tag.string))

    # Find all 'a' tags
    a_tags = soup.find_all('a')

    # Change the first and second 'a' tags to link to random HTML files
    for i, a_tag in enumerate(a_tags):
        if i == 0 or i == 1:
            random_html_file = random.choice(os.listdir(new_folder_path))
            a_tag['href'] = os.path.join(random_html_file)
        else:
            # Remove other 'a' tags
            a_tag.decompose()

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
