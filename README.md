🍿 Movie Recommendation API & Chatbot
Esta es una API construida con FastAPI que permite explorar un catálogo de películas de Netflix y consultar recomendaciones mediante un Chatbot con procesamiento de lenguaje natural (NLP) básico utilizando sinonimia.

🚀 Características
Listado Completo: Acceso a todo el catálogo de películas.

Búsqueda por ID: Obtención de detalles específicos de un título.

Filtro por Categoría: Endpoint dedicado para filtrar géneros.

Chatbot Inteligente: Búsqueda basada en palabras clave y sinónimos (gracias a NLTK y WordNet).

Documentación Automática: Generada por Swagger UI.

🛠️ Requisitos Previos
Antes de empezar, asegúrate de tener instalado:

Python 3.8 o superior.

Pip (gestor de paquetes de Python).

📦 Instalación
Clona este repositorio (o descarga los archivos):

Bash
git clone https://github.com/tu-usuario/movie-api-chatbot.git
cd movie-api-chatbot
Crea un entorno virtual (Recomendado):

Bash
python -m venv venv
# Actívalo en Windows:
.\venv\Scripts\activate
# Actívalo en Mac/Linux:
source venv/bin/activate
Instala las dependencias:

Bash
pip install fastapi uvicorn pandas nltk
Configura el Dataset:
Asegúrate de tener el archivo netflix_titles.csv dentro de una carpeta llamada Dataset/ en la raíz del proyecto.

🚦 Ejecución
Para poner en marcha el servidor, utiliza el siguiente comando:

Bash
python -m uvicorn main:app --reload
Nota: Sustituye main por el nombre de tu archivo .py si es distinto.

Una vez ejecutado, abre tu navegador en:

API: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Documentación Interactiva (Swagger): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

🤖 Uso del Chatbot
El endpoint /chatbot acepta una consulta en texto plano. El sistema buscará coincidencias no solo por la palabra exacta, sino también por sus sinónimos.

Ejemplo de consulta:
GET /chatbot?query=flicks
(Esto podría devolver resultados de la categoría "Movies" aunque no hayas escrito la palabra exacta).

🛠️ Tecnologías Utilizadas
FastAPI: Framework web de alto rendimiento.

Pandas: Manipulación y limpieza de datos del CSV.

NLTK: Procesamiento de lenguaje natural para el manejo de sinónimos.

Uvicorn: Servidor ASGI para la ejecución de la API.

📝 Notas de configuración
Si estás en Windows, recuerda verificar la ruta de datos de NLTK en el código:

Python
nltk.data.path.append(r'C:\Tu\Ruta\Personalizada')
