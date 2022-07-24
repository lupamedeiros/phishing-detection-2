"""
Creator: Luiz Paulo de Souza Medeiros
Date: Jul 24, 2022
API testing
"""

from fastapi.testclient import TestClient
import os
import sys
import pathlib
from source.api.main import app

# Instantiate the testing client with our app
client = TestClient(app)

# a unit test that testes the status code of the root path
def test_root():
    r = client.get("/")
    assert r.status_code == 200

# a unit test that tests the status code and response for
# an instance with legitm url
def test_get_inference_legitm():
    url = {
        "url": "http://www.crestonwood.com/router.php",
        "length_url": 37,
        "length_hostname": 19,
        "ip": 0,
        "nb_dots": 3,
        "nb_hyphens": 0,
        "nb_at": 0,
        "nb_qm": 0,
        "nb_and": 0,
        "nb_or": 0,
        "nb_eq": 0,
        "nb_underscore": 0,
        "nb_tilde": 0,
        "nb_percent": 0,
        "nb_slash": 3,
        "nb_star": 0,
        "nb_colon": 1,
        "nb_comma": 0,
        "nb_semicolumn": 0,
        "nb_dollar": 0,
        "nb_space": 0,
        "nb_www": 1,
        "nb_com": 0,
        "nb_dslash": 0,
        "http_in_path": 0,
        "https_token": 1,
        "ratio_digits_url": 0.0,
        "ratio_digits_host": 0.0,
        "punycode": 0,
        "port": 0,
        "tld_in_path": 0,
        "tld_in_subdomain": 0,
        "abnormal_subdomain": 0,
        "nb_subdomains": 3,
        "prefix_suffix": 0,
        "random_domain": 0,
        "shortening_service": 0,
        "path_extension": 0,
        "nb_redirection": 0,
        "nb_external_redirection": 0,
        "length_words_raw": 4,
        "char_repeat": 4,
        "shortest_words_raw": 3,
        "shortest_word_host": 3,
        "shortest_word_path": 3,
        "longest_words_raw": 11,
        "longest_word_host": 11,
        "longest_word_path": 6,
        "avg_words_raw": 5.75,
        "avg_word_host": 7.0,
        "avg_word_path": 4.5,
        "phish_hints": 0,
        "domain_in_brand": 0,
        "brand_in_subdomain": 0,
        "brand_in_path": 0,
        "suspecious_tld": 0,
        "statistical_report": 0,
        "nb_hyperlinks": 17,
        "ratio_intHyperlinks": 0.529411765,
        "ratio_extHyperlinks": 0.470588235,
        "ratio_nullHyperlinks": 0,
        "nb_extCSS": 0,
        "ratio_intRedirection": 0,
        "ratio_extRedirection": 875,
        "ratio_intErrors": 0,
        "ratio_extErrors": 0.5,
        "login_form": 0,
        "external_favicon": 0,
        "links_in_tags": 80.0,
        "submit_email": 0,
        "ratio_intMedia": 100.0,
        "ratio_extMedia": 0.0,
        "sfh": 0,
        "iframe": 0,
        "popup_window": 0,
        "safe_anchor": 0.0,
        "onmouseover": 0,
        "right_clic": 0,
        "empty_title": 0,
        "domain_in_title": 0,
        "domain_with_copyright": 1,
        "whois_registered_domain": 0,
        "domain_registration_length": 45,
        "domain_age": -1,
        "web_traffic": 0,
        "dns_record": 1,
        "google_index": 1,
        "page_rank": 4
    }
    r = client.post("/predict",json=url)

    assert r.status_code == 200
    assert r.json() == "legitm"