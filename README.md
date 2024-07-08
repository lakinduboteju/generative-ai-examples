# Generative AI Examples

``` bash
$ docker compose up -d
$ docker compose down
```

``` bash
$ docker exec -it generative-ai-examples bash
```

``` bash
$ poetry init
$ poetry add -G dev debugpy
```

``` bash
$ poetry run python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 --wait-for-client main.py
```
