import setuptools
import release_bot_test

setuptools.setup(
    name="release_bot_test_b3xw5IBKShQLb0sT",
    version=release_bot_test.__version__,
    author="User Cont",
    author_email="user-cont@redhat.com",
    description="A small example package used fo release-bot testing",
    long_description="Test",
    long_description_content_type="text/markdown",
    url="https://github.com/usercont-release-bot/release-bot-test-b3xw5IBKShQLb0sT",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)