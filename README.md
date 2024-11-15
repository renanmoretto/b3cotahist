# b3cotahist

Biblioteca Python para leitura e fetch do arquivo COTAHIST da B3. Suporta tanto pandas quanto polars como engines.

## Instalação

```bash
pip install b3cotahist
```

## Uso

### Download direto da B3

```python
import datetime
import b3cotahist

# Download dos dados do pregão de 01/03/2024
df = b3cotahist.get(
    date=datetime.date(2024, 3, 1),
    engine='pandas'  # ou 'polars'
)

# Caso tenha problemas com SSL da b3
df = b3cotahist.get(
    date=datetime.date(2024, 3, 1),
    raise_ssl_error=True
)
```

### Leitura de arquivos

```python
df = b3cotahist.read_zip(path='COTAHIST_D20240301.ZIP')

df = b3cotahist.read_txt(path='COTAHIST_D20240301.TXT')

# Ou caso queira usar polars
df = b3cotahist.read_zip(path='COTAHIST_D20240301.ZIP', engine='polars')
```

### Leitura de bytes

```python
# Lendo a partir de bytes
with open('COTAHIST_D20240301.TXT', 'rb') as f:
    dados = f.read()
df = b3cotahist.read_bytes(dados)

# Ou a partir de BytesIO
import io
bytes_io = io.BytesIO(dados)
df = b3cotahist.read_bytes(bytes_io)
```