# CLAUDE.md — NTI Buddhist Text Reader Project

## Architecture note

The site has migrated from static site generation to a single page app built
with the [chinesenotes-frontend](https://github.com/alexamies/chinesenotes-frontend)
framework. **Generation of the HTML pages in `html/` is outside the scope of
this repository.** The files in `html/` are content fragments consumed by the
frontend framework, not full standalone pages.

Do not attempt to run a static site generator or build tool from this repo to
produce the HTML output — that is handled by the frontend framework.

## External links in HTML fragments

External links (href starting with `http://` or `https://`) in the HTML
fragments use `target="_blank" rel="noopener noreferrer"` and include an inline
`<img src="external-link.svg">` icon so users know the link opens in a new
window. The icon lives at `html/external-link.svg`.

## Data files

- `data/dictionary/buddhist_terminology.txt` — main Buddhist terminology dictionary
- `data/dictionary/cnotes_zh_en_dict.tsv` — general Chinese-English dictionary
- Corpus texts are in `corpus/`

## License

- Dictionary content: Creative Commons Attribution-Share Alike 3.0
- Source code and markup: Apache 2.0
