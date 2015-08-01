import weechat, urllib, json

weechat.register("weechat-pushbullet", "soh335", "0.0.1", "MIT", "notify via pushbullet", "", "")
weechat.hook_print("", "notify_private,notify_highlight", "", 1, "print_cb", "")
weechat.hook_command("pushbullet", "send pushbullet for debug message", "[message]", "", "", "pushbullet_cb", "")

def pushbullet_cb(data, buffer, args):
  notify(args)
  return weechat.WEECHAT_RC_OK

def print_cb(data, buffer, date, tags, displayed, highlight, prefix, message):
  buffer_name = weechat.buffer_get_string(buffer, "full_name")
  body        = "[%s] <%s> %s" % (buffer_name, prefix, message)
  notify(body)
  return weechat.WEECHAT_RC_OK

def notify(body):
  token  = weechat.config_get_plugin("token")
  url    = "https://%s@api.pushbullet.com/v2/pushes" % (token)
  fields = urllib.urlencode({"type": "note", "body": body})
  weechat.hook_process_hashtable("url:"+url, { "postfields": fields }, 10000, "notify_cb", "")

def notify_cb(data, command, return_code, out, err):
  if return_code == weechat.WEECHAT_HOOK_PROCESS_ERROR:
    weechat.prnt("", "%s pushbullet.py got err command %s" % (weechat.prefix("error"), command))
    return weechat.WEECHAT_RC_OK

  # weechat.prnt("", "command:%s return_code:%s out:%s err:%s" % (command, return_code, out, err))
  j = json.loads(out)
  if "error" in j:
    weechat.prnt("", "%s weechat-pushbullet.py %s %s" % (weechat.prefix("error"), j["error"]["type"], j["error"]["message"]))

  return weechat.WEECHAT_RC_OK
