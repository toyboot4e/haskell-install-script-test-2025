import tomllib
import json

with open('installscript.toml', 'rb') as f:
    config = tomllib.load(f)

def replace_ML(s: str) -> str:
    # ML 2 GB を入れる
    s = s.replace('{memory:b}', str(1 << 31))
    s = s.replace('{memory:kb}', str(1 << 21))
    s = s.replace('{memory:mb}', str(1 << 11))
    return s

with open('src/install.sh', 'w') as f:
    f.write(replace_ML(config['install']))

with open('src/compile.sh', 'w') as f:
    f.write(replace_ML(config['compile']))

with open('src/Dockerfile', 'w') as f:
    f.write(f'''FROM ubuntu:24.04 AS base

RUN apt-get update && apt-get upgrade -y

COPY src/missing-packages.txt /tmp/missing-packages.txt
RUN DEBIAN_FRONTEND=noninteractive xargs -a /tmp/missing-packages.txt apt-get install -y --no-install-recommends

RUN useradd -m runner && echo "runner ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/runner

RUN mkdir -p /judge && chown runner:runner /judge

WORKDIR /judge

USER runner

ENV ATCODER=1

FROM base AS install

COPY src/install.sh /tmp/install.sh

RUN bash /tmp/install.sh

FROM install AS compile

COPY src/source /judge/{config['filename']}
COPY src/compile.sh /tmp/compile.sh

RUN bash /tmp/compile.sh
RUN test -f {config['object']}
CMD {json.dumps(config['execution'])}
''')
    if 'environment' in config:
        for key, value in config['environment'].items():
            f.write(f'ENV {key}={value}\n')
