# weechat-pushbullet.py

weechat notification plugin via pushbullet.

weechat-pushbullet.py hooks notify_private and notify_highlight.

## INSTALL

```
$ curl -o ~/.weechat/python/weechat-pushbullet.py https://raw.githubusercontent.com/soh335/weechat-pushbullet/master/weechat-pushbullet.py
/set plugins.var.python.weechat-pushbullet.token "<API_TOKEN>"
/script load weechat-pushbullet.py
```

### AUTOLOAD

```
$ cd ~/.weechat/python/autoload
$ ln -s ../weechat-pushbullet.py
```

## LICENSE

* MIT
