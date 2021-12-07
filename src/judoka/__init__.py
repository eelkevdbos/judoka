from os.path import dirname, abspath

package_path = abspath(dirname(__file__))
completions_path = dirname(dirname(package_path)) + "/completions"
