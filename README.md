## Oppgave
Jeg har tenkt å lage en nettside basert på python og flask. Nettsiden skal gi mulighet til brukere for spør om ulike tjenester (feks. Real estate, trading), med chat lignende grensesnitt. Skal bruke Open AI og GPT modellene for å svare på spørsmålene. Hvis jeg har tid skal jeg ha CI/CD for å “deploye” til en Azure app service. 

## Kompetansemålene

Dette prosjektet inngår disse kompetansemålene: 

## Driftstøtte 

### planlegge, drifte og implementere IT-løsninger som ivaretar informasjonssikkerhet og gjeldende regelverk for personvern

Tar ikke eller lagrer noe personlig informasjon sendt gjennom nettsiden. Bruker open AI tjenester som kan være en risiko, men har satt en varsel melding ved chatboxen om å ikke dele personlig info, i og med at OpenAI lagrer info den tar imot.

"We may use content submitted to ChatGPT, DALL·E, and our other services for individuals to improve model performance"
https://help.openai.com/en/articles/7039943-data-usage-for-consumer-services-faq  

Jeg bruker secrets i prosjektet som OPEN_AI API key for å sette en kobling til Open AI. Disse kan være farlig å publisere for diverse grunner (bruke min AI service, som kan koste penger), og er derfor lagret i en .env som ikke publiserer til Github.

### reflektere over og beskrive hvordan brudd på personvernet kan påvirke enkeltmennesker, virksomheter og samfunn 
Ved brudd på personvernet kan andre få tilgang til personlig info, som Navn Adresse og økonomiske opplysninger. Dette kan blandt annet brukes for blackmail, fraud, phishing, identity theft, stealing selskaps hemmeligheter (espionage) 


## Brukerstøtte 

### gjøre rede for og anvende etiske retningslinjer og relevant lovverk i eget arbeid 



### utvikle kursmateriell og gjennomføre kurs i relevante IT-systemer tilpasset en målgruppe 

Har fokusert en del på UI, for at nettsiden skal være enkel å forstå og bruke for de fleste. Også brukt tid på å prøve å lage en forklarende readme fil, som skal hjelpe meg og andre i og sette opp og bruke dette prosjektet, messt rette mot utviklere.

bruker vennlig, veiledning i nettside til sluttbrukere, utfullende readme tilpasset utviklere

### bruke og tilpasse kommunikasjonsform og fagterminologi i møte med brukere, kunder og fagmiljø. 



### reflektere over og gjøre rede for hvordan intelligente systemer påvirker bransjen og samfunnet 

Nettsiden jeg har laget er et eksempel på bruk av AI. Noen positive effekter er enklere tilgang til kunsskap, kjappere svar, ny innsikt, nye muligheter, automatisering av diverse program eller tidligere menneske jobber, større kunnskap. Noen negatvie effekter er at den som sagt erstatte jobber, har mulighet for feil svar/misforståelser som mennesker ikke alltid ville hatt ("feks: chat gpt som sa Anders Breivik var en norsk helt https://www.theverge.com/2018/1/12/16882408/google-racist-gorillas-photo-recognition-algorithm-ai) må lære andre måter å hente info fra


noen selskap responsible Ai guidelines
https://ai.google/responsibility/responsible-ai-practices/
https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai?view=azureml-api-2



### bruke og administrere samhandlingsverktøy som effektiviserer samarbeid og deling av informasjon 

Har brukt Github gjennom hele prosjektet, for versjonskontroll(i tilfelle noe gale skulle skjdd me koden), og slik at jeg kan legge det ut på profilen min som en public repository. Github sammen med bra dokumentasjon og forståpelig kode gjør det enkelt for samarbeid via feks branches, og enkelt og dele me andre.

### utøve brukerstøtte og veilede i relevant programvare 

Brukerstøtte ligger i readme filen for de som ønsker å sette opp prosjektet selv, med en step-by-step guide til å sette det opp. Har også veiledning på nettsiden, og kunne hatt mulighet for en AI chat box laget kunn for brukervennlighet og hjelp til å navigere osv.

## Utvikling 

### vurdere fordeler og ulemper ved ulike programmeringsspråk og velge og anvende relevante programmeringsspråk og algoritmer i eget arbeid 

Flask er enkel å bruke, forstå og lære, i tillegg til at jeg har brukt det før. Det finnes andre "web framework" som f.eks Django, men hadde ikke så mye tid til å lære noe nytt på gitt tid. Brukt en del bootstrap og for å hjelpe med diverse frontend funksjoner. 

### lage og begrunne funksjonelle krav til en IT-løsning basert på behovskartlegging 



### vurdere brukergrensesnitt til IT-tjenester og designe tjenester som er tilpasset brukernes behov 

bilde

### gjøre rede for hensikten med teknisk dokumentasjon og utarbeide teknisk dokumentasjon for IT-løsninger 

Slik at jeg og andre enklere kan huske og forstå prosjektets oppsett og hvordan det kan brukes.

### beskrive og anvende relevante versjonskontrollsystemer i utviklingsprosjekter 

Som nevnt tidligere har jeg brukt Github som versjonskontroll, hvor jeg har prøvd å comitte forandringer ofte, slik at mulige feil er enklere å rette opp i ved å se på tidligere versjoner på prosjektet.


# AI Chat Website 
This is a website made for anyone to help them pursue different types of careers, such as investing or real estate. It uses AI to respond to input bu users.

## Setup

### Prerequisites

Before starting, install the following tools:

- Python 3.12 or later
- Pip package manager

For more information on these tools, see the public documentation on
[Python](https://www.python.org/downloads/) or
[Pip](https://pip.pypa.io/en/stable/installing/)

### Setup development PC
From the root of your cloned repo, generate a virtual environment with a
specific version of python.

Windows
```bash
python -m venv .venv
.venv\Scripts\activate.bat
```

Linux / MacOS
```bash
python3 -m venv .venv
. ./.venv/bin/activate
```

Next install any necessary packages.

```bash
pip install -r requirements.txt
```

### Running the Flask App Locally

From the root of your cloned repo run the following:

```bash
flask run --debug
```

## References

* https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
* https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?toc=%2Fazure%2Fdeveloper%2Fpython%2Ftoc.json&bc=%2Fazure%2Fdeveloper%2Fpython%2Fbreadcrumb%2Ftoc.json&tabs=flask%2Cwindows%2Cvscode-aztools%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli
* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-facelift

