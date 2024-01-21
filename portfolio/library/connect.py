from google.oauth2.credentials import Credentials
from typing import Optional
from pandas import DataFrame
from portfolio.library.datatypes import PortfolioBlog

def content_from_uri(
    uri:str,
    credentials:Optional[Credentials]=None)->bytes:

    from portfolio.library.utils import bucket_info_from_gs_path
    from google.cloud.storage import Client
    from ast import literal_eval

    # Connect to cloud storage
    if credentials is not None:
        token = literal_eval(credentials.to_json())['token']
        bucket_client = Client.from_service_account_json(token)
    else:
        bucket_client = Client()

    # Bucket info from gs string
    bucket_name, bucket_file = bucket_info_from_gs_path(uri)
    
    # Get content from bucket
    bucket = bucket_client.get_bucket(bucket_name)
    blob = bucket.blob(bucket_file)
    content = blob.download_as_bytes()
    # Close
    bucket_client.close()
    return content


def image_from_file_bytes(
    content:bytes,
    img_type:str='png')->str:

    from base64 import b64encode

    encoded_image = b64encode(content).decode('utf-8')

    if img_type == 'png':
        src='data:image/png;base64,{}'.format(encoded_image)

    return src


def png_from_uri(
    uri:str,
    credentials:Optional[Credentials]=None)->str:

    content = content_from_uri(uri,credentials)
    image = image_from_file_bytes(content)
    return image


def table_from_bigquery(
    query:str,
    credentials:Optional[Credentials]=None,
    dataframe:bool=True)->DataFrame:

    from google.cloud.bigquery.client import Client
    
    # Connect to BigQuery
    if credentials is not None:
        bq_client = Client(credentials=credentials)
    else:
        bq_client = Client()

    # Submit query
    table = bq_client.query(query)

    # Convert to dataframe
    if dataframe:
        table = table.to_dataframe()

    # Close to not overload connections
    bq_client.close()
    return table


def upload_portfolio_blog(
    portfolio_blog:PortfolioBlog,
    location:str,
    table_name:str,
    dataset_name:str,
    project_id:str,
    append:bool=True,
    credentials:Optional[Credentials]=None):

    from google.cloud import bigquery

    # Create dataframe from Portfolio Blog
    blog_df = portfolio_blog.to_dataframe()

    # 
    client = bigquery.Client(
        credentials=credentials,
        project=project_id
    )

    # Define your table ID (dataset.table_name)
    table_id = f'{project_id}.{dataset_name}.{table_name}'

    # Append or write new table
    write_disposition="WRITE_TRUNCATE"
    if append:
        write_disposition="WRITE_APPEND"

    # Specify a (partial) schema. All columns are always written.
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("blog_id", bigquery.enums.SqlTypeNames.INTEGER),
            bigquery.SchemaField("blog_title", bigquery.enums.SqlTypeNames.STRING),
            bigquery.SchemaField("blog_date", bigquery.enums.SqlTypeNames.DATETIME),
            bigquery.SchemaField("blog_abstract", bigquery.enums.SqlTypeNames.STRING),
            bigquery.SchemaField("blog_markdown", bigquery.enums.SqlTypeNames.STRING),
            bigquery.SchemaField("blog_image", bigquery.enums.SqlTypeNames.STRING),
            bigquery.SchemaField("blog_image_source", bigquery.enums.SqlTypeNames.STRING),
            bigquery.SchemaField("tag_id", bigquery.enums.SqlTypeNames.INTEGER),
        ],
        write_disposition=write_disposition,
    )

    # If the table does not exist, it will be created. If it exists, it will be replaced/updated based on the if_exists parameter
    job = client.load_table_from_dataframe(
        blog_df, 
        table_id, 
        job_config=job_config,
        location=location,
        project=project_id
    )

    # Wait for the load job to complete.
    job.result()

    # Close connection
    client.close()
    return