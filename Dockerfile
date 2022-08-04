FROM public.ecr.aws/lambda/python:3.8
#FROM python:3.8-slim


#WORKDIR /code
COPY doc_classifier/ ${LAMBDA_TASK_ROOT}/doc_classifier/

#COPY ./lambda_function.py ./
COPY lambda_function.py ${LAMBDA_TASK_ROOT}
#COPY ./lambda_function.py /code/lambda_function.py

#COPY poetry.lock ${LAMBDA_TASK_ROOT}

COPY pyproject.toml ${LAMBDA_TASK_ROOT}


ENV PATH /home/$(python3 -m site --user-base)/.local/bin:${PATH}

#ENV PATH="${PATH}:/root/.poetry/bin"

#COPY requirements.txt  .
#RUN pip3 install --upgrade pip
#RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
RUN pip install poetry mangum  && poetry config virtualenvs.create false && poetry update && poetry install

#RUN pip install poetry && poetry install

#COPY ./doc_classifier /code/doc_classifier
#CMD ["uvicorn", "doc_classifier.main:app", "--host", "0.0.0.0", "--port", "8000"]
#ENTRYPOINT ["/lambda-entrypoint.sh", "/lambda_function.lambda_handler"] 
#CMD [ "lambda_function.lambda_handler" ]
CMD [ "lambda_function.lambda_handler" ]