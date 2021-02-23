# Trabalho 2 

Segunda prática desenvolvida na aula de Data Sciense em Segurança. Consiste de duas partes: a primeira mexe com a análise de APKs e a segunda com análise de arquivos PE.

## Parte 1 : Análise de APKs

### Entrada

Consiste no nome do diretório com os arquivos .xml das APKS que desejam ser analisadas.

```bash
python T2p1.py [caminho diretório]
```

### Saida

O script retorna a lista de permissões de cada arquivo .xml sob forma de um dicionário (chave: nome da APK, valor: lista de permissões). Assim como a lista de permissões únicas de cada APK e comuns a todas as APKs analisadas.

```bash
===================

Permissões por APK

===================

BancoX-v01: ['WRITE_SETTINGS', 'READ_APP_BADGE']

...

InstantMessengerY-101010: ['SEND_SMS', 'WRITE_SETTINGS']


===================

Permissões únicas por APK

===================

BancoX-v01: ['READ_APP_BADGE']

...

InstantMessengerY-101010: ['SEND_SMS']

===================

Permissões comuns das APKs

===================

['WRITE_SETTINGS']
```

## Parte 2 : Análise de arquivos PE

Na segunda parte fazemos dois tipos de análises :

### Análise 1

#### Entrada

Consiste no nome do diretório com os arquivos .exe que desejam ser analisados.

```bash
python T2p2-1.py [caminho diretório]
```

### Saída

O script retorna a lista de de seções executáveis de cada binário .exe sob forma de um dicionário (chave: nome do .exe, valor: lista de seções executáveis)


```bash
===================

Seções executáveis por PE

===================

BancoX.exe: ['.text', '.data']

```


### Análise 2

#### Entrada

Consiste no nome do dos arquivos dois arquivos .exe que desejam ser analisados.

```bash
python T2p2-1.py [caminho arquivo 1] [caminho arquivo 2]
```

### Saída

O script retorna a lista de seções de cada arquivo .xml sob forma de um dicionário (chave: nome da APK, valor: lista de permissões). Assim como a lista de seções únicas de cada APK e comuns a todos os arquivos .exe analisados.

```bash
===================

Seções por PE

===================

file1.exe: ['.text', '.data']


file2.exe: ['.text', '.data', '.rsrc']


===================

Seções únicas por PE

===================

file1.exe: []

file2.exe: ['.rsrc']

===================

Seções comuns das PE

===================

 ['.text', '.data']
```