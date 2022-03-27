# Tiles Server

## Install requirements
```
pip install -r requirements.txt
```

## 1. Download Tiles

Go to this web site: https://boundingbox.klokantech.com/

Change to CSV format and get the bounds of the desire area.

For example -10.06,40.16,4.11,52.66

The bounds are given: left, bottom, right, top

Choose the zoom level you want from 0 to 18.

Launch the command
```bash
# python3 download.py left bottom right top min_zoom max_zoom
python3 download.py -10.06 40.16 4.11 52.66 0 6
# OR
python3 download.py -4.91 43.04 5.44 49.53 0 5
```

## 2. Launch Server

Launch the server for your new server

```
python3 app.py
```

If the request correspond to a unknown tiles, the server sent the 0-0-0 tile.