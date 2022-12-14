# ITaP_labs
Изначально нужно установить `jupyter`, [pandoc](https://pandoc.org/installing.html) и [TeX](https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex) и зависимости окружения.

Конвертировать сразу все jupyter notebooks в pdf-файлы (запустить в корне репозитория, выполнение может занять несколько минут):
```shell
jupyter nbconvert --to webpdf labs/*/*.ipynb --TemplateExporter.extra_template_basedirs=share/jupyter/nbconvert/templates --template mtuci --FilesWriter.build_directory=labs/export_jupyter --allow-chromium-download
```
При повторном запуске указывать флаг `--allow-chromium-download` не нужно:
```shell
jupyter nbconvert --to webpdf labs/*/*.ipynb --FilesWriter.build_directory=labs/export_jupyter
```
Вместо `labs/*/*.ipynb` могут быть указаны любые другие notebooks или их маски.

Объединить несколько `notebooks` в один:
```shell
nbconvert <name1>.ipynb <name2>.ipynb ... <nameN>.ipynb -o result.ipynb
```
[Подробнее](https://github.com/jbn/nbmerge#usage)
