# pyguass
A wrap guass 200 java jdbc driver for python

## Dependence
* typing_extensions
* JPype1
* JayDeBeApi
* JAVA SDK 1.8

## Usage
```
import pyguass
kwargs = {
	"user":"user1",
	"password":"password1",
	"dbname":"testdb",
	"host":"xx.xx.xx.xx",
	"port":25308
}
conn = pyguass.connect(**kwargs)
...
```

