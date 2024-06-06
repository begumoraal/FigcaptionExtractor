from bs4 import BeautifulSoup

def extract_figcaption(html_content):
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    figcaptions = soup.find_all('figcaption')
    
    captions = [figcaption.get_text() for figcaption in figcaptions]
    
    return "\n".join(captions) if captions else "" 

file_path = r'C:\Users\begum\Desktop\test.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

captions = extract_figcaption(html_content)

output_file_path = r'C:\Users\begum\Desktop\captions.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(captions)

print(f'Captions have been written to {output_file_path}')
