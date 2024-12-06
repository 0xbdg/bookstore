import midtransclient, os

from dotenv import load_dotenv

load_dotenv()

midtrans_server_key=os.getenv("MIDTRANS_SERVER_KEY")
midtrans_client_key=os.getenv("MIDTRANS_CLIENT_KEY")

core_api = midtransclient.CoreApi(
    is_production=os.getenv("MIDTRANS_PRODUCTION"),
    server_key=midtrans_server_key,
    client_key=midtrans_client_key,
)

# Create Snap API instance
snap = midtransclient.Snap(
    is_production=os.getenv("MIDTRANS_PRODUCTION"),
    server_key=midtrans_server_key,
    client_key=midtrans_client_key
)