from setuptools import setup

setup(
    name="ytdx",
    version="0.1.0",
    description="Загрузчик видео с YouTube через командную строку",
    author="Flaymie",
    author_email="flaymie@example.com",
    py_modules=["ytdx"],
    install_requires=[
        "yt-dlp>=2023.3.4",
    ],
    entry_points={
        "console_scripts": [
            "ytdx=ytdx:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 