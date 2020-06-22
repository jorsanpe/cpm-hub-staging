import yaml
import os

import bit_code_generator


def __add_package(project_directory, package_name):
    os.mkdir(f'{project_directory}/{package_name}')
    with open(f'{project_directory}/project.yaml') as stream:
        project_descriptor = yaml.safe_load(stream)
    project_descriptor['packages'] = {
        package_name: None
    }
    with open(f'{project_directory}/{package_name}/{package_name}.cpp', 'w+') as stream:
        stream.write(bit_code_generator.generate_c_function())
    with open(f'{project_directory}/project.yaml', 'w') as stream:
        yaml.dump(project_descriptor, stream)


def __set_version(project_directory, version):
    with open(f'{project_directory}/project.yaml') as stream:
        project_descriptor = yaml.safe_load(stream)
    project_descriptor['version'] = version
    with open(f'{project_directory}/project.yaml', 'w') as stream:
        yaml.dump(project_descriptor, stream)


def bootstrap(project_directory, project_name):
    __add_package(project_directory, project_name)
    __set_version(project_directory, '1.0')

