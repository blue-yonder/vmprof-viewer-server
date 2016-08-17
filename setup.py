from setuptools import setup

setup(
    name="vmprof-viewer",
    author="Jonas Haag",
    author_email="jonas.haag@blue-yonder.com",
    version="1.0.0",
    packages=["vmprof_viewer", "profiles", "profiles.migrations"],
    include_package_data=True,
    zip_safe=False,
    install_requires=["vmprof", "django>=1.9", "msgpack-python", "pandas"],
)
