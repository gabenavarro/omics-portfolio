from google.oauth2.credentials import Credentials


def info_from_credentials(
    credentials:Credentials,
    info:str)->str:
    import json
    import io

    assert_items  = [
        'type',
        'project_id',
        'private_key_id',
        'private_key',
        'client_email',
        'client_id',
        'auth_uri',
        'token_uri',
        'auth_provider_x509_cert_url',
        'client_x509_cert_url',
        'universe_domain'
    ]

    assert info in assert_items, f'Error, info {info} not in {assert_items}'

    # Get token path from credentials
    token = credentials.to_json()
    with io.open(token['token'], "r", encoding="utf-8") as json_file:
        # Read token as json
        data = json.load(json_file)

    # Return json
    return data[info]


def bucket_info_from_gs_path(
    gs_path:str):

    if not gs_path.startswith("gs://"):
        raise ValueError(f"gs_path needs to start gs://\n{gs_path}")
    
    gs_path = gs_path.replace("gs://","").split('/',1)
    bucket_name = gs_path[0]
    bucket_file = gs_path[-1]
    return bucket_name, bucket_file
