"""Check local page, stylesheet, module and asset references without dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.ids = set()
        self.headings = 0

    def handle_starttag(self, tag, attributes):
        values = dict(attributes)
        if values.get('id'):
            assert values['id'] not in self.ids, f"Duplicate id: {values['id']}"
            self.ids.add(values['id'])
        if tag == 'h1':
            self.headings += 1
        for key in ['src', 'href']:
            if key in values:
                self.references.append(values[key])
        if tag == 'img':
            assert 'alt' in values, 'Missing image alt attribute'


def check_reference(source, reference, pages):
    url = urlsplit(reference)
    if url.scheme or url.netloc:
        return
    target = (source.parent / unquote(url.path)).resolve() if url.path else source
    assert target.is_relative_to(ROOT), f'Outside project: {reference}'
    assert target.is_file(), f'{source.relative_to(ROOT)}: Missing {reference}'
    if url.fragment and target in pages:
        assert url.fragment in pages[target].ids, f'Missing anchor: {reference}'


def main():
    pages = {}
    for path in [ROOT / 'index.html', *sorted((ROOT / 'pages').glob('*.html'))]:
        parser = PageParser()
        parser.feed(path.read_text())
        assert parser.headings == 1, f'{path.name}: Expected one h1'
        pages[path] = parser
    for path, page in pages.items():
        for reference in page.references:
            check_reference(path, reference, pages)
    for path in (ROOT / 'css').rglob('*.css'):
        for reference in re.findall(r'url\([\"\']?([^\)\"\']+)', path.read_text()):
            check_reference(path, reference, pages)
    for path in (ROOT / 'js').rglob('*.js'):
        for reference in re.findall(r'from [\"\']([^\"\']+)', path.read_text()):
            check_reference(path, reference, pages)
    print(f'OK: {len(pages)} pages; local links, anchors, assets, CSS and JS imports.')


if __name__ == '__main__':
    main()
