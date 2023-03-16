from setuptools import setup

package_name = 'py_pubsub'

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
    maintainer='ros',
    maintainer_email='126540662+nws01@users.noreply.github.com',
    description='ROS2 Publisher/Subscriber Tutorial',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'talker = py_pubsub.publisher_member_function:main', 'listener = py_pubsub.subscriber_member_function:main',
        ],
    },
    
)
