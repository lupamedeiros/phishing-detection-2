"""
Creator: Luiz Paulo de Souza Medeiros
Date: Jul 24, 2022
Create the API for phishing detection 2.0
"""

from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import pandas as pd
import joblib
import os
import wandb
import sys
from source.api.model import df_to_dataset, get_normalization_layer

# name of the model artifact
artifact_model_name = "phishing-detection-2/model_export:latest"

# initiate teh wandb project
run = wandb.init(project="phishing-detection-2",job_type="api")

# Create the API

app = FastAPI()

# Declare the request example data using pydantic
# a url in ou dataset has the following attributes
class Url(BaseModel):
    url: object 
    length_url: int  
    length_hostname: int
    ip: int
    nb_dots: int
    nb_hyphens: int
    nb_at: int
    nb_qm: int  
    nb_and: int  
    nb_or: int  
    nb_eq: int
    nb_underscore: int
    nb_tilde: int
    nb_percent: int
    nb_slash: int  
    nb_star: int
    nb_colon: int
    nb_comma: int
    nb_semicolumn: int
    nb_dollar: int
    nb_space: int
    nb_www: int
    nb_com: int
    nb_dslash: int
    http_in_path: int
    https_token: int
    ratio_digits_url: float
    ratio_digits_host: float
    punycode: int
    port: int
    tld_in_path: int
    tld_in_subdomain: int
    abnormal_subdomain: int
    nb_subdomains: int
    prefix_suffix: int
    random_domain: int
    shortening_service: int
    path_extension: int
    nb_redirection: int
    nb_external_redirection: int
    length_words_raw: int
    char_repeat: int
    shortest_words_raw: int
    shortest_word_host: int
    shortest_word_path: int
    longest_words_raw: int
    longest_word_host: int
    longest_word_path: int
    avg_words_raw: float
    avg_word_host: float
    avg_word_path: float
    phish_hints: int
    domain_in_brand: int
    brand_in_subdomain: int
    brand_in_path: int
    suspecious_tld: int
    statistical_report: int
    nb_hyperlinks: int
    ratio_intHyperlinks: float
    ratio_extHyperlinks: float
    ratio_nullHyperlinks: int
    nb_extCSS: int
    ratio_intRedirection: int
    ratio_extRedirection: float
    ratio_intErrors: int
    ratio_extErrors: float
    login_form: int
    external_favicon: int
    links_in_tags: float
    submit_email: int
    ratio_intMedia: float
    ratio_extMedia: float
    sfh: int
    iframe: int
    popup_window: int
    safe_anchor: float
    onmouseover: int
    right_clic: int
    empty_title: int
    domain_in_title: int
    domain_with_copyright: int
    whois_registered_domain: int
    domain_registration_length: int
    domain_age: int
    web_traffic: int
    dns_record: int
    google_index: int
    page_rank: int

    class Config:
        schema_extra = {
            "example": {
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
        }

# Greetings using GET
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <p><span style="font-size:28px"><strong>Hello World<strong></span></p>
    <p><span style="font-size:20px">In this project, we will apply the skills
        acquired in the Deployng a Scalable ML Pipeline in Production course to develop
        a classification model on publicly available
        <a href="https://data.mendeley.com/datasets/c2gw7fy2j4/3> Mendeley Data</a>.</span></p>
    <p><span style="font-size:20px">Source code available on
        <a href="https://github.com/lupamedeiros/phishing-detection-2>github/lupamedeiros/phishing-detection-2</a>.</span></p>
    <p><span style="font-size:20px">More info available on 
        <a href="https://github.com/lupamedeiros/phishing-detection-2>Medium article.</a>.</span></p>
    """

# run the model inferece and use a Url data structure via POST to the API
@app.post("/predict")
async def get_inference(url: Url):
    # Download inferecen artifact
    model_export_path = run.use_artifact(artifact_model_name).file()
    model = joblib.load(model_export_path)

    # create a dataframe from the input feature
    # note that we could use pd.DataFrame.from_dict
    # but due be only one instance, it would be necessary to pass the Index
    df = pd.DataFrame([url.dict()])
    ds = df_to_dataset(df,shuffle=False)

    predict = model.predict(ds)  

    return "legitm" if predict[0] <= 0.5 else "phishing"