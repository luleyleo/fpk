pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'fpk'

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('pkgdatadir', pkgdatadir)
configure_file(
            input: 'fpk.in',
           output: 'fpk',
    configuration: conf,
          install: true,
      install_dir: get_option('bindir'),
     install_mode: 'r-xr--r--'
)

fpk_sources = [
    '__init__.py',
    'main.py',
    'builder.py',
    'flathub.py'
]

install_data(fpk_sources, install_dir: moduledir)
