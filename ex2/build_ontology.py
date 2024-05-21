""" Analisa a ontologia médica:

@prefix : <http://www.example.org/disease-ontology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix swrl: <http://www.w3.org/2003/11/swrl#> .
@prefix swrlb: <http://www.w3.org/2003/11/swrlb#> .

:Ontology a owl:Ontology .

# Classes
:Disease a owl:Class .
:Symptom a owl:Class .
:Treatment a owl:Class .
:Patient a owl:Class .

# Properties
:hasSymptom a owl:ObjectProperty ;
    rdfs:domain :Disease ;
    rdfs:range :Symptom .

:hasTreatment a owl:ObjectProperty ;
    rdfs:domain :Disease ;
    rdfs:range :Treatment .

:exhibitsSymptom a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Symptom .

:hasDisease a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Disease .

:receivesTreatment a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Treatment .

# Disease instances
:Flu a :Disease ;
    :hasSymptom :Fever, :Cough, :SoreThroat ;
    :hasTreatment :Rest, :Hydration, :AntiviralDrugs .

:Diabetes a :Disease ;
    :hasSymptom :IncreasedThirst, :FrequentUrination, :Fatigue ;
    :hasTreatment :InsulinTherapy, :DietModification, :Exercise .

# Symptom instances
:Fever a :Symptom .
:Cough a :Symptom .
:SoreThroat a :Symptom .
:IncreasedThirst a :Symptom .
:FrequentUrination a :Symptom .
:Fatigue a :Symptom .

# Treatment instances
:Rest a :Treatment .
:Hydration a :Treatment .
:AntiviralDrugs a :Treatment .
:InsulinTherapy a :Treatment .
:DietModification a :Treatment .
:Exercise a :Treatment .


# Patient instances
:Patient1 a :Patient ;
    :name "Paul Harrods" ;
    :exhibitsSymptom :Fever ;
    :exhibitsSymptom :Cough ;
    :exhibitsSymptom :SoreThroat .

:Patient2 a :Patient ;
    :name "Ana Montana" ;
    :exhibitsSymptom :IncreasedThirst ;
    :exhibitsSymptom :FrequentUrination ;
    :exhibitsSymptom :Fatigue .


Junto com este enunciado foram disponibilizados 3 datasets em CSV e um em JSON:

- Disease_Syntoms.csv que contem uma lista de doenças e a cada uma associa uma lista de sintomas
Disease,Symptom_1,Symptom_2,...,Symptom_17

- Disease_Description.csv que contem uma lista de pares doença e respetiva descrição: 
Disease,Description

- Disease_Treatment.csv que contem uma lista de doenças e a cada uma associa uma lista de tratamentos:
Disease,Precaution_1,Precaution_2,Precaution_3,Precaution_4

pg54194.json na pasta doentes, que a um nome de doente associa uma lista de sintomas """

# A partir de Disease_Syntoms.csv vais criar instâncias de doença (:Disease) para ca doença;

import csv

def symptoms():
    # open the file
    csv_reader = csv.reader(open("Disease_Syntoms.csv", "r"))
    next(csv_reader)

    # iterate over the rows
    diseases_out = ""
    symptoms_out = ""
    all_symptoms = []

    for row in csv_reader:
        # get the disease name
        disease = row[0]
        disease = disease.strip()
        disease = disease.replace(" ", "_")
        disease = disease.replace("(", "")
        disease = disease.replace(")", "") 
        
        # create the disease instance
        diseases_out += f":{disease} a :Disease ;"
        # get the symptoms
        symptoms = row[1:]
        # iterate over the symptoms
        diseases_out += f"    :hasSymptom "
        # remove empty strings ("")
        symptoms = [symptom for symptom in symptoms if symptom != '']

        for symptom in symptoms[1:-2]:
            symptom = symptom.strip()
            symptom = symptom.replace(" ", "_")
            symptom = symptom.replace("(", "")
            symptom = symptom.replace(")", "") 
            
            # check if the symptom triple was already created
            if symptom not in all_symptoms:
                all_symptoms.append(symptom)
                # create the symptom triple
                symptoms_out += f":{symptom} a :Symptom .\n"
        
            diseases_out += f":{symptom}, "
        
        # add the last symptom (without the comma)
        symptom = symptoms[-1]
        symptom = symptom.strip()
        symptom = symptom.replace(" ", "_")
        symptom = symptom.replace("(", "")
        symptom = symptom.replace(")", "")
        diseases_out += f":{symptom} .\n"

        
    # create the symptoms.ttl -> medical.ttl + diseases_out + symptoms_out
    # read the medical.ttl file


    
    return diseases_out, symptoms_out
    
    
