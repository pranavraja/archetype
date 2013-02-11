import jinja2
import os
import sys
import string

def output_files(input_files, template_params, new_basepath):
    return { jinja2.Template(os.path.join(new_basepath, filename)).render(**template_params) : jinja2.Template(content).render(**template_params) for filename, content in input_files }

def write_all(files):
    def ensure_parent(filename):
        if not os.path.isdir(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
    def write(filename, content):
        with open(filename, 'w') as f:
            f.write(content)
    for filename, content in files.items():
        ensure_parent(filename)
        write(filename, content)

def read_all(folder):
    for root, dirs, files in os.walk(folder):
        for f in files:
            filename = os.path.join(root, f)
            yield os.path.relpath(filename, folder), open(filename).read()

def read_env(filename):
    env = {}
    with open(filename) as f:
        for line in f:
            param, value = line.rstrip().split('=')
            env[param] = value
    return env

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print 'Usage: python {} template_folder output_folder env'.format(__file__)
        sys.exit(0)
    template_folder = sys.argv[1]
    output_folder = sys.argv[2]
    env = sys.argv[3] if len(sys.argv) > 3 else None
    files = read_all(template_folder)
    params = read_env(env) if env else {}
    params['APP_DIR'] = os.path.basename(output_folder)
    params['APP_NAME'] = ''.join(c for c in os.path.basename(output_folder) if c not in string.punctuation).lower()
    params['APP_PATH'] = os.path.abspath(output_folder)
    output = output_files(files, params, output_folder)
    write_all(output)