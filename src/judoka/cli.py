from judoka import command, config


hub = command.Hub(configresolver=config.load)


if __name__ == "__main__":
    hub()
