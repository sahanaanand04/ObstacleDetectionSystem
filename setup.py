from setuptools import setup, find_packages

setup(
    name='ObstacleDetectionSystem',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tensorflow>=2.18.0',
        'torch>=2.5.1',
        'opencv-python>=4.10.0',
        'matplotlib>=3.3',
        'numpy>=1.23.5',
        'scipy>=1.4.1',
        'pillow>=10.3.0',
        'psutil',
        'requests',
        'pyyaml>=5.3.1',
    ],
    description='A system for object detection in obstacle avoidance',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://your_project_url.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

