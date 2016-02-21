try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'Key Result Area application for employee performance management',
    'author': ['Meshack B. Shabalala', 'Alex Lucouw'],
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'mshabalala@csir.co.za, bafana5@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['wKRApp'],
    'scripts': [],
    'name': 'wKRApp'
}

setup(**config)