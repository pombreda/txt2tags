#
# txt2tags %!settings tester (http://txt2tags.org)
# See also: ../run.py ../lib.py
#
# Note: The .t2t files are generated dynamicaly, based on 'tests' dict data
#

import sys, os

sys.path.insert(0, '..')
import lib
del sys.path[0]

# sux
lib.OK = lib.FAILED = 0
lib.ERROR_FILES = []

# text patterns to compose source files
EMPTY_HEADER    = "\n"
# FULL_HEADER     = "Header 1\nHeader 2\nHeader 3\n"
SIMPLE_BODY     = "Text.\n"
# TITLED_BODY     = "= Title 1 =\nText.\n== Title 2 ==\nText.\n"
# EMAIL           = 'user@domain.com\n'
CONFIG_FILE_TXT = '%!target: html\n'
CSS_FILE_TXT    = 'p { color: blue; }\n'

# a nice postproc to rip off version information from output
VERSION_GOTCHA = "%!postproc: '(generated by txt2tags) [^ ]+' '\\1'\n"


# the registered tests
# Note: the extensive tests for each option are in test/options/ module.
tests = [
    {
    'name'   : 'target-empty',                  # empty %!target
    'content': '%!target:',
    'extra'  : ['notarget', 'error'],
    }, {
    'name'   : 'target-invalid',                # %!target: ERROR
    'content': '%!target: ERROR',
    'extra'  : ['notarget', 'error'],
    }, {
    'name'   : 'target',                        # %!target: html
    'content': '%!target: html',
    'outfile': 'target.html',
    'extra'  : ['notarget', 'noversion'],
    }, {
    'name'   : 'target-over-target',            # --target wins %!target
    'content': '%!target: pm6',
    'target' : 'html',
    'outfile': 'target-over-target.html',
    'extra'  : ['noversion'],
    }, {
    'name'   : 'options-target',                # %!options: --target html
    'content': '%!options: --target html',      # ignored
    }, {
    'name'   : 'options-empty',                 # empty %!options
    'content': '%!options:',
    }, {
    'name'   : 'options-invalid-short',         # %!options: -z
    'content': '%!options: -z',
    'extra'  : ['error'],
    }, {
    'name'   : 'options-invalid-long',          # %!options: --zzzz
    'content': '%!options: --zzzz',
    'extra'  : ['error'],
    }, {
    'name'   : 'options-no-header',             # %!options: --no-header
    'content': '%!options: --no-header',
    'target' : 'html',
    }, {
    'name'   : 'options-ignored',               # %!options: --(ignored-options)
    'content': '%!options: -h --help -V --version -v --verbose --debug --infile foo.t2t',
    # Actions not ignored (2012-07-31): --dump-config --dump-source --targets
    # TODO: -q
    }, {
    'name'   : 'options-no-infile',             # %!options: --no-infile
    'content': '%!options: --no-infile',        # ignored
    }, {
    'name'   : 'options-outfile-empty',         # %!options: --outfile
    'content': '%!options: --outfile',
    'extra'  : ['error'],
    }, {
    'name'   : 'options-outfile',               # %!options: --outfile *.out
    'content': '%!options: --outfile options-outfile.out',
    'outfile': 'options-outfile.out'
    }, {
    'name'   : 'options-no-outfile',             # %!options: --no-outfile
    'content': '%!options: --outfile fake --no-outfile',
    }, {
    ### TODO
    # 'name'   : 'enum-title-1',
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --enum-title"],
    # }, {
    # 'name'   : 'enum-title-2',                # with --toc
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --toc --enum-title"],
    # }, {
    # 'name'   : 'enum-title-3',                # no title to enumerate
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+SIMPLE_BODY,
    # 'cmdline': ["-H --enum-title"],
    # }, {
    # 'name'   : 'no-enum-title-1',             # useless
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --no-enum-title"],
    # }, {
    # 'name'   : 'no-enum-title-2',             # turning OFF
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --enum-title --no-enum-title"],
    # }, {
    # 'name'   : 'toc-1',
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --toc"],
    # }, {
    # 'name'   : 'toc-2',                       # empty toc (no title)
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+SIMPLE_BODY,
    # 'cmdline': ["-H --toc"],
    # }, {
    # 'name'   : 'toc-3',                       # empty body
    # 'target' : 'html',
    # 'content': EMPTY_HEADER,
    # 'cmdline': ["-H --toc"],
    # }, {
    # 'name'   : 'no-toc-1',                    # useless
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --no-toc"],
    # }, {
    # 'name'   : 'no-toc-2',                    # turning OFF
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --toc --no-toc"],
    # }, {
    # 'name'   : 'toc-level-1',
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --toc --toc-level 1"],
    # }, {
    # 'name'   : 'toc-level-2',                 # very deep
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --toc --toc-level 999"],
    # }, {
    # 'name'   : 'toc-level-3',                 # useless (no --toc)
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --toc-level 1"],
    # }, {
    # 'name'   : 'toc-only-1',
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["--toc-only -o toc-only-1.html"],
    # }, {
    # 'name'   : 'toc-only-2',                  # empty toc (no title)
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+SIMPLE_BODY,
    # 'cmdline': ["--toc-only -o toc-only-2.html"],
    # }, {
    # 'name'   : 'toc-only-3',                  # no target, defaults to txt
    # 'target' : 'out',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["--toc-only -o toc-only-3.out"],
    # 'extra'  : ['notarget'],
    # }, {
    # 'name'   : 'toc-only-4',                  # with --toc-level
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["--toc-only --toc-level 1 -o toc-only-4.html"],
    # }, {
    # 'name'   : 'toc-only-5',                  # with --enum-title
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["--toc-only --enum-title -o toc-only-5.html"],
    # }, {
    # 'name'   : 'no-toc-only-1',               # useless
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --no-toc-only"],
    # }, {
    # 'name'   : 'no-toc-only-2',               # turning OFF
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+TITLED_BODY,
    # 'cmdline': ["-H --toc-only --no-toc-only"],
    # }, {
    # 'name'   : 'mask-email',
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+EMAIL,
    # 'cmdline': ["-H --mask-email"],
    # }, {
    # 'name'   : 'no-mask-email-1',             # useless
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+EMAIL,
    # 'cmdline': ["-H --no-mask-email"],
    # }, {
    # 'name'   : 'no-mask-email-2',             # turning OFF
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+EMAIL,
    # 'cmdline': ["-H --mask-email --no-mask-email"],
    # }, {
    'name'   : 'encoding',                      # %!encoding: ...
    'content': '%!encoding: ISO-8859-2',
    'target' : 'html',
    'extra'  : ['noversion'],
    }, {
    'name'   : 'options-encoding',              # %!options: --encoding ...
    'target' : 'html',
    'content': '%!options: --encoding ISO-8859-2',
    'extra'  : ['noversion'],
    }, {
    'name'   : 'options-no-encoding',           # %!options: --encoding ... --no-encoding
    'target' : 'html',
    'content': '%!options: --encoding ISO-8859-2 --no-encoding',
    'extra'  : ['noversion'],
    }, {
    'name'   : 'style-1',                       # %!style: ...
    'content': '%!style: css1',
    'target' : 'html',
    'extra'  : ['noversion'],
    }, {
    'name'   : 'style-2',                       # %!style: ... %!style: ...
    'content': '%!style: css1\n%!style: css2',
    'target' : 'html',
    'extra'  : ['noversion'],
    }, {
    'name'   : 'options-style-1',               # %!options: --style ...
    'target' : 'html',
    'content': '%!options: --style css1',
    'extra'  : ['noversion'],
    }, {
    'name'   : 'options-style-2',               # %!options: --style ... --style ...
    'target' : 'html',
    'content': '%!options: --style css1 --style css2',
    'extra'  : ['noversion'],
    }, {
    'name'   : 'options-no-style',              # %!options: --style ... --no-style
    'target' : 'html',
    'content': '%!options: --style css1 --no-style',
    'extra'  : ['noversion'],
    }, {
    'name'   : 'options-css-sugar',             # %!options: --css-sugar
    'target' : 'html',
    'content': '%!options: --css-sugar',
    'extra'  : ['noversion'],
    }, {
    'name'   : 'options-no-css-sugar',          # %!options: --css-sugar --no-css-sugar
    'target' : 'html',
    'content': '%!options: --css-sugar --no-css-sugar',
    'extra'  : ['noversion'],
    }, {
    'name'   : 'options-css-inside-1',          # %!options: --css-inside
    'target' : 'html',
    'content': '%!options: --style css --css-inside',
    'extra'  : ['noversion', 'css'],
    }, {
    'name'   : 'options-css-inside-2',          # two CSS files
    'target' : 'html',
    'content': '%!options: --style css --style css --css-inside',
    'extra'  : ['noversion', 'css'],
    }, {
    'name'   : 'options-css-inside-3',          # two CSS files, one missing
    'target' : 'html',
    'content': '%!options: --style css --style missing.css --css-inside',
    'extra'  : ['noversion', 'css', 'error'],
    }, {
    'name'   : 'options-no-css-inside',         # %!options: --css-inside --no-css-inside
    'target' : 'html',
    'content': '%!options: --style css --css-inside --no-css-inside',
    'extra'  : ['noversion', 'css'],

    ### Now fully tested in test/includeconf
    # }, {
    # 'name'   : 'config-file',
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+SIMPLE_BODY,
    # 'cmdline': ["-H --config-file", lib.CONFIG_FILE],
    # 'extra'  : ['config', 'notarget'],
    # }, {
    # 'name'   : 'C',
    # 'target' : 'html',
    # 'content': EMPTY_HEADER+SIMPLE_BODY,
    # 'cmdline': ["-H -C", lib.CONFIG_FILE],
    # 'extra'  : ['config', 'notarget'],

    ### Working, but not really used in %!options:
    # --dump-config
    # --no-dump-config
    # --dump-source
    # --no-dump-source
    # --targets
    # --no-targets
    # See ../options/run.py for examples
    }
]

