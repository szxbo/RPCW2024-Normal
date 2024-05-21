# Ficha rpcw2024-normal
# Avaliação: Representação e Processamento de Conhecimento na Web
## 21 de Maio de 2023, 16h, Ed.1 - sala 1.25
### Mestrado em Engenharia Informática (1º ano)
## Sinopsis

O objectivo principal deste teste é avaliar os conhecimentos obtidos durante as aulas na especificação e desenvolvimento de ontologias e de aplicações que tiram partido destas.

Antes de começares, lê atentamente até ao fim para ficares com uma percepção do todo que se pretende. 
Vais ver que tomarás decisões mais acertadas depois de uma leitura completa.

Os resultados finais deverão ser enviados ao docente da seguinte forma:
* Enviar por email para: `jcr@di.uminho.pt`;
* Colocar no subject/assunto: `RPCW2024::Normal::Axxxxx`, em que `Axxxxx` corresponde ao número do aluno;
* Enviar ao docente um link do github para um repositório novo criado especificamente para o exame com o seguinte conteúdo (esta preparação poderá valer 1 valor do exame):
    * O repositório no GitHub deverá chamar-se `RPCW2024-Normal`;
    * Dentro do repositório deverá haver um ficheiro, `PR.md`, contendo uma descrição do que fez e como fez, contendo instruções se necessário, para o docente poder replicar os cenários na correção.
    * Dentro do repositório deverão existir duas pastas: `ex1`, onde colocarão a aplicação desenvolvida para responder ao primeiro exercício e, `ex2`, onde colocarão a aplicação desenvolvida para responder ao segundo exercício.

## Exercício 1: Vamos extrair conhecimento de uma história 

Neste exercício, deverás especificar uma ontologia OWL, podes usar o `Protégé`, para a história abaixo e os requisitos que lhe seguem.

### História

> O Sr. João é um agricultor que vive na vila de São José. Ele possui uma pequena fazenda onde cultiva vários tipos de frutas, como maçãs, laranjas e bananas. Na sua fazenda, ele também cria alguns animais, incluindo vacas, galinhas e porcos.
>
> A esposa do Sr. João, a Sra. Maria, ajuda na colheita e na alimentação dos animais. Além disso, ela faz geleias de frutas para vender na feira local. Eles têm dois filhos, Pedro e Ana. Pedro gosta de ajudar o pai com os animais, enquanto Ana prefere ajudar a mãe a fazer as geleias.
>
> O Sr. João tem um vizinho chamado Sr. Carlos, que possui uma fazenda maior onde cultiva principalmente vegetais, como tomates, alfaces e cenouras. O Sr. Carlos frequentemente troca vegetais por frutas com o Sr. João. Ambos também vendem seus produtos na feira de São José todos os sábados.
>
> A fazenda do Sr. João tem um cachorro chamado Rex, que protege a propriedade. A família também possui um trator que é usado para arar os campos e plantar as sementes.
>
> Durante a estação de colheita, o Sr. João contrata trabalhadores temporários para ajudar na colheita das frutas. Esses trabalhadores são pagos por hora e recebem refeições durante o trabalho.

### A Ontologia (3 val.)

Especifica agora a ontologia que dê suporte ao conhecimento nesta história:
1. Define as Classes;
2. Define os atributos de cada Classe (`data properties`);
3. Define as relações que se podem estabelecer entre indivíduos da mesma classe ou de classes diferentes (`object properties`);
4. Cria os indivíduos com os seus atributos e as suas relações;
5. Deixa a ontologia num ficheiro TTL: `historia.ttl`.

### As Queries (2 val. = 0.4 * 5)

Adicionalmente especifica queries em SPARQL para responder às seguintes questões (coloca as queries, devidamente identificadas, num ficheiro de texto designado por `queries.txt`):
1. Quantas classes estão definidas na Ontologia?
2. Quantas `Object Properties` estão definidas na Ontologia?
3. Quantos indivíduos existem na tua ontologia?
4. Quem planta tomates?
5. Quem contrata trabalhadores temporários?


## Exercício 2: Era uma vez... uma ontologia médica... (15 val.)

