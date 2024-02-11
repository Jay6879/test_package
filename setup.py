import setuptools 

with open("README.md", "r") as fh: 
	description = fh.read() 

setuptools.setup( 
	name="test-package", 
	version="0.0.1", 
	author="jyoshilchandana", 
	author_email="jyoshilchandana@gmail.com", 
	packages=["test_package"], 
	description="A sample test package", 
	long_description=description, 
	long_description_content_type="text/markdown", 
	url="Jay6879", 
	license='MIT', 
	python_requires='>=3.8', 
	install_requires=[] 
) 
