# Russian

# ytdx - Загрузчик видео с YouTube

Командная утилита для скачивания видео и аудио с YouTube по ссылке с дополнительными опциями.

## Возможности

- Скачивание видео в различных качествах (1080p, 720p, 480p, 360p)
- Скачивание только аудио
- Выбор формата (mp4, mp3, webm и другие)
- Указание имени выходного файла
- Указание папки для сохранения
- Работа в неинтерактивном режиме

## Установка

### Через Homebrew

```bash
brew install flaymie/tap/ytdx
```

### Через pip

```bash
pip install git+https://github.com/flaymie/ytdx.git
```

### Из исходников

```bash
git clone https://github.com/flaymie/ytdx.git
cd ytdx
pip install .
```

## Использование

### Простое скачивание видео

```bash
ytdx https://youtube.com/watch?v=abc123
```

### Скачивание только аудио в формате mp3

```bash
ytdx https://youtube.com/watch?v=abc123 --audio
```

### Скачивание видео в определенном качестве и формате

```bash
ytdx https://youtube.com/watch?v=abc123 -f mp4 -q 720
```

### Скачивание с указанием имени файла и папки сохранения

```bash
ytdx https://youtube.com/watch?v=abc123 -o Видео -n мое_видео
```

### Работа с путями

По умолчанию файлы сохраняются в текущую директорию. При указании пути можно использовать:
- Относительные пути: `-o videos` (относительно текущей директории)
- Абсолютные пути: `-o /Users/username/Downloads`
- Пути с тильдой: `-o ~/Downloads` (относительно домашней директории)

### Все доступные опции

```
usage: ytdx [-h] [-a] [-f FORMAT] [-o OUTPUT] [-n NAME] [-q QUALITY] url

Скачивание видео с YouTube по ссылке

positional arguments:
  url                   Ссылка на видео

options:
  -h, --help            показать справку и выйти
  -a, --audio           Скачать только аудио (mp3)
  -f FORMAT, --format FORMAT
                        Формат (mp4, mp3, webm и т.д.)
  -o OUTPUT, --output OUTPUT
                        Папка для сохранения (по умолчанию: текущая директория)
  -n NAME, --name NAME  Имя выходного файла (без расширения)
  -q QUALITY, --quality QUALITY
                        Качество видео (1080, 720, 480, 360)
```

## Требования

- Python 3.6+
- yt-dlp
- FFmpeg (для конвертации аудио)

## Лицензия

MIT

---

# English

# ytdx - YouTube Video Downloader

Command-line utility for downloading videos and audio from YouTube with additional options.

## Features

- Download videos in various qualities (1080p, 720p, 480p, 360p)
- Download audio only
- Choose format (mp4, mp3, webm and others)
- Specify output filename
- Specify save directory
- Non-interactive mode

## Installation

### Via Homebrew

```bash
brew install flaymie/tap/ytdx
```

### Via pip

```bash
pip install git+https://github.com/flaymie/ytdx.git
```

### From source

```bash
git clone https://github.com/flaymie/ytdx.git
cd ytdx
pip install .
```

## Usage

### Simple video download

```bash
ytdx https://youtube.com/watch?v=abc123
```

### Download audio only in mp3 format

```bash
ytdx https://youtube.com/watch?v=abc123 --audio
```

### Download video in specific quality and format

```bash
ytdx https://youtube.com/watch?v=abc123 -f mp4 -q 720
```

### Download with custom filename and directory

```bash
ytdx https://youtube.com/watch?v=abc123 -o Videos -n my_video
```

### Working with paths

By default, files are saved to the current directory. When specifying a path, you can use:
- Relative paths: `-o videos` (relative to current directory)
- Absolute paths: `-o /Users/username/Downloads`
- Tilde paths: `-o ~/Downloads` (relative to home directory)

### All available options

```
usage: ytdx [-h] [-a] [-f FORMAT] [-o OUTPUT] [-n NAME] [-q QUALITY] url

Download videos from YouTube by URL

positional arguments:
  url                   Video URL

options:
  -h, --help            show help and exit
  -a, --audio           Download audio only (mp3)
  -f FORMAT, --format FORMAT
                        Format (mp4, mp3, webm, etc)
  -o OUTPUT, --output OUTPUT
                        Output directory (default: current directory)
  -n NAME, --name NAME  Output filename (without extension)
  -q QUALITY, --quality QUALITY
                        Video quality (1080, 720, 480, 360)
```

## Requirements

- Python 3.6+
- yt-dlp
- FFmpeg (for audio conversion)

## License

MIT