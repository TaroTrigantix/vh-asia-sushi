"""Bundle only public static files. Does not publish or change DNS."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'dist'


def main():
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    for name in ['index.html', 'robots.txt', '_redirects']:
        shutil.copy2(ROOT / name, OUTPUT / name)
    for name in ['pages', 'css', 'js', 'assets']:
        shutil.copytree(ROOT / name, OUTPUT / name)
    print(f'Static files bundled: {OUTPUT}')


if __name__ == '__main__':
    main()
