from setuptools import setup

package_name = 'my_turtle_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Turtle control package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = my_turtle_package.move_turtle:main',
            'circle_turtle = my_turtle_package.circle_turtle:main',
            'triangle_turtle = my_turtle_package.triangle_turtle:main',
            'multi_turtle = my_turtle_package.multi_turtle:main',
            'go_to_goal = my_turtle_package.go_to_goal:main',
        ],
    },
)

