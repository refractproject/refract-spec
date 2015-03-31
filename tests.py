import os
import json
from jsonschema import validate


def load_suite(path):
    with open(path) as fp:
        return json.load(fp)


def print_ansi(code, text):
    print('\033[{}m{}\x1b[0m'.format(code, text))


print_bold = lambda text: print_ansi(1, text)
print_green = lambda text: print_ansi(32, text)
print_red = lambda text: print_ansi(31, text)


if __name__ == '__main__':
    with open('refract-schema.json') as fp:
        schema = json.load(fp)

    suite_directory = 'refract-schema-tests'
    join_path = lambda path: os.path.join(suite_directory, path)
    is_json = lambda path: path.endswith('.json')
    suite_paths = map(join_path, filter(is_json, os.listdir(suite_directory)))

    suites = map(load_suite, suite_paths)

    passes = 0
    failures = 0

    for suite in suites:
        for case in suite:
            print_bold('-> {}'.format(case['description']))

            for test in case['tests']:
                success = True

                try:
                    validate(test['data'], schema)
                except Exception as e:
                    if test['valid']:
                        success = False
                else:
                    if not test['valid']:
                        success = False

                if success:
                    passes += 1
                    print_green('  -> {}'.format(test['description']))
                else:
                    failures += 1
                    print_red('  -> {}'.format(test['description']))
                    print('    Expected data to validate as: {}'.format(test['valid']))
                    print('    ' + json.dumps(test['data']))
                    print('')

            print('')

    print('{} passes, {} failures'.format(passes, failures))

    if failures:
        exit(1)