```ttl
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
    :name "Paul Harrods"
    :exhibitsSymptom :Fever ;
    :exhibitsSymptom :Cough ;
    :exhibitsSymptom :SoreThroat .

:Patient2 a :Patient ;
    :name "Ana Montana"
    :exhibitsSymptom :IncreasedThirst ;
    :exhibitsSymptom :FrequentUrination ;
    :exhibitsSymptom :Fatigue .
```

Analisa a ontologia médica acima (está disponível no ficheiro `medical.ttl`) e sobre ela realiza as seguintes operações:

Junto com este enunciado foram disponibilizados 3 datasets em CSV e um em JSON:
- `Disease_Syntoms.csv` que contem uma lista de doenças e a cada uma associa uma lista de sintomas;
- `Disease_Description.csv` que contem uma lista de pares: doença e respetiva descrição;
- `Disease_Treatment.csv` que contem uma lista de doenças e a cada uma associa uma lista de tratamentos;
- `pgXXXXX.json` na pasta `doentes`, que a um nome de doente associa uma lista de sintomas (**atenção: há um dataset diferente para cada aluno, usa o que tem o teu número**).

Vais usar estes datasets para povoar a ontologia da seguinte forma:
1. `[0.5 val.]` A partir de `Disease_Syntoms.csv` vais criar instâncias de doença (`:Disease`) para cada doença;
2. `[1 val.]` Para os sintomas de cada doença vais criar uma instância para cada sintoma se esta ainda não existir;
3. `[1 val.]` Vais associar cada doença criada aos respetivos sintomas;
4. `[1 val.]` A partir de `Disease_Description.csv` vais associar uma descrição a cada doença (cria esta nova propriedade);
5. `[0.4 val.]` Depois destas alterações, coloca a ontologia na pasta `ex2` com nome `med_doencas.ttl`;
6. `[0.5 val.]` A partir de `Disease_Treatment.csv` vais criar uma instância para cada tratamento se esta ainda não existir;
7. `[1 val.]` Vais associar cada doença criada aos respetivos tratamentos;
8. `[0.2 val.]` Depois destas alterações, coloca a ontologia na pasta `ex2` com nome `med_tratamentos.ttl` (é sempre o resultado cumulativo de todas as alterações feitas até ao momento);
9. `[2 val.]` A partir de `pgXXXXX.json` que está na pasta `doentes` vais criar as instâncias dos doentes: um doente deverá ter um id (usa a tua imaginação), um nome (extraído do dataset) e uma lista de sintomas associados (extraídos do dataset);
10. `[0.4 val.]` Depois destas alterações, coloca a ontologia na pasta `ex2` com nome `med_doentes.ttl`;

11. `[2 val. = 0.5 * 4]` Uma vez criada a ontologia (última versão: `med_doentes.ttl`), especifica queries SPARQL que permitam responder às seguintes questões:
    - Quantas doenças estão presentes na ontologia?
    - Que doenças estão associadas ao sintoma `"yellowish_skin"`?
    - Que doenças estão associadas ao tratamento `"exercise"`?
    - Produz uma lista ordenada alfabeticamente com o nome dos doentes.
12. `[2 val.]` Cria uma query CONSTRUCT que diagnostique a doença de cada pessoa, ou seja, produza uma lista de triplos com a forma `:patientX :hasDisease :diseaseY`. No fim, acrescenta estes triplos à ontologia;
13. `[1 val.]` Cria um query SPARQL que poduza uma distribuição dos doentes pelas doenças, ou seja, dá como resultado uma lista de pares `(doença, nº de doentes)`;
14. `[1 val.]` Cria um query SPARQL que poduza uma distribuição das doenças pelos sintomas, ou seja, dá como resultado uma lista de pares `(sintoma, nº de doenças com o sintoma)`;
15. `[1 val.]` Cria um query SPARQL que poduza uma distribuição das doenças pelos tratamentos, ou seja, dá como resultado uma lista de pares `(tratamento, nº de doenças com o tratamento)`.

Bom trabalho e boa sorte 
jcr
