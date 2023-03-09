from setuptools import setup


def get_version() -> str:
    rel_path = "bidet/__init__.py"
    with open(rel_path, "r") as fp:
        for line in fp.read().splitlines():
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name='bidet',
    version=get_version(),
    description='The cleanest machine learning library',
    url='http://github.com/poopingface/bidet',
    author='Pooping Face',
    author_email='poopingface.co@gmail.com',
    license='MIT',
    packages=['bidet'],
    zip_safe=False
)