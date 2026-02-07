from pathlib import Path

from setuptools import find_packages, setup

ROOT = Path(__file__).resolve().parent

setup(
    name="genz_icp",
    version="0.3.0",
    description="GenZ-ICP: LiDAR odometry with Geometric CNN cues",
    long_description=(ROOT / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    license_files=["LICENSE"],
    package_dir={"": "python"},
    packages=find_packages("python"),
    include_package_data=True,
)
