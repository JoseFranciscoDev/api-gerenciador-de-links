from urllib.parse import urlencode, urlparse, parse_qs, urlunparse

def build_tracked_url(base_url: str, params: dict) -> str:
    base_url_object = urlparse(base_url)
    base_url_querys_dict = parse_qs(base_url_object.query)
    base_url_querys_dict.update(params)
    base_url_querys_serialized = urlencode(base_url_querys_dict, doseq=True)
    url_final = base_url_object._replace(query=base_url_querys_serialized)
    return urlunparse(url_final)
   
