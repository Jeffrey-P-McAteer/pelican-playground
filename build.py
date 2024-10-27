
import os
import sys
import argparse
import subprocess

def setup_env():
  packages = os.path.join(os.path.dirname(__file__), '.py-env')
  os.makedirs(packages, exist_ok=True)

  if not packages in sys.path:
    sys.path.append(packages)

  # Assigning to PYTHONPATH means child processes inherit the python sys.path change
  if not packages in os.environ.get('PYTHONPATH', ''):
    os.environ['PYTHONPATH'] = os.pathsep.join([x for x in os.environ.get('PYTHONPATH', '').split(os.pathsep) if len(x) > 0] + [packages])

  try:
    import pelican
  except:
    subprocess.run([
      sys.executable, '-m', 'pip',
        'install',
        f'--target={packages}',
        'pelican[markdown]',
    ])
    import pelican

def ensure_site_initialized(args):
  if not os.path.exists(args.site_content):
    os.makedirs(args.site_content, exist_ok=True)

  pelicanconf_py = os.path.join(args.site_content, 'pelicanconf.py')

  if not os.path.exists(pelicanconf_py):
    original_sys_argv = list(sys.argv)

    import re
    from pelican.tools.pelican_quickstart import main as pelican_main
    sys.argv = [
      re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0]), # copy/paste out of the shim used to run pelican_quickstart.main(),
      f'--path={args.site_content}',
    ]
    pelican_main()

    sys.argv = original_sys_argv


def run_build(args):
  setup_env()
  ensure_site_initialized(args)

  subprocess.run([
    sys.executable, '-m', 'pelican',
      'content',
  ], check=True, cwd=args.site_content)

  out_dir = os.path.join(args.site_content, 'output')
  print()
  print(f'Site content was genereated to {out_dir}')



def run_server(args):
  setup_env()
  ensure_site_initialized(args)
  subprocess.run([
    sys.executable, '-m', 'pelican',
      '--listen',
      '--autoreload',
      '--port', str(args.server_port),
      '--bind', '127.0.0.1',
      '--ignore-cache',
      '--relative-urls',
  ], check=True, cwd=args.site_content)

def main(argv=sys.argv):
  ap = argparse.ArgumentParser(
    prog=__file__,
    description='A Pelican Builder w/ no dependencies outside python STL and some package sources'
    # epilog=''
  )
  ap.add_argument(
    '--site-content',
    type=str,
    default=os.path.join(os.path.dirname(__file__), 'content'),
    help='Directory which holds your site content; is passed to pelican-quickstart if <site-content>/pelicanconf.py does not exist.'
  )
  ap.add_argument(
    '--server',
    default=False,
    action='store_true',
    help='Run a Pelican server on --server-port'
  )
  ap.add_argument(
    '--server-port',
    type=int,
    default=8080,
    help='For --server, which port to bind to'
  )

  args = ap.parse_args(argv[1:])

  if args.server:
    run_server(args)
  else:
    run_build(args)


if __name__ == '__main__':
  main()