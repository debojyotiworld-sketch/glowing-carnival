import supabase
import http.server

def get_supabase_client():
    url = "https://your-supabase-url.supabase.co"
    key = "your-supabase-key"
    client = supabase.create_client(url, key)
    return client

