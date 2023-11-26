import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Authenticate
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = "1gr17gLNrJfqnUIWBsUdyCt2W0L64Bq7c"

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_file(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    # Create metadata
    file_metadata = {
        'name': "comments_and_ratings.csv",
        'parents': [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()

upload_file("comments_and_ratings.csv")


# data_file = '/content/drive/MyDrive/For_Colab/reviews.csv'

# # Load the CSV data into a pandas DataFrame
# data = pd.read_csv(data_file, delimiter=',')

# # Remove irrelevant columns
# data = data.drop(['ReviewId', 'RecipeId', 'AuthorId', 'AuthorName', 'DateSubmitted', 'DateModified'], axis=1)

# # Handle missing values
# data.dropna(subset=['Rating', 'Review'], inplace=True)

# # Text preprocessing
# data['Review'] = data['Review'].str.lower()
# data['Review'] = data['Review'].str.replace('[^\w\s]', '')
# data['Review'] = data['Review'].str.split().str.join(' ')

# # Data partitioning
# from sklearn.model_selection import train_test_split

# train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
