def load_config(config, key, default_value=None):
    if key in config:
        return config[key]
    else:
        return default_value
ans=load_config({"timeout": 10}, "timeout")
print(ans)
