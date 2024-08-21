import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate




def extract_best_worst(div):
    

    mejor_span = div.find('span', text='Lo mejor:')
    peor_span = div.find('span', text='Lo peor:')

    if mejor_span or peor_span:
        lo_mejor = mejor_span.find_next('span').get_text(strip=True) if mejor_span else 'No disponible'
        lo_peor = peor_span.find_next('span').get_text(strip=True) if peor_span else 'No disponible'

        comentario= f'lo mejor: {lo_mejor}, lo peor: {lo_peor}'

    if not mejor_span and not peor_span:
        comentario_div = div.find('div', class_='Text margin-top')
        comentario = comentario_div.get_text(strip=True) if comentario_div else 'No disponible'

    calificacion = sum(1 for img in div.find('div', {'class': 'LeftRightBox__left LeftRightBox__left--noshrink'}).find_all('img') if 'gold' in img['src'])
    
    return {
            'comment': comentario,
            'rating': calificacion
        }


def fetch_reviews(brand, model):

    print(f'Obteniendo reseñas de {brand} {model}...')
    # Formatear la URL usando la marca y el modelo
    url = f'https://www.opinautos.com/co/{brand}/{model}/opiniones'
    
    # Obtener el contenido HTML de la URL
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    
    # Encontrar todos los divs de reseñas
    divs = soup.find_all('div', {'class': 'WhiteCard margin-top desktop-margin15 js-review'})
    
    # Inicializar el DataFrame
    df = pd.DataFrame()
    
    # Procesar cada div y agregar los datos al DataFrame
    for div in divs:
        data = extract_best_worst(div)
        data['name'] = f'{brand} {model}'  # Añadir la columna marca_modelo
        print('vamos bien')
        

        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        print('vamos bien parte 2')

    return df



def summarize_reviews(vehicles):

    llm = Ollama(
    model="llama3.1"
    ) 


    template = """Comentarios: {comentarios}

    Aquí tienes un conjunto de comentarios sobre vehiculo. Genera un resumen coherente y representativo de estos comentarios, destacando los puntos clave y las opiniones más frecuentes. Omite introducciones como acontinuacion, en resumen y demas parecidas, que el resumen sea entre 150 y 200 palabras.
    """

    prompt = ChatPromptTemplate.from_template(template)


    chain = prompt | llm | StrOutputParser()

    summary_dfs = []
    comments_dfs = []


    for brand, model in vehicles:
        df = fetch_reviews(brand, model)
        comments_dfs.append(df)
        
        summary = chain.invoke({"comentarios": '\n'.join([f'• {comentario}' for comentario in df.comment.to_list()])})
        
        summary_df = pd.DataFrame({
            'name':  f'{brand} {model}',
            'summary': [summary],
            'average_rating': [df.rating.mean()]  
        })
        summary_dfs.append(summary_df)


    summary_dfs = pd.concat(summary_dfs, ignore_index=True)
    all_reviews_df = pd.concat(comments_dfs, ignore_index=True)


    return summary_dfs, all_reviews_df

    
    
