imagefun

0. Generate image albumn snapshot

![alt clusters](https://github.com/blackball/imagefun/raw/master/snapshot.jpg)

```Python
from Snapshot import *
sp = Snapshot()
sp.generate("/home/blackball/Pictures/", "snapshot.jpg")
```

1. Backup unique images.

```Python
from ImageBackUp import *
bk = ImageBackUp()
unique_images = bk.get("/home/blackball/Pictures/")
bk.backup(unique_names, "/home/blackball/backup/photos/")
```