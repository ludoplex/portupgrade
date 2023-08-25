class PkgConfig:
    def __init__(self):
        pass

    def load_config(self, file):
        if not os.path.exists(file):
            return False

        try:
            with open(file, 'r') as f:
                self.config = json.load(f)
        except Exception as e:
            print(f"** Error occured reading {file}:", e)
            exit(1)

        self.init_pkgtools_global()

        val = self.config_value('SANITY_CHECK')
        if val is not None:
            self.sanity_check = val

        if 'PKG_SITES' in self.config:
            self.pkg_sites.extend(self.config['PKG_SITES'])
        else:
            self.pkg_sites.append(self.config['pkg_site_mirror'])

        return True

    def setproctitle(self, fmt, *args):
        setproctitle.setproctitle(f'{MYNAME}: {fmt.format(*args)}')

    def config_value(self, name):
        return self.config.get(name, None)

    def compile_config_table(self, hash):
        otable = {}
        gtable = {}

        if hash:
            for pattern, value in hash.items():
                self.glob(pattern, lambda portinfo: (otable.setdefault(portinfo.origin, set())).add(value))

            if not pattern.include('/'):
                gtable[pattern] = value

        return [otable, gtable]
