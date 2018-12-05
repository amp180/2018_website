from pathlib import Path
import os
import scss

def compile_scss(basedir, infile, outfile):
    compiled = scss.compiler.compile_file(
        Path(infile),
    )
    with open(outfile, 'w') as o:
        o.write(compiled)
    

ASSETS_DIR = os.path.dirname(__file__)

if __name__== '__main__':
	compile_scss(
	  os.path.join(ASSETS_DIR, ".."), 
	  os.path.join(ASSETS_DIR, "./scss/main.scss"),
	  os.path.join(ASSETS_DIR, "../static/css/main.css")
	)