import os
import zipfile
import pandas as pd

# Descomprimir el archivo data.zip
with zipfile.ZipFile('data.zip', 'r') as zip_ref:
    zip_ref.extractall('data')

# Función para leer los archivos de texto y crear el DataFrame
# Función para leer los archivos de texto y crear el DataFrame
def create_dataset(directory):
    data = {'phrase': [], 'sentiment': []}
    for sentiment in os.listdir(directory):
        sentiment_dir = os.path.join(directory, sentiment)
        if os.path.isdir(sentiment_dir):  # Ignorar archivos que no son directorios
            for filename in os.listdir(sentiment_dir):
                if not filename.startswith('.'):  # Ignorar archivos ocultos
                    file_path = os.path.join(sentiment_dir, filename)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        phrase = file.read().strip()
                        data['phrase'].append(phrase)
                        data['sentiment'].append(sentiment)
    return pd.DataFrame(data)


# Crear el conjunto de datos de entrenamiento
train_directory = 'data/train'
train_df = create_dataset(train_directory)

# Crear el conjunto de datos de prueba
test_directory = 'data/test'
test_df = create_dataset(test_directory)

# Guardar los conjuntos de datos en archivos CSV
train_df.to_csv('train_dataset.csv', index=False)
test_df.to_csv('test_dataset.csv', index=False)

print("Archivos CSV creados: train_dataset.csv y test_dataset.csv")
