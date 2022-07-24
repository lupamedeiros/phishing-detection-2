# Phishing Detection 2.0
A new aproach for the Phishing Detection project.

## Creating the Model

The projects initial steps run on Google Colab. In order to run it, download the
content in source/creating_model and upload it to your google colaboratory.

## Setting up the environment

In this project we use Anaconda to manage the local environment, in order to
create and user the correct environment, do as told bellow.

    conda env create --file environment.yml
    conda activate phishing-detection-2
    pip install -r requirements.txt

To exit the envoriment:

    conda deactivate

To run the API:

    uvicorn source.api.main:app --reload