from crewai_tools import ScrapeWebsiteTool
from collections import Counter
from string import punctuation
import requests
from langchain_community.tools import tool

class SearchTools():
  def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            tool = ScrapeWebsiteTool()
            tool = ScrapeWebsiteTool(website_url= url)
            result = tool.run()
            print("\n\n########################")
            print("## Here is your result:")
            print("########################\n")
            print(result)
        else:
            print(f"Failed to fetch {url}: Status code {response.status_code}")
    except Exception as e:
        print(f"Error occurred while scraping {url}: {e}")

  def web_scrapper(txt):
    urls = []
    while True:
        url = input("Enter a URL to scrape (or type 'done' to finish): ")
        if url.lower() == 'done':
            break
        urls.append(url)

    print("\nScraping websites...\n")
    for url in urls:
            SearchTools.scrape_website(url)
            print()

# class CleanDataTools():    
    
#     def preprocess_text(text):
#       text= text.lower()
#       text= re.sub(r'/d+', "", text)
#       text = re.sub(r'[^\w\s]',"",text)
#       tokens = nltk.word_tokenize(text)
#       return tokens
    
#     def remove_stopwords(tokens):
#       stop_words= set(stopwords.words('english'))
#       filtered_tokens = [word for word in tokens if word not in stop_words]
#       return filtered_tokens
    
#     def perform_lemmatization(tokens):
#       lemmatizer = nltk.WordNetLemmatizer()
#       lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
#       return lemmatized_tokens
    
#     @tool("CleanData")
#     def clean_text(text):
#       tokens = CleanDataTools.preprocess_text(text)
#       filtered_tokens =CleanDataTools.perform_lemmatization(filtered_tokens)
#       lemmatized_tokens = CleanDataTools.perform_lemmatization(filtered_tokens)
#       clean_text = ' '.join(lemmatized_tokens)
#       return clean_text
  

# nlp = spacy.load("en_core_web_sm")



# class KeywordsAndEntities:
#    def get_hotwords(text):
#     result = []
#     pos_tag = ['PROPN', 'ADJ', 'NOUN'] 
#     doc = nlp(text.lower()) 
#     for token in doc:
#         if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
#             continue
#         if(token.pos_ in pos_tag):
#             result.append(token.text)
#     return result