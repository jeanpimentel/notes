import shutil
import os
from pprint import pprint

def copy_licenses(*args, **kwargs):	
	docs_dir = kwargs['config']['docs_dir']

	# shutil.copy('docs/LICENSE-CC-BY-SA', f'{docs_dir}/LICENSE-CC-BY-SA.md')
	# shutil.copy('docs/LICENSE-MIT', 'docs/LICENSE-MIT.md')

def rename_licenses(*args, **kwargs):
	site_dir = kwargs['config']['site_dir']

	# os.rename(f'{site_dir}/LICENSE-CC-BY-SA', f'{site_dir}/LICENSE-CC-BY-SA.md')
	# os.rename(f'{site_dir}/LICENSE-MIT', f'{site_dir}/LICENSE-MIT.md')

	
	pprint(args)
	pprint(kwargs)
	pprint(site_dir)