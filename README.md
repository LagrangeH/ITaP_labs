# ITaP_labs
Изначально нужно установить `jupyter`, [pandoc](https://pandoc.org/installing.html) и [TeX](https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex) и зависимости окружения.

Конвертировать сразу все jupyter notebooks в pdf-файлы (запустить в корне репозитория, выполнение может занять несколько минут):
```sh
jupyter nbconvert --to webpdf labs/*/*.ipynb --FilesWriter.build_directory=labs/export_jupyter --allow-chromium-download
```
При повторном запуске указывать флаг `--allow-chromium-download` не нужно:
```sh
jupyter nbconvert --to webpdf labs/*/*.ipynb --FilesWriter.build_directory=labs/export_jupyter
```
Вместо `labs/*/*.ipynb` могут быть указаны любые другие notebooks или их маски.
