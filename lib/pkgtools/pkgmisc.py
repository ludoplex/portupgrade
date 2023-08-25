import os
import re
import tempfile

def qindex(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return None

def qinclude(lst, item):
    return item in lst

def shellwords(line):
    return re.findall(r'"([^"]*)"|\'([^\']*)\'|\\(.)|(\S+)', line)

def shelljoin(args):
    return ' '.join(re.sub(r'([$\\\"\`])', r'\\\1', arg) if re.search(r'[*?{}\[\]<>()~&|\\$;\'\`\s]', arg) else arg for arg in args)

def init_tmpdir():
    global $tmpdir
    if $tmpdir is None or $tmpdir == "":
        $tmpdir = tempfile.mkdtemp()
