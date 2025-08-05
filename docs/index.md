# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Workflow

mermaid

```mermaid
flowchart LR
    subgraph ETL [Pipeline]
        A("Múltiplos Arquivos Excel")
        B("Extract: extract_from_excel")
        C("Transformation: consolidate_dataframes")
        D("Load: Converte para Excel")
        E("Pasta Output: Um Arquivo único Excel")

        A --> B
        B -- "Gera uma lista de DataFrames" --> C
        C -- "Gera um DataFrame consolidado" --> D
        D -- "Salva o consolidado em Excel" --> E
    end

```

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


# Função de transformação de dados

### ::: app.pipeline.extract.extract_from_excel