def descr():    
    # A partir de Disease_Description.csv vais adicionar a cada doença uma descrição (:Disease, rdfs:comment "Description");
    csv_reader = csv.reader(open("Disease_Description.csv", "r"))
    next(csv_reader)

    descrip_out = ""
    # iterate over the rows
    for row in csv_reader:
        # get the disease name
        disease = row[0]
        disease = disease.strip()
        disease = disease.replace(" ", "_")
        disease = disease.replace("(", "")
        disease = disease.replace(")", "") 
        
        descr = row[1]
        descr = descr.strip()
        descr = descr.replace("\"", "'")
        # create the disease instance
        descrip_out += f":{disease} rdfs:comment \"{descr}\" .\n"

    return descrip_out

def treat():
    # A partir de Disease_Treatment.csv vais adicionar a cada doença uma lista de tratamentos (:Disease, :hasTreatment);
    csv_reader = csv.reader(open("Disease_Treatment.csv", "r"))
    next(csv_reader)

    treat_out = ""
    # iterate over the rows
    for row in csv_reader:
        # get the disease name
        disease = row[0]
        disease = disease.strip()
        disease = disease.replace(" ", "_")
        disease = disease.replace("(", "")
        disease = disease.replace(")", "") 
        
        # create the disease instance
        treat_out += f":{disease} :hasTreatment "
        # get the treatments
        treatments = row[1:]
        # iterate over the treatments
        for treatment in treatments[:-1]:
            treatment = treatment.strip()
            treatment = treatment.replace(" ", "_")
            treatment = treatment.replace("(", "")
            treatment = treatment.replace(")", "") 
            treat_out += f":{treatment}, "
        
        # add the last treatment (without the comma)
        treatment = treatments[-1]
        treatment = treatment.strip()
        treatment = treatment.replace(" ", "_")
        treatment = treatment.replace("(", "")
        treatment = treatment.replace(")", "")
        treat_out += f":{treatment} .\n"
        
    return treat_out

import json

def patients(file_path):
    
    json_reader = json.load(open(file_path, "r"))
    patients_out = ""
    
    for i, patient in enumerate(json_reader):
        name = patient["nome"]
        symptoms = patient["sintomas"] # list of symptoms
        
        # create the patient instance
        patients_out += f":p{i} a :Patient ;"
        patients_out += f"    :name \"{name}\" ;"
        if len(symptoms) > 0:
            patients_out += f"    :exhibitsSymptom "
            for symptom in symptoms[:-1]:
                symptom_clean = symptom.strip()
                symptom_clean = symptom_clean.replace(" ", "_")
                symptom_clean = symptom_clean.replace("(", "")
                symptom_clean = symptom_clean.replace(")", "")
                patients_out += f":{symptom_clean}, "
            # add the last symptom (without the comma)
            symptom = symptoms[-1]
            symptom_clean = symptom.strip()
            symptom_clean = symptom_clean.replace(" ", "_")
            symptom_clean = symptom_clean.replace("(", "")
            symptom_clean = symptom_clean.replace(")", "")
            patients_out += f":{symptom_clean} .\n"
        
    return patients_out

def main():
    #diseases_out, symptoms_out = symptoms()
    #descriptions = descr()
    #treatments = treat()
    patients_out = patients("pg54194.json")
    
    # open medical.ttl
    with open("medical.ttl", "r") as file:
        medical = file.read()
        
    # write the new file
    #with open("symptoms.ttl", "w") as file:
    #    file.write(medical + diseases_out + symptoms_out)
    
    # write the new file (descriptions.ttl)
    #with open("descriptions.ttl", "w") as file:
    #    file.write(medical + diseases_out + symptoms_out + descriptions)
    
    # write the new file (treatments.ttl)
    #with open("treatments.ttl", "w") as file:
    #    file.write(medical + treatments)
    
    # write the new file (patients.ttl)
    with open("patients.ttl", "w") as file:
        file.write(medical + patients_out)

if __name__ == "__main__":
    main()
    