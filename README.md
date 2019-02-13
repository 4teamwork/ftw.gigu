# ftw.gigu

Analyse github data

## Quickstart

```bash
git clone git@github.com:4teamwork/ftw.gigu.git
cd ftw.gigu
path/to/favourite/python3 -m venv venv
source venv/bin/activate
python setup.py install
```

Add Credentials:

```bash
touch .env
echo "GITHUB_TOKEN='[your github token]'" >> .env
```

Generate graph for current github data:

```bash
analyze_data
```
