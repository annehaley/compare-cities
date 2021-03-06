FROM ubuntu:20.04

# Install system libraries for Python packages:
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends --yes \
        # C/C++ compilers and C standard library development files
        gcc g++ binutils g++ libc6-dev \
        # Python
        python-is-python3 python3-dev python3-pip \
        # PostgreSQL library development files (psycopg2)
        libpq-dev \
        # GDAL development files and binary (GeoDjango)
        libgdal-dev gdal-bin gdal-data \
        # PROJ development files and binary (GeoDjango)
        libproj-dev proj-bin proj-data \
        # GEOS library development files (GeoDjango)
        libgeos-dev \
    && pip install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install \
        # pyvips==2.0 \
        # constrain GDAL for use with Ubuntu Focal library version
        gdal==3.0.4 \
        # constrain pyproj for use with Ubuntu Focal library version
        pyproj~=2.0


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /opt/django-project/


# Use a directory name which will never be an import name, as isort considers this as first-party.
WORKDIR /opt/django-project

RUN pip install -r requirements.txt
