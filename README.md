# Generative AI Examples

## How to run

``` bash
# Add LLM credentials to the .env file
mv .env.example .env
```

``` bash
$ docker compose build
$ docker compose up -d
$ docker compose down
```

``` bash
$ docker exec -it generative-ai-examples bash
```

``` bash
$ poetry install
```

``` bash
$ poetry run python run_xxxx.py
```

## Debug

``` bash
# Run following command and debug using Pythong Debugger in vscode
$ poetry run python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 --wait-for-client run_xxxx.py
```

## Contents

1. Hello, World! : [hello_world](app/hello_world/)
2. Organize Medical Record : [organize_medical_record](app/organize_medical_record/)
