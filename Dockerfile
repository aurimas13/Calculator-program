# Simple docker file 
# Dockerfile for Calculator program
#
# Created by Aurimas A. Nausedas on 05/29/21.
# Uploaded by Aurimas A. Nausedas on 05/29/21.
# Updated by Aurimas A. Nausedas on 11/05/21.

FROM python:3.8.10-slim
RUN pip install typing
RUN pip install python-math
WORKDIR /calculator/calculatorpackage
COPY . .
CMD ["python", "./calculator/calculator.py"]
