from distutils.core import setup


conf = dict(
    name='autoversion',
    version='1.2.1',
    description="Obtain installed version of package automatically, even if "
                "it is installed using editable or develop",
    long_description="\n".join(list(open("README"))[2:]).strip(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ],
    requires=["setuptools"],
    keywords='autoversion __autoversion__ __version__ __version__tuple__ version git',
    author='Peter Waller',
    author_email='p@pwaller.net',
    url='http://github.com/pwaller/__autoversion__',
    py_modules=["__autoversion__"],
)

if __name__ == '__main__':
    setup(**conf)