def run():
    for test in tests:
        target  = test.get('target') or 'txt'
        infile  = test['name'] + '.t2t'
        outfile = test.get('outfile') or test['name'] + '.' + target
        extra   = test.get('extra') or []
        cmdline = ['-i', infile] + test.get('cmdline', [])
        content = test['content']
        if 'noversion' in extra:
            content = VERSION_GOTCHA + content
        if 'error' in extra:
            outfile = test['name'] + '.out'
        if lib.initTest(test['name'], infile, outfile):
            # create the extra files (if needed for this test)
            if 'config' in extra:
                lib.WriteFile(lib.CONFIG_FILE, CONFIG_FILE_TXT)
            if 'css' in extra:
                lib.WriteFile(lib.CSS_FILE, CSS_FILE_TXT)
            # may I add the -t target automatically?
            if not 'notarget' in extra:
                cmdline = ['-t', target] + cmdline
            # may I redirect the output to a file?
            if test.get('redir'):
                cmdline.extend(test['redir'])
            elif 'error' in extra:
                cmdline.append('> %s.out' % test['name'])
            # always catch the error output
            cmdline.append('2>&1')
            # create the source file
            lib.WriteFile(infile, EMPTY_HEADER + content + '\n' + SIMPLE_BODY)
            # convert and check results
            lib.convert(cmdline)
            lib.diff(outfile)
            lib.convert(cmdline, True)
            lib.diff(outfile)
            # remove the trash
            os.remove(infile)
            if os.path.isfile(lib.CSS_FILE):
                os.remove(lib.CSS_FILE)
            if os.path.isfile(lib.CONFIG_FILE):
                os.remove(lib.CONFIG_FILE)
    return lib.OK, lib.FAILED, lib.ERROR_FILES

if __name__ == '__main__':
    print lib.MSG_RUN_ALONE
