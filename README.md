# ITaP_labs
Конвертировать сразу все jupyter notebooks в pdf-файлы:
```sh
jupyter nbconvert --to pdf labs/*/*.ipynb --FilesWriter.build_directory=labs/export_jupyter
```
Могут вылететь исключения о том, что не установлены все зависимости - тогда нужно перейти по соответствующим ссылкам и установить