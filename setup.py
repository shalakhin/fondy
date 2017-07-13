from distutils.core import setup


setup(
  name = 'fondy',
  packages = ['fondy'], # this must be the same as the name above
  version = '0.1',
  description = 'Python library for the Fondy API',
  author = 'Olexandr Shalakhin',
  author_email = 'olexandr@shalakhin.com',
  url = 'https://github.com/shalakhin/fondy', # use the URL to the github repo
  download_url = 'https://github.com/shalakhin/fondy/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  requires = ['requests'],
  classifiers = [
	'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'

  ],
)
