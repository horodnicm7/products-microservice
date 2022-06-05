python3 -m venv products-venv
source products-venv/bin/activate

pip install -r requirements-development.txt
pip install "uvicorn[standard]"  # it will install the uvicorn server