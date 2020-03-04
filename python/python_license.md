# Python License

https://ja.stackoverflow.com/questions/48650/python%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%81%AE%E3%83%A9%E3%82%A4%E3%82%BB%E3%83%B3%E3%82%B9%E3%82%92%E7%A2%BA%E8%AA%8D%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95

## pip-licenses
### Install
```
pip install pip-licenses
```

```
$ pip-license > licenses.txt
```

https://pypi.org/project/pip-licenses/#option-from-classifier

```
$ pip-licenses --from=classifier --with-system | grep entrypoints
 entrypoints         0.3         MIT License
```

```
pip-licenses --from=mixed --with-system --with-description --order=license --format=csv > license_<project>.csv
```
