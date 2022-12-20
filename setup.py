import setuptools

setuptools.setup(
    name="workshop_lib",
    version="0.0.1",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["numpy", "pandas"],
)

print(setuptools.find_packages())
