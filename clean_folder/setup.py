from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0',
    description='Script to sort and clean folder',
    url='https://github.com/denzai83/homework-7',
    author='Denys Zaitsev',
    author_email='denzai83@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': [
        'clean-folder = clean_folder.clean:main']}
)